from main import load_data, get_data_descriptive_stats
import pandas as pd

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


