import pandas as pd

def load_data(datapath):
    return pd.read_csv(datapath)

def get_data_descriptive_stats(dataframe):
    statistics = {
        'Mean': dataframe.mean(numeric_only=True),
        'Median': dataframe.median(numeric_only=True),
        'StdDev': dataframe.std(numeric_only=True),
        'Min': dataframe.min(numeric_only=True),
        'Max': dataframe.max(numeric_only=True)
    }
    return pd.Series(statistics)