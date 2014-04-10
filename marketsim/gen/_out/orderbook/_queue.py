from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.proxy import Queue_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "Queue"])
class Queue_IOrderBookSide(IOrderQueue,Queue_Impl):
    """ **Returns order queue of order *book* for trade *side***
    
    
    Parameters are:
    
    **book**
    
    **side**
    """ 
    def __init__(self, book = None, side = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        self.side = side if side is not None else deref_opt(_side_Sell_())
        rtti.check_fields(self)
        Queue_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'side' : IFunctionSide
    }
    
    
    
    
    def __repr__(self):
        return "Queue(%(book)s, %(side)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.book.bindEx(self._ctx_ex)
        self.side.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Queue(book = None,side = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            return Queue_IOrderBookSide(book,side)
    raise Exception('Cannot find suitable overload for Queue('+str(book) +':'+ str(type(book))+','+str(side) +':'+ str(type(side))+')')
