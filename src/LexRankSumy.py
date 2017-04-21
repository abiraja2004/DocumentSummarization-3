from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
summarizer = LexRankSummarizer()
from Calling_Stanford_NLP import CallingStanfordNLP

for i in range(1,3001):
    parser = PlaintextParser.from_file('.\\texts\\'+str(i), Tokenizer("english"))
    taggedtext = open('.\\taggedtexts\\'+str(i),'w')
    summary = summarizer(parser.document,5)
    for sentence in summary:
        cs = CallingStanfordNLP(str(sentence),taggedtext)