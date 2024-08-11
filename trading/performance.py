import pandas as pd



def get_performance(equity: pd.Series) -> pd.Series:
    """Get overall performance of a strategy,
    giving the equity resulting from the strategy.

    Args:
        equity (pd.Series): Value of the portfolio
        after each day

    Returns:
        pd.Series: Overall performance of the strategy
    """
    index_min = equity.index.min()
    index_max = equity.index.max()
    performance = equity.loc[index_max] / equity.loc[index_min]
    delta_time = index_max - index_min
    # Gregorian average number of days within a year
    delta_years = delta_time.days /  365.2425
    annual_performance = (performance - 1) ** (1/delta_years) - 1
    res = {
        'Years': delta_years,
        'Overall performance': performance,
        'Annual performance': annual_performance
    }
    return pd.Series(res)
