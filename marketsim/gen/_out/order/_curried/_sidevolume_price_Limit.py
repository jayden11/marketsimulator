from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class sidevolume_price_Limit(IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self):
        pass
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "sidevolume_price_Limit" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._price_Limit import price_Limit
        side = side if side is not None else _side_Sell()
        volume = volume if volume is not None else _constant(1.0)
        
        return price_Limit(side, volume)
    