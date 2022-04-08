import pandas as pd
import numpy as np
a = pd.read_csv(r'C:\Users\User\Desktop\TEPAV\TEPAV-DATABASE\il_bazinda_gsyh\il_bazinda_gsyh.csv', sep = '|' )
a = a.ffill()
del[a['Unnamed: 0']]
a.columns = ['veri', 'yıl']+list(a.loc[0,:][2:])
a = a[a['veri']  == a['veri'].unique()[1]]
del(a['veri'])
a = a.T.reset_index()
a.columns = ['İl']+list(a.loc[0,:])[1:]
a = a.iloc[1:,:]
a = a.dropna()
liste = list()
for ill in a['İl']:
    liste.append(ill.split('-')[0].strip())
a['İl'] = liste
a = a.reset_index(drop=True)
b = a.columns[1:]
for column in b:
    c = a[column]
    liste = list()
    for element in c:
        liste.append(float(element))
    a[column] = liste
a.to_excel(r'C:\Users\User\Desktop\TEPAV\TEPAV-DATABASE\il_bazinda_gsyh\il_bazinda_gsyh.xlsx', index=False)