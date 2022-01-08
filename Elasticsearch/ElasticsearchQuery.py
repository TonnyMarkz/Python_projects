# -*- coding: utf-8 -*- 

#Importo biblioteca
from elasticsearch import Elasticsearch
from datetime import datetime

#crio a variavel
es = Elasticsearch(
    ['localhost'],
    port=9200,
)

search = input('Digite o nome da pessoa: ')
res = es.search(index='python-elasticsearch', body={'query': {'match': {'nome': ""+search+""}} })
print('\nA busca retornou: %d hits' % res['hits'])