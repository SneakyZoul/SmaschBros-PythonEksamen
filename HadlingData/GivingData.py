import pandas as pd

Champ1 = {'name': "Pica", 'type': "fast", 'playStyle': "Combo"}
Champ2 = {'name': "Mario", 'type': "fast", 'playStyle':"kill"}
Champ3 = {'name': "Steve", 'type': "slow", 'playStyle':"Special"}


def making_a_dataframe(champ1,champ2,champ3):
    ##her skal navnene så sættes op mod hiandne i et dataframe med deres data
    df2 = pd.DataFrame([champ1,champ2,champ3])
    print(df2)

if __name__ =='__main__':
    making_a_dataframe(Champ1,Champ2,Champ3)
