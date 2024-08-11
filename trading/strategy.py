import pandas as pd



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