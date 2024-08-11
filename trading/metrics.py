import pandas as pd



def low_ratio(data: pd.DataFrame) -> pd.Series:
    """Compute the low_ratio for each day
    of the asset

    Args:
        data (pd.DataFrame): Historical data
        of the asset

    Returns:
        pd.Series: Low_ratio for each day
        of the asset
    """
    return (data['low'] - data['open']) / data['close']



def delta_session_ratio(data: pd.DataFrame) -> pd.Series:
    """Compute the delta of the session for each day
    of the asset

    Args:
        data (pd.DataFrame): Historical data
        of the asset

    Returns:
        pd.Series: the delta of the session
        for each day of the asset
    """
    return (data['close'] - data['open']) / data['close']



def decrease_session_quantile(data: pd.DataFrame,
                              quantile: float=0.05,
                              condition= lambda x: x>0
                              ) -> float:
    """Look at the low ratio of a certain quantile,
    with condition of the delta of the session

    Args:
        data (pd.DataFrame): Historical data
        of the asset
        quantile (float): Quantile of the
        historical decreases
        condition (callable): Condition for
        the delta session ratio
    Returns:
        float: Low ratio of a certain quantile,
        with condition of the delta of the session
    """
    low = low_ratio(data)
    delta = delta_session_ratio(data)
    return low.where(condition(delta)).quantile(quantile)
