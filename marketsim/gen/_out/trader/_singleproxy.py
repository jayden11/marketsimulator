from marketsim import registry
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._intrinsic.trader.proxy import Single_Impl
@registry.expose(["Trader", "SingleProxy"])
class SingleProxy_(ISingleAssetTrader,Single_Impl):
    """ **Phantom trader that is used to refer to the current trader**
    
      (normally it is used to define trader properties and strategies)
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        Single_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    
def SingleProxy(): 
    from marketsim import rtti
    return SingleProxy_()
    raise Exception('Cannot find suitable overload for SingleProxy('++')')
