#from urllib.request import urlopen
from os import path
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

dirname = path.dirname(__file__)

product_list_file = 'release-note.htm'
products = open(path.join(dirname,product_list_file), 'r').read()
release_file = '2017.htm'
releases = open(path.join(dirname,release_file), 'r').read()

# urlopenで取得する場合はこちら
#f = urlopen('https://aws.amazon.com/about-aws/whats-new/2017/')
words = ""
labels = []
counts = []
product_dics = {}
product_noupdate = []
soup_products = BeautifulSoup(products,"html.parser")
soup_releases = BeautifulSoup(releases,"html.parser")
for title in soup_releases.find_all('h3'):
    words += ' ' + title.text

for product in soup_products.find_all('a', {'class': 'link-list-item'}):
    product = product.text.rstrip(' ')
    product_dics[product] = words.count(product)

words_dics_sort = sorted(product_dics.items(), key=lambda x: x[1], reverse=True)
for k, v in words_dics_sort:
    if v > 1:
        labels.append(k)
        counts.append(v)
#    else:
#        product_noupdate.append(k)

x = np.array(counts)
plt.figure(figsize=(15,15))
plt.pie(x, labels=labels)
plt.savefig('awsrelease-piechart.png')
#print(product_noupdate)
