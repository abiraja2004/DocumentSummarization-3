import networkx as nx
from scipy import sparse
import numpy as np
import matplotlib.pyplot as plt
from IDF import IDF
from Preprocess import Preprocess
import time

class LexRank:
    def __init__(self,cv,totalidf,words,threshold=0):
        self.cv = cv
        self.idf = self.create(totalidf,words)
        self.graph = nx.Graph()
        self.threshold = threshold
        self.createGraph
        self.populateGraph()
        self.pr = nx.pagerank(self.graph)

    def createGraph(self):
        self.graph.add_nodes_from(range(self.cv.shape[0]))


    def populateGraph(self):
        h = self.cv.shape[0]
        for i in range(h):
            for j in range(i+1,h):
                r1 = self.cv.getrow(i)
                r2 = self.cv.getrow(j)
                a = r1.multiply(r2)
                b = r1.multiply(r1)
                c = r2.multiply(r2)
                num = a * self.idf
                den = (np.sqrt(b * self.idf) * np.sqrt(c * self.idf))
                if num[0]/float(den[0]) > self.threshold:
                    self.graph.add_edge(i,j,{'weight' : num[0]/float(den[0])})

    def create(self,totalidf,words):
        idf = np.zeros(len(words))
        for i in range(len(words)):
            idf[i] = totalidf[words[i]]
        return idf





if __name__ == "__main__":
    #cv = sparse.random(5,5,0.5).tocsr()
    #idf = sparse.csr_matrix(np.array([1]*5))
    #lr = LexRank(cv,idf.T)
    #nx.draw(lr.graph)
    #plt.show()
    #print lr.pr

    idf = IDF("/home/venkata/DocumentSummarization/data")
    with open("/home/venkata/DocumentSummarization/src/textfile") as f:
        textfile = f.readlines()

    start = time.time()
    for line in textfile:
        preprocess = Preprocess(line)
        lr = LexRank(preprocess.featurevector,idf.IDFDict,preprocess.indextoword,0.3)
        print lr.pr
    print time.time() - start
