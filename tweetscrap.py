# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:32:18 2017

@author: FAUSTINE
"""
import re
from bs4 import BeautifulSoup as bs
import urllib.request as ureq

myurl = "https://twitter.com/UKenyatta"
theurl= ureq.urlopen(myurl)
supu= bs(theurl,"html.parser")
print(supu.title.text)
#print(supu.find_all('a'))
"""
for links in supu.find_all('a'):
    print(links.get('href'))
    print(links.text)
    """
print(supu.find('div',{"class":"ProfileHeaderCard"}).find('p').text) 
i = 1   
for tweetz in supu.find_all('div',{"class":"content"}):
    print(tweetz.find('p').text)
    i = i+1