import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('./Data/data.csv')

def fetchingData():
    datas = pd.DataFrame(data) #laver et nyt DataFrame ud fra de "navne" du gere vil have
    df = datas.dropna()
    return df

    


if __name__ == '__main__':
    print(fetchingData())




