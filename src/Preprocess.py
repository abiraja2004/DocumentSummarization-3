from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

class Preprocess:
    def __init__(self):
        self.englishStopWords = set(stopwords.words('english'))
        self.englishStopWords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '-'])
        self.analyzer = CountVectorizer(lowercase=True, stop_words=self.englishStopWords).build_analyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.lemmatizedVectorizer = CountVectorizer(analyzer=self.lemmatizedWords)

    def lemmatizedWords(self, doc):
        return (self.lemmatizer.lemmatize(word) for word in self.analyzer(doc))

    def getFeatureVector(self, doc):
        originalSentences = sent_tokenize(doc)
        return self.lemmatizedVectorizer.fit_transform(originalSentences)

if __name__ == '__main__':
    doc = """The top three leagues in Europe are currently allowed to enter four teams into the Champions League. Michel Platini, the UEFA president, had proposed taking one place from the top three leagues and allocating it to that nation's cup winners. This proposal was rejected in a vote at a UEFA Strategy Council meeting.[49] In the same meeting, however, it was agreed that the third-placed team in the top three leagues would receive automatic qualification for the group stage, rather than entry into the third qualifying round, while the fourth-placed team would enter the play-off round for non-champions, guaranteeing an opponent from one of the top 15 leagues in Europe. This was part of Platini's plan to increase the number of teams qualifying directly into the group stage, while simultaneously increasing the number of teams from lower-ranked nations in the group stage. For this stage, the winning team from one group plays against the runners-up from another group, and teams from the same association may not be drawn against each other. From the quarter-finals onwards, the draw is entirely random, without association protection. The tournament uses the away goals rule: if the aggregate score of the two games is tied, then the team who scored more goals at their opponent's stadium advances."""
    preprocess = Preprocess()
    cvf = preprocess.getFeatureVector(doc)
    # print cvf
    # print preprocess.lemmatizedVectorizer.vocabulary_
    # print preprocess.englishStopWords



