from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer 
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys


LANGUAGE = "english"
SENTENCES_COUNT = int(sys.argv[2])
text_file = sys.argv[1]


if __name__ == "__main__":
    
    parser = PlaintextParser.from_file(text_file, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = EdmundsonSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

