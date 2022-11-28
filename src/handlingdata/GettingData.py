import os
import numpy as np
import pandas as pd
import matplotlib as plt
from config.definitions import ROOT_DIR

data = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'data.csv'))


def fetching_data():
    datas = pd.DataFrame(data)  # laver et nyt DataFrame ud fra de "navne" du gere vil have
    df = datas.dropna()
    return df


if __name__ == '__main__':
    print(fetching_data())
