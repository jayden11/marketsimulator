# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._intrinsic.strategy.account import Account_Impl
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "Real"])
class Real_ISingleAssetStrategy(IAccount,Account_Impl):
    """ **Associated with a strategy account that tracks**
    
      how orders sent by the strategy have been actually traded
    
    Parameters are:
    
    **inner**
    	 strategy to track 
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        rtti.check_fields(self)
        Account_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    
    
    def __repr__(self):
        return "Real(%(inner)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        self.inner.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
def Real(inner = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        return Real_ISingleAssetStrategy(inner)
    raise Exception('Cannot find suitable overload for Real('+str(inner) +':'+ str(type(inner))+')')
def real(): 
    from marketsim.gen._out.strategy.account.inner._inner_real import inner_Real_ as _strategy_account_inner_inner_Real_
    from marketsim import rtti
    return _strategy_account_inner_inner_Real_()
    raise Exception('Cannot find suitable overload for real('++')')