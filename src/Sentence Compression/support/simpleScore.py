from __future__ import division
import sys
import re
import os

def score(ourWords, goldWords):
    #return match, actual, proposed word counts for input lists of words
    goldSet = set(goldWords)

    match = 0
    for wi in ourWords:
        if wi in goldSet:
            match += 1

    return match, len(goldWords), len(ourWords)

if __name__ == "__main__":
    
    dire = "Results\\"
    avg_prec = 0
    avg_rec = 0
    avg_fsc = 0
    count = 0
    evaluate = 1
    for index, fil in enumerate(os.listdir(dire)) :
        if "check_" + str(evaluate) not in fil:
            continue
        print "Scoring", fil
        count += 1
        allWords = 0
        allMatch = 0
        allGold = 0
        allProp = 0
    
        fh = open(dire + fil)
        try:
            while True:
                line = fh.next()
                if not line.strip():
                    line = fh.next()
    
                orig = line.strip().split()
                if orig.pop(0) != "Orig:":
                    raise Exception("Expected Orig:, got %s" % line)
    
                line = fh.next()
                human = line.strip().split()
                if human.pop(0) != "Human:":
                    raise Exception("Expected Human:, got %s" % line)
    
                line = fh.next()
                ours = line.strip().split()
                if ours.pop(0) != "Ours:":
                    raise Exception("Expected Ours:, got %s" % line)
    
                (match, gold, prop) = score(ours, human)
                allWords += len(orig)
                allMatch += match
                allGold += gold
                allProp += prop
        except StopIteration:
            pass
    
        prec = allMatch / allProp
        rec = allMatch / allGold
        fscore = (2 * prec * rec) / (prec + rec)
    
        print allWords, "compressed by humans to", allGold, (1 - allGold / allWords)
        print allWords, "compressed by us to", allProp, (1 - allProp / allWords)
    
        print "Matched", allMatch, "of", allGold, "human words"
        print "Printed", allProp, "words"
        print "Prec", prec, "rec", rec, "F", fscore
        avg_prec += prec
        avg_rec += rec
        avg_fsc += fscore

    print "\n\n\nAvg Prec", avg_prec/count, "Avg rec", avg_rec/count, "Avg F", avg_fsc/count