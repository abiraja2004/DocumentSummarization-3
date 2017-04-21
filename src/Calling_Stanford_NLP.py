# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:20:58 2017

@author: Akshay
"""
from pycorenlp import StanfordCoreNLP
from bs4 import BeautifulSoup
#from parse import *
'''text = (
  'Pusheen and Smitha walked along the beach. '
  'Pusheen wanted to surf, but fell off the surfboard.'
  )

nlp = StanfordCoreNLP('http://nlp.stanford.edu:8080/parser/?query=' + text)

output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })

output = nlp.annotate(text)

output = output.encode('ascii', 'xmlcharrefreplace')
soup = BeautifulSoup(output, 'html.parser')
#print soup.prettify()
whole_text = soup.get_text()
whole_text = whole_text.split("\n")'''

class CallingStanfordNLP:
    def __init__(self,text,file):
        self.nlp = StanfordCoreNLP('http://nlp.stanford.edu:8080/parser/?query=' + text)
        self.output = self.nlp.annotate(text)
        self.output = self.output.encode('utf-16', 'xmlcharrefreplace')
        self.soup = BeautifulSoup(self.output, 'html.parser')
        # print soup.prettify()
        self.whole_text = self.soup.get_text()
        self.whole_text = self.whole_text.split("\n")
		self.whole_text = self.whole_text.split(".")
        self.textfinder(file)
		file.write(text)

    def textfinder(self,file):
        done = 0
		#file.write(('.').join(self.whole_text))
        '''for index, text in enumerate(self.whole_text):
            if "Universal dependencies" in text:
                for i in range(index + 1, len(self.whole_text)):
                    if "Universal dependencies, enhanced" in self.whole_text[i]:
                        done = 1
                        break
                    else:
                        try:
                            file.write(self.whole_text[i] + '\n')
                        except:
                            pass
                        #print self.whole_text[i]
                if done == 1:
                    break
'''