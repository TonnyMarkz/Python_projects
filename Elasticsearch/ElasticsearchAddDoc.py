# -*- coding: utf-8 -*- 

#Importo biblioteca
from elasticsearch import Elasticsearch
from datetime import datetime

#crio a variavel
es = Elasticsearch(
    ['localhost'],
    port=9200,
)

#criando uma variavel com os dados do novo documento
doc = {
    'nome': 'Tonny Markz',
    'idade': 34,
    'email': 'tonnymarkz@gmail.com',
    'Skills': ['Python', 'Elasticsearch', 'Security'],
    'timestamp': datetime.now(),
}

res = es.index(index='python-elasticsearch', id=1, body=doc)
print("Status inserção: ", res['result'])

res = es.get(index='python-elasticsearch', id=1)
print('\n')
print(res['_source'])