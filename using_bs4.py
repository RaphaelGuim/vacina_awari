#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:55:08 2021

@author: pauloeduardosampaio
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

urls = ["https://www.vivareal.com.br/venda/sp/sao-paulo/zona-sul/brooklin/apartamento_residencial/",
        "https://www.vivareal.com.br/venda/sp/sao-paulo/zona-sul/brooklin/apartamento_residencial/?pagina=2"]


propriedades = []

for url in urls:
    c=requests.get(url).content
    soup=BeautifulSoup(c)
    
    cards = soup.findAll("article", {"class": "js-property-card"})   
    for card in cards:
        propriedade = {}
        propriedade["endereco"] = card.find("span", {"class": "property-card__address"}).text
        propriedade["area"] = card.find("li", {"class": "property-card__detail-area"}).text
        propriedade["quartos"] = card.find("li", {"class": "property-card__detail-room"}).text
        propriedade["banheiros"] = card.find("li", {"class": "property-card__detail-bathroom"}).text
        propriedade["vagas"] = card.find("li", {"class": "property-card__detail-garage"}).text
        propriedade["preco"] = card.find("div", {"class": "property-card__price"}).text
        try:
            propriedade["outros"] = card.find("ul", {"class": "property-card__amenities"}).text
        except:
            propriedade["outros"] = None
        try:
            propriedade["condominio"] = card.find("div", {"class": "property-card__price-details--condo"}).text
        except:
            propriedade["condominio"] = None
        propriedades.append(propriedade)

