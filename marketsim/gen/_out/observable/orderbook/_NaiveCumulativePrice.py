from marketsim import registry
from marketsim import Price
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import IFunction
from marketsim import context
@registry.expose(["Asset's", "NaiveCumulativePrice"])
class NaiveCumulativePrice(Observable[Price]):
    """ 
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import _
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _observable_orderbook_OfTrader()
        self.depth = depth if depth is not None else _constant()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction[float]
    }
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._ObservablePrice import ObservablePrice as _observable_ObservablePrice
        from marketsim.gen._out.observable.orderbook.ask._Price import Price as _observable_orderbook_ask_Price
        from marketsim.gen._out.observable.orderbook.bid._Price import Price as _observable_orderbook_bid_Price
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out._const import const as _const
        return _observable_ObservablePrice((self.depth<_const(0.0))[self.depth*_observable_orderbook_ask_Price(self.book), (self.depth>_const(0.0))[self.depth*_observable_orderbook_bid_Price(self.book), _const(0.0)]])
        
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
