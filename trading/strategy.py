import pandas as pd

from trading.metrics import low_ratio



def apply_stop(data: pd.DataFrame,
               equity: pd.Series,
               stop_limit: pd.Series
               ) -> pd.Series:
    """Apply stop on an equity, looking
    at historical data of the asset

    Args:
        data (pd.DataFrame): Historical data
        of the asset
        equity (pd.Series): Value of the portfolio
        after each day
        stop_limit (pd.Series): Limit ratio for
        the stop order

    Returns:
        pd.Series: Equity with stop loss applied
    """
    stop_cond =  low_ratio(data) < stop_limit
    return equity.where(~stop_cond).fillna(-1)



def hold(timeseries: dict)-> dict:
    """Strategy which consists only to
    hold the asset.

    Args:
        timeseries (dict): Dictionnary of
        historical daily data of the asset

    Returns:
        dict: Equity for each asset
    """
    res = dict()
    for symbol, data in timeseries.items():
        index_min = data.index.min()
        initial_price = data['open'].loc[index_min]
        res[symbol] = data['close'] / initial_price
    return res