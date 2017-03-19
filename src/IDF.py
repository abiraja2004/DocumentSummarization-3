from __future__ import division
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from math import log

class IDF:
    def __init__(self, path):
        self.IDFDict = {}
        self.totalNoOfDocs = 0
        self.path = path
        self.wordTokenizer = RegexpTokenizer(r'\w+')
        self.englishStopWords = set(stopwords.words('english'))
        self.englishStopWords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '-'])
        self.wordNetLemmatizer = WordNetLemmatizer()
        self.getIDFDict()

    def lemmatizer(self, word):
        return self.wordNetLemmatizer.lemmatize(word)

    def tokenizeAndLemmatize(self, word):
        return self.lemmatizer(word.lower())

    def tokenizedWords(self, doc):
        return set(filter(lambda w : w not in self.englishStopWords, map(self.tokenizeAndLemmatize, self.wordTokenizer.tokenize(doc))))

    def getIDFDict(self):
        # path = "C:\\Users\\aniru\\Downloads\\data"
        for fileName in os.listdir(self.path):
            for lines in open(self.path + "/" + fileName):
                setOfTokenizedWords = self.tokenizedWords(lines)
                self.totalNoOfDocs += 1
                for word in setOfTokenizedWords:
                    if word not in self.IDFDict:
                        self.IDFDict[word] = 1
                    else:
                        self.IDFDict[word] += 1

        for word, noOfDocs in self.IDFDict.iteritems():
            self.IDFDict[word] = log(float(self.totalNoOfDocs) / noOfDocs) ** 2

        print self.totalNoOfDocs
        # print IDFDict

    def getIDFOfWord(self, word):
        return self.IDFDict[word]

if __name__ == '__main__':
    idf = IDF()
