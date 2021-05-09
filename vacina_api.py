#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:18:33 2021

@author: pauloeduardosampaio
"""

import requests
import pandas as pd

url = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"

user = "imunizacao_public"
password = "qlto5t&7r_@+#Tlstigi"

response = requests.get(url)
print(response.content)

response = requests.get(url, auth=(user, password))
print(response.content)
response = response.json()

response.keys()
print(response.get("took"))
print(response.get("timed_out"))
print(response.get("_shards"))
hits = response.get("hits")
print(hits.get("total"))
results = hits.get("hits")

url = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
request_body = {"size": 10000}
response = requests.post(url, auth=(user, password), json=request_body)
response = response.json()
scroll_id = response.get("_scroll_id")

request_body = {"scroll_id": scroll_id, "scroll": "1m"}
url = "https://imunizacao-es.saude.gov.br/_search/scroll"
response_2 = requests.post(url, auth=(user, password), json=request_body)
reponse_2 = response_2.json()

####
# First request
results = []
url = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
request_body = {"size": 10000}
user = "imunizacao_public"
password = "qlto5t&7r_@+#Tlstigi"
response = requests.post(url, auth=(user, password), json=request_body)
response = response.json()


hits = response.get("hits").get("hits")
results = results + hits
scroll_id = response.get("_scroll_id")
for i in range(50):
    request_body = {"scroll_id": scroll_id, "scroll": "1m"}
    url = "https://imunizacao-es.saude.gov.br/_search/scroll"
    response = requests.post(url, auth=(user, password), json=request_body)
    response = response.json()
    scroll_id = response.get("_scroll_id")
    hits = response.get("hits").get("hits")
    results = results + hits
    print(f"hits len: {len(hits)}, total results: {len(results)}")
