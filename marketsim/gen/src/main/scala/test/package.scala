import marketsim._
import marketsim.orderbook.BestPrice
import marketsim.Scheduler._

package object test
{
    case class OrderEvents(trace : String => Unit, name : String) extends OrderListener
    {
        def OnTraded(order : Order, price : Ticks, volume : Volume)
        {
            trace(s"$order traded at $price with $volume")
        }

        def OnStopped(order : Order, unmatchedVolume : Volume)
        {
            trace(order + (if (unmatchedVolume != 0) " canceled" else " matched completely"))
        }

        override def toString = name
    }

    def withLogging(trace : String => Unit)(book : Orderbook) =
    {
        def OnBestChanged(sender : String, pv : Option[Ticks])
        {
            trace(s"best of $sender changed = " + pv)
        }

        def OnTraded(sender : String, pv : (Ticks, Int))
        {
            trace(sender + " on_traded: " + pv)
        }

        val bestAsk = BestPrice(book.Asks)
        val bestBid = BestPrice(book.Bids)

        bestAsk += { OnBestChanged("asks", _) }
        bestBid += { OnBestChanged("bids", _) }

        import marketsim.math.Cumulative

        Cumulative.Min(bestAsk) += { OnBestChanged("min ask", _) }
        Cumulative.Max(bestBid) += { OnBestChanged("max bid", _) }

        book.Asks.TradeDone += { OnTraded("asks", _) }
        book.Bids.TradeDone += { OnTraded("bids", _) }

        98 to 105 foreach { i =>
            val handler = (i, () => trace("ask is less than " + i.toString))
            val source = OnceLessThan(orderbook.BestPrice(book.Asks))
            source += handler
            if (i == 102)
                source -= handler

        }

        98 to 105 foreach { i =>
            val handler = (i, () => trace("bid is greater than " + i.toString))
            val source = OnceGreaterThan(orderbook.BestPrice(book.Bids))
            source += handler
            if (i == 99)
                source -= handler
        }

        book
    }

    class LoggedAccount(trace_ : String => Unit, book : Orderbook, name : String)
    {
        val account = new marketsim.Account(book)

        def trace(s : String) = trace_(s"$name : $s")

        account.OrderSent += { order => trace(s"sending $order") }
        account.OrderTraded += { case (order, price, volume)  =>
            trace(s"$order traded $volume at $price")
            trace(s"position = ${account.getPosition}; balance = ${account.getBalance}")
        }
        account.OrderStopped += { case (order, unmatched) =>
            trace(order + (if (unmatched == 0) " matched completely" else " unmatched volume: " + unmatched )) }

        val ordersSent = new PendingOrders(account)

        def sendOrder(factory : OrderFactory) {
            trace("before = " + book)
            val order = factory.create
            account send order
            async {
                trace("after = " + book)
                trace("")
            }
        }

        def cancel(order : Order) {
            trace("cancelling " + order)
            account send CancelOrder(order)
        }
    }


}
