import pandas as pd
champ_data = pd.read_csv('../Data/TryData.csv')
Champ1 = {'Name': "Pica", 'Speed': "fast", 'PlayStyle': "Combo"}
Champ2 = {'Name': "Mario", 'Speed': "fast", 'PlayStyle':"kill"}
Champ3 = {'Name': "Steve", 'Speed': "slow", 'PlayStyle':"Special"}



def making_it_to_a_dict(data):
     cData = pd.DataFrame(data)
     champ = cData.set_index('Name').to_dict()['Play-style']

     print(champ)


def making_a_dataframe(champ1):
    ##her skal navnene så sættes op mod hiandne i et dataframe med deres data

    df2 = pd.DataFrame(champ1)
    print(df2)

    return df2



if __name__ =='__main__':
    making_a_dataframe()

