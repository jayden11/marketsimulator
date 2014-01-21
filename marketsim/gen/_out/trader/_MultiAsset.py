from marketsim import registry
from marketsim.gen._intrinsic.trader.classes import _MultiAsset_Impl
from marketsim import listOf
from marketsim import ISingleAssetTrader
from marketsim import IMultiAssetStrategy
from marketsim import listOf
from marketsim import ITimeSerie
@registry.expose(["Trader", "MultiAsset"])
class MultiAsset(_MultiAsset_Impl):
    """ 
    """ 
    def __init__(self, traders = None, strategy = None, name = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._Arbitrage import Arbitrage as _strategy_Arbitrage
        self.traders = traders if traders is not None else []
        self.strategy = strategy if strategy is not None else _strategy_Arbitrage()
        self.name = name if name is not None else "-trader-"
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        _MultiAsset_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'traders' : listOf(ISingleAssetTrader)
        ,
        'strategy' : IMultiAssetStrategy,
        'name' : str,
        'PnL' : float,
        'timeseries' : listOf(ITimeSerie)
        
    }
    def __repr__(self):
        return "%(name)s" % self.__dict__
    