import os
import pandas as pd
from config.definitions import ROOT_DIR

data = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'data.csv'))


def fetching_data():
    datas = pd.DataFrame(data)  # laver et nyt DataFrame ud fra de "navne" du gere vil have
    df = datas.dropna()
    return df


def fetching_images():
    # Removes spaces, makes names lowercase and adds .png to the string
    names = [name.replace(" ", '').lower() + ".png" for name in data['character']]
    paths = []
    for name in names:
        paths.append(os.path.join(ROOT_DIR, 'data/img', name))

    return paths


if __name__ == '__main__':
    print(fetching_data())


