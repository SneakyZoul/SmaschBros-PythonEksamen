import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('../Data/students.csv')
ldata = data# .iloc[:0, :]

def fetchingData(datas):
    datas = data[['first_name','last_name','ged']]
    df = datas.dropna()

    print(df)

def plottingTheData(fdata):
    


if __name__ == '__main__':
    print(ldata)
    fetchingData(data.head())




