import requests
from pprint import pprint


link = 'https://api.namefake.com/'
requisicao = requests.get(link)

print(requisicao)   # vai exibir o código da resposta
#print(requisicao.json())
pprint(requisicao.json())
