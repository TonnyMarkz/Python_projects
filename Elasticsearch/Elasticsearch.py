# -*- coding: utf-8 -*- 

#Importo biblioteca
from elasticsearch import Elasticsearch

#crio a variavel
es = Elasticsearch(
    ['localhost'],
    port=9200,
)
#Imprimo na tela a informação
print(es.info())