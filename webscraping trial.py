# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:24:25 2019

@author: vrlpa
"""

from bs4 import BeautifulSoup
import urllib2

url = "https://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)



print title
>> 'title'? Python For Beginners

print soup.title.string
>> ? Python For Beginners

print soup.p
 



print soup.a
Python For Beginners