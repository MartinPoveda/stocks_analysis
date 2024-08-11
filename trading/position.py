import pandas as pd

from trading import metrics, strategy


def session_position(data: pd.DataFrame,
                     stop_limit: pd.Series=-1
                     ) -> pd.Series:
    """Position opened at the open of the session
    and close at the close of the session for
    a given asset

    Args:
        data (pd.DataFrame):  Historical data
        of the asset
        stop_limit (pd.Series, optional): Limit ratio for
        the stop order.
        Defaults to -1 (no stop).

    Returns:
        pd.Series: Ratio of performance compared to the
        stop limit for each day
    """
    res = - metrics.delta_session_ratio(data) / stop_limit
    return strategy.apply_stop(data, res, stop_limit)