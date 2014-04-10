from marketsim import registry
from marketsim.gen._out.strategy.side._sidestrategy import SideStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["-", "Noise"])
class Noise_Float(SideStrategy):
    """ 
    """ 
    def __init__(self, side_distribution = None):
        from marketsim.gen._out.math.random._uniform import uniform_FloatFloat as _math_random_uniform_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.side_distribution = side_distribution if side_distribution is not None else deref_opt(_math_random_uniform_FloatFloat(0.0,1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side_distribution' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Noise(%(side_distribution)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.side_distribution.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    

    @property
    def Side_distribution(self):
        from marketsim.gen._out.strategy.side._side_distribution import Side_distribution
        return Side_distribution(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    pass
Noise = Noise_Float
