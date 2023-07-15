import requests 
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)
soup = bs(r.content,'lxml')

prices = soup.find_all('h4', class_ = "pull-right price")
price_list = []
for i in prices:
    price = i.text
    price_list.append(price)
    
title = soup.find_all('a', class_ = 'title')
pr_name = []
for i in title:
    product = i.text
    pr_name.append(product)
    
desc = soup.find_all('p', class_ = 'description')
pr_desc = []
for i in desc:
    descs= i.text
    pr_desc.append(descs)
    
Products = {"Product Name" : pr_name,
           "Price" : price_list,
           "Product Details" : pr_desc}

df = pd.DataFrame(Products)
df
df.to_csv("Product.csv")
