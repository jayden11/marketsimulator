# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._fundamentalvaluestrategy import FundamentalValueStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["-", "FundamentalValue"])
class FundamentalValue_Float(FundamentalValueStrategy):
    """ 
    """ 
    def __init__(self, fv = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.fv = fv if fv is not None else deref_opt(_constant_Float(200.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "FundamentalValue(%(fv)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.fv.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    

    @property
    def Fundamental_Value(self):
        from marketsim.gen._out.strategy.side._fundamental_value import Fundamental_Value
        return Fundamental_Value(self)
    
    @property
    def book(self):
        from marketsim.gen._out.strategy.side._book import book
        return book(self)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Fv(self):
        from marketsim.gen._out.strategy.side._fv import Fv
        return Fv(self)
    
    pass
FundamentalValue = FundamentalValue_Float