from __future__ import division
from path import path
import sys
import re
from collections import defaultdict
from math import log
from StringIO import StringIO
from depParse import readParses

# this function takes the name of the directory to process
# and returns a set of statistics which are useful for computing tfidf values
def countStats(textDir):
    termCounts = defaultdict(lambda: defaultdict(int))

    for fi in textDir.glob("*.orig"):
        ff = file(fi)
        for parse in readParses(ff):
            leaves = parse.leaves()
            for (word, pos) in leaves:
                termCounts[fi][word] += 1

    return termCounts

# this function takes the word, the name of the document it appears in, 
# and the termcounts object returned by countstats
# and returns the tf*idf value for that word in that document
def tfidf(word, doc, termCounts):
    tf = termCounts[doc][word]
    print tf
    dcount = sum([1 for fi in termCounts if word in termCounts[fi]])
    print dcount
    idf = len(termCounts) / (1 + dcount)
    lidf = log(idf)

    return tf * lidf

if __name__ == "__main__":
    textDir = path("E:\\SP 17\\5525 SLP\\Project\\Sentence Compression\\data")

    termCounts = countStats(textDir)
    print "tf*idf for the", tfidf("the", "E:\\SP 17\\5525 SLP\\Project\\Sentence Compression\\data\\A30.7.orig", termCounts)
    print "tf*idf for kinnock", tfidf("Kinnock", "E:\\SP 17\\5525 SLP\\Project\\Sentence Compression\\data\\A30.7.orig", termCounts)
    #print termCounts
