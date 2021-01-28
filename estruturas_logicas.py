import pandas as pd
data= pd.read_csv('data.csv') # lê os dados do arquivo data.csv e armazena na variável data
#print(data)
'''
linha=data.loc[0]

if linha.all() == 'Sim': #se em algum lugar da linha conter a palavra Sim entao true
    print('Tem peptídeo sinal e a localização é {}'.format(linha['Localizacao_subcelular']))
elif linha.all() == 'Nao': #se em algum lugar da linha conter a palavra Nao entao true
    print('Não tem peptídeo sinal e a localização é {}'.format(linha['Localizacao_subcelular']))
else:
    print('Não tem informações sobre peptídeo sinal')

'''

for local_sub in data['Localizacao_subcelular']:
    if local_sub == 'citplasmatica':
        print('Essa proteina não nos interessa') # pois se a proteina esta nessa parte ela não ajudará na vacina
    elif local_sub == 'transmembranica':
        print(data['sequencia'])
    else:
        print('Ptroteina sem informação')