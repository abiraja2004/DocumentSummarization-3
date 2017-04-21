from pythonrouge.pythonrouge import Pythonrouge
from nltk import sent_tokenize
from itertools import izip
from collections import Counter

def sentTokenize(paragraph):
    return [sent_tokenize(paragraph)]

# initialize setting of ROUGE, eval ROUGE-1, 2, SU4, L
rouge = Pythonrouge(n_gram=2, ROUGE_SU4=True, ROUGE_L=True, stopwords=True)

path = "../Summaries"
modelGeneratedSummariesPath = path + "/modelGenerated/1.txt"
goldReferenceSummariesPath = path + "/goldReference/1.txt"
avgRougeScoreCounter = Counter({})

with open(modelGeneratedSummariesPath) as f:
    modelLines = f.readlines()
with open(goldReferenceSummariesPath) as f:
    goldLines = f.readlines()

noOfDocs = 0

for (modelDocSummary, goldDocSummary) in izip(modelLines, goldLines):
    if(modelDocSummary.__len__() == 1):
        continue
    modelSummaryInputToRouge = [[modelDocSummary]]
    goldSummaryInputToRouge = [[[goldDocSummary]]]
    setting_file = rouge.setting(files=False, summary=modelSummaryInputToRouge, reference=goldSummaryInputToRouge)
    rougeScore = rouge.eval_rouge(setting_file, recall_only=True)
    avgRougeScoreCounter += Counter(rougeScore)
    noOfDocs += 1

avgRougeScore = dict(map(lambda (k,v) : (k, v / float(noOfDocs)), avgRougeScoreCounter.items()))
print avgRougeScore