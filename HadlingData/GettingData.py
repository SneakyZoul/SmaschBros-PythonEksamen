import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('../Data/students.csv')
ldata = data# .iloc[:0, :]

def fetchingData(datas):
    datas = data[['first_name','ged']] #laver et nyt DataFrame ud fra de "navne" du gere vil have
    df = datas.dropna()

    print(df)
    return df

    


if __name__ == '__main__':
    print(ldata)
    fetchingData(data.head())




