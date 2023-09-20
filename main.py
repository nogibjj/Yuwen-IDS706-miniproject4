import pandas as pd
import matplotlib.pyplot as plt

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

def plot_hist(dataframe, col):
    """Plot histogram of the given column"""
    plt.figure(figsize=(3.1104,2.0736))
    plt.hist(dataframe[col], bins=10, color='green', edgecolor='black', linewidth=1.2)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    visualization_path = 'output/visualization_hist.png'
    plt.savefig(visualization_path)  # save png
