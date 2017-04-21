# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:20:58 2017

@author: Akshay
"""
from pycorenlp import StanfordCoreNLP
from bs4 import BeautifulSoup
text = (
  'Pusheen and Smitha walked along the beach. '
  'Pusheen wanted to surf, but fell off the surfboard.'
  )

nlp = StanfordCoreNLP('http://nlp.stanford.edu:8080/parser/?query=' + text)

'''output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
'''

output = nlp.annotate(text)

output = output.encode('ascii', 'xmlcharrefreplace')
soup = BeautifulSoup(output, 'html.parser')
#print soup.prettify()
whole_text = soup.get_text()
whole_text = whole_text.split("\n")

done = 0
for index, text in enumerate(whole_text):
    if "Universal dependencies" in text:
        for i in range(index + 1, len(whole_text)):
            if "Universal dependencies, enhanced" in whole_text[i]:
                done = 1
                break
            else:
                print whole_text[i]
        if done == 1:
            break;
            