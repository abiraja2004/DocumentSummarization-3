from __future__ import division
import sys
import re
from collections import defaultdict

class DepParse:
    #a class for stanford dependencies
    #represents things as a dictionary headOf[(word,pos)] = ((word, pos), rel)
    #where pos is the integer position (1-indexed) of the word in the string
    #root is ("ROOT", 0)

    def __init__(self, parse):
        self.headOf = {}
        for line in parse:
            match = re.match("([^(]+)\(([^ ]+), ([^)]+)\)", line)
            (rel, arg1, arg2) = match.groups()
            (arg1, pos1) = arg1.rsplit("-", 1)
            (arg2, pos2) = arg2.rsplit("-", 1)

            pos1 = int(pos1)
            pos2 = int(pos2)

            self.headOf[(arg2, pos2)] = ((arg1, pos1), rel)

    def leaves(self):
        return self.headOf.keys()

    def dist(self):
        return 5
    
    def distToRoot(self, node):
        #This function can return the distance of "node" to the root
        #print "***"
        #print self.headOf
        #print(node)
        depth = 0
        (word, pos) = node.rsplit("-",1)
        pos = int(pos)
        #print node
        while word != "ROOT":
            for n in self.headOf:
                (w1, w2) = n
                if w1 == word and w2 == pos:
                    #print self.headOf[n]
                    ((word, pos), w3) = self.headOf[n]
                    depth += 1
        return depth
        
    def get_head(self, node):
        (word, pos) = node.rsplit("-",1)
        pos = int(pos)
        for n in self.headOf:
            (w1, w2) = n
            if w1 == word and w2 == pos:
                #print self.headOf[n]
                ((word, pos), w3) = self.headOf[n]
                break
        return word + "-" + str(pos)
    
    def get_children(self, node):
        #print self.headOf
        children = []
        (word, pos) = node.rsplit("-",1)
        pos = int(pos)
        for n in self.headOf:
            #print self.headOf[n]
            ((head, position), dp_tag) = self.headOf[n]
            if head==word and pos==position:
                (child, post) = n
                #print child, post, dp_tag
                children.append([n, dp_tag])
        
        return children
    
    def sentence(self):
        #returns the sentence as a string
        words = self.leaves()
        words.sort(key=lambda xx: xx[1])

        return " ".join([word for (word, pos) in words])

def readParses(ff):
    #reads DepParse objects from the file stream ff
    res = []
    for line in ff:
        if not line.strip():
            yield DepParse(res)
            res = []
        else:
            res.append(line.strip())
    if res:
        yield DepParse(res)

if __name__ == "__main__":
    '''#for fi in sys.argv[1:]:
    fi="E:\\SP 17\\5525 SLP\\Project\\Sentence Compression\\data\\A1G.11.orig"
    for parse in readParses(file(fi)):
        #print parse.sentence()
        #print parse.distToRoot("the-20")
        #print parse.leaves()
        print parse.get_children("members-22")
        break
    '''