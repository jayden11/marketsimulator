
package strategy {
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                              /** order factory function*/ orderFactory = order._.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell(),
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = mathutils.rnd.lognormvariate(0.0,0.1))
         = Generic(orderFactory(side,observable.pricefunc.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    /** Liquidity provider for two sides
     */
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                          /** order factory function*/ orderFactory = order._.side_price.Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr = mathutils.rnd.lognormvariate(0.0,0.1))
         = Combine(LiquidityProviderSide(eventGen,orderFactory,side.Sell(),initialValue,priceDistr),LiquidityProviderSide(eventGen,orderFactory,side.Buy(),initialValue,priceDistr))
    
    /** A Strategy that allows to drive the asset price based on historical market data
     *  by creating large volume orders for the given price.
     *
     *  Every time step of 1 in the simulation corresponds to a 1 day in the market data.
     *
     *  At each time step the previous Limit Buy/Sell orders are cancelled and new ones
     *  are created based on the next price of the market data.
     */
    def MarketData(/** Ticker of the asset */ ticker = "^GSPC",
                   /** Start date in DD-MM-YYYY format */ start = "2001-1-1",
                   /** End date in DD-MM-YYYY format */ end = "2010-1-1",
                   /** Price difference between orders placed and underlying quotes */ delta = 1.0,
                   /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0)
         = Combine(Generic(order.Iceberg(constant(volume),order.FloatingPrice(observable.BreaksAtChanges(observable.Quote(ticker,start,end)+delta),order._.price.Limit(side.Sell(),constant(1000000)))),event.After(constant(0.0))),Generic(order.Iceberg(constant(volume),order.FloatingPrice(observable.BreaksAtChanges(observable.Quote(ticker,start,end)-delta),order._.price.Limit(side.Buy(),constant(1000000)))),event.After(constant(0.0))))
}