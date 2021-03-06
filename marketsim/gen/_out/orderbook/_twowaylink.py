# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._itwowaylink import ITwoWayLink
from marketsim.gen._intrinsic.orderbook.link import TwoWayLink_Impl
from marketsim.gen._out._ilink import ILink
@registry.expose(["Asset", "TwoWayLink"])
class TwoWayLink_ILinkILink(ITwoWayLink,TwoWayLink_Impl):
    """ **Represents latency in information propagation between two agents**
    
     (normally between a trader and a market).
     Ensures that sending packets via links preserves their order.
     Holds two one-way links in opposite directions.
    
    Parameters are:
    
    **up**
    	 Forward link (normally from a trader to a market)
    
    **down**
    	 Backward link (normally from a market to a trader)
    """ 
    def __init__(self, up = None, down = None):
        from marketsim.gen._out.orderbook._link import Link_IObservableFloat as _orderbook_Link_IObservableFloat
        from marketsim import deref_opt
        self.up = up if up is not None else deref_opt(_orderbook_Link_IObservableFloat())
        self.down = down if down is not None else deref_opt(_orderbook_Link_IObservableFloat())
        TwoWayLink_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'up' : ILink,
        'down' : ILink
    }
    
    
    
    
    def __repr__(self):
        return "TwoWayLink(%(up)s, %(down)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.up.bind_ex(self._ctx_ex)
        self.down.bind_ex(self._ctx_ex)
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
        self.up.reset_ex(generation)
        self.down.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ilink import ILink
        rtti.typecheck(ILink, self.up)
        rtti.typecheck(ILink, self.down)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.up.registerIn(registry)
        self.down.registerIn(registry)
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
    
    def bind_impl(self, ctx):
        TwoWayLink_Impl.bind_impl(self, ctx)
    
    def reset(self):
        TwoWayLink_Impl.reset(self)
    
def TwoWayLink(up = None,down = None): 
    from marketsim.gen._out._ilink import ILink
    from marketsim import rtti
    if up is None or rtti.can_be_casted(up, ILink):
        if down is None or rtti.can_be_casted(down, ILink):
            return TwoWayLink_ILinkILink(up,down)
    raise Exception('Cannot find suitable overload for TwoWayLink('+str(up) +':'+ str(type(up))+','+str(down) +':'+ str(type(down))+')')
