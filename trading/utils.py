import os
import json

import pandas as pd



def save_data(datas: list, output_path: str) -> None:
    """Save the data extracted from API

    Args:
        data (list): List of tuples.
        Each tuple contains timeseries market data and
        metadata of the request to get timeseries
        output_path (str): Place to save the data
    """
    for data in datas:
        symbol = data[1]["2. Symbol"]
        directory = output_path + symbol
        os.mkdir(directory)
        data[0].to_parquet(directory + '/data.parquet')
        with open(directory + '/meta_data.json', 'w') as f:
            json.dump(data[1], f)


def load_data(input_path: str) -> dict:
    """Load the data extracted from API

    Args:
        input_path (str): Place to load the data

    Returns:
        dict: Dict of tuples.
        Each tuple contains timeseries market data and
        metadata of the request to get timeseries
    """
    datas = dict()
    for object in os.listdir(input_path):
        directory = input_path + object
        if os.path.isdir(directory):
            timeseries = pd.read_parquet(
                directory + '/data.parquet')
            with open(directory + '/meta_data.json', 'r') as f:
                metadata = json.load(f)
            datas[metadata["2. Symbol"]] = (timeseries, metadata)
    return datas