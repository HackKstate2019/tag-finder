from lxml import html
import re
import requests
import nltk
import matplotlib
import matplotlib.pyplot as plt
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from urllib import request
from nltk.corpus import stopwords
# Corpus Libraries Needed run once then comment out
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('vader_lexicon')
nltk.download('wordnet')
