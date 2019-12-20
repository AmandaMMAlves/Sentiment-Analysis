# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:21:57 2018


@author: Amanda Mayara Menino   | GitHub: https://github.com/AmandaMMAlves
@author: Carla A. Madureira     | GitHub: https://github.com/carlalmadureira
"""
import pandas as pd

path = "massas-extraidas-rotuladas/"
filenames = [
    path + '#EleNunca.xlsx',
    path + '#HaddadSim.xlsx',
    path + '#MudaBrasil17.xlsx',
    path + '#nordestee17.xlsx',
    path + '#Bolsonaro.xlsx',
    path + '#viravotohaddad.xlsx',
    path + '#vivavirouhaddad.xlsx',
    path + '#ptnao.xlsx',
    path + '#Bolsonaro17.xlsx',
#    path + '#HaddadSim.xlsx',
    path + '#haddadmanu13.xlsx',
    path + '#mulhervotahaddad.xlsx',
    path + '#pelademocracia.xlsx',
    path + '#manunojaburu.xlsx',
    path + '#haddadpresidente13.xlsx'
]


def count_tweets(rot_list):
    count_H = 0
    count_B = 0
    count_L = 0

    for r in rot_list:
        if r == 'B' or r == 'b':
            count_B += 1
        elif r == 'H' or r == 'h':
            count_H += 1
        else:
            count_L += 1
        
    print("\nQuantidade de tweets rotulados: " + str(len(rot_list)))
    print("\nQuantidade de tweets a favor do Bolsonaro: " + str(count_B))
    print("\nQuantidade de tweets a favor do Haddad: " + str(count_H))
    print("\nQuantidade de tweets utilizáveis: " + str(count_H + count_B))
    print("\nQuantidade de tweets lixos: " + str(count_L))

rot_all = []
ids_all = []
tweets_all = []

for f in filenames:
    dataset = pd.read_excel(f, dtype=str)
    ids = dataset['ID'].values
    tweets = dataset['Tweets'].values
    rot = dataset['Rotulacoes'].values
    ids_all += ids.tolist()
    tweets_all += tweets.tolist()
    rot_all += rot.tolist()
    print("\nDados do " + f)
    count_tweets(rot)
    
print("\n\n\nTotal")
count_tweets(rot_all)

dict_ = {'ID': ids_all, 'Tweets': tweets_all, 'Rotulacoes': rot_all}
df = pd.DataFrame(data=dict_)

max_balanceado = 1285
id_o = []
tweet_o = []
rot_o = []

count_H = 0
count_B = 0
for index, row in df.iterrows():
    rot = row['Rotulacoes']
    if not 'L' in rot or not 'l' in rot:
        if 'b' in rot or 'B' in rot and count_B < max_balanceado:
            count_B += 1
            id_o.append(row['ID'])
            tweet_o.append(row['Tweets'])
            rot_o.append('B')
        elif  'h' in rot or 'H' in rot and count_H < max_balanceado:
            count_H += 1
            id_o.append(row['ID'])
            tweet_o.append(row['Tweets'])
            rot_o.append('H')

#for index, row in df.iterrows():
#    rot = row['Rotulacoes']
#    if not 'L' in rot or not 'l' in rot:
#        if 'b' in rot or 'B' in rot:
#            id_o.append(row['ID'])
#            tweet_o.append(row['Tweets'])
#            rot_o.append('B')
#        elif  'h' in rot or 'H' in rot:
#            id_o.append(row['ID'])
#            tweet_o.append(row['Tweets'])
#            rot_o.append('H')
        
print("\nQuantidade balanceada: " + str(max_balanceado))       
dict_o = {'ID': id_o, 'Tweets': tweet_o, 'Rotulacoes': rot_o}
df_o = pd.DataFrame(data=dict_o)
            
writer = pd.ExcelWriter('massa_2570_balanceada.xlsx', engine='xlsxwriter')
df_o.to_excel(writer, sheet_name="Sheet1", index=False)
writer.save()