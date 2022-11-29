import os
import pandas as pd
from config.definitions import ROOT_DIR

champ_data = pd.read_csv(os.path.join(ROOT_DIR, 'data', 'try_data.csv'))
Champ1 = {'Name': "Pica", 'Speed': "fast", 'PlayStyle': "Combo"}
Champ2 = {'Name': "Mario", 'Speed': "fast", 'PlayStyle': "kill"}
Champ3 = {'Name': "Steve", 'Speed': "slow", 'PlayStyle': "Special"}


def making_it_to_a_dict(data):
    chmp_data = pd.DataFrame(data)
    champ = chmp_data.set_index('Name').to_dict()['Play-style']

    print(champ)


def making_a_dataframe(champ1):
    # Her skal navnene så sættes op mod hinanden i et dataframe med deres data

    df2 = pd.DataFrame(champ1)
    print(df2)

    return df2


if __name__ == '__main__':
    making_a_dataframe()
