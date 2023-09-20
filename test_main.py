from main import load_data, get_data_descriptive_stats, plot_hist
import pandas as pd
import matplotlib.pyplot as plt

def test_loaddata():
    #load iris dataset
    path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    iris_df = load_data(path)
    assert isinstance(iris_df, pd.DataFrame)
    assert not iris_df.empty

def test_descriptive_stats():
    path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    iris_df = load_data(path) 
    statistics = get_data_descriptive_stats(iris_df)
    assert statistics['Mean']['sepal_length'] == 5.843333333333334


def test_plot_hisogram():
    path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    iris_df = load_data(path) 
    plot_hist(iris_df, 'sepal_length')
    fig = plt.gcf()
    assert len(fig.axes) > 0