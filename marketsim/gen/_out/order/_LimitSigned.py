# generated with class generator.python.order_factory$Factory
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
@registry.expose(["Order", "LimitSigned"])
class LimitSigned_FloatFloat(ObservableIOrder,IObservableIOrder):
    """ **Factory creating limit orders**
    
    
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    
    Parameters are:
    
    **signedVolume**
    	signed volume
    
    **price**
    	 function defining price of orders to create 
    """ 
    def __init__(self, signedVolume = None, price = None):
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else deref_opt(_constant_Float(1.0))
        self.price = price if price is not None else deref_opt(_constant_Float(100.0))
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunctionfloat,
        'price' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "LimitSigned(%(signedVolume)s, %(price)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.signedVolume.bind_ex(self._ctx_ex)
        self.price.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.signedVolume.reset_ex(generation)
        self.price.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.signedVolume)
        rtti.typecheck(IFunctionfloat, self.price)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.signedVolume.registerIn(registry)
        self.price.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._out._side import Side
        from marketsim.gen._intrinsic.order.limit import Order_Impl
        signedVolume = self.signedVolume()
        if signedVolume is None: return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        volume = abs(signedVolume)
        if abs(volume) < 1: return None
        volume = int(volume)
        price = self.price()
        if price is None: return None
        
        return Order_Impl(side, price, volume)
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
def LimitSigned(signedVolume = None,price = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunctionfloat):
        if price is None or rtti.can_be_casted(price, IFunctionfloat):
            return LimitSigned_FloatFloat(signedVolume,price)
    raise Exception('Cannot find suitable overload for LimitSigned('+str(signedVolume) +':'+ str(type(signedVolume))+','+str(price) +':'+ str(type(price))+')')
