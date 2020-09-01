#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:00:52 2020

@author: usuario
"""


from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from unidecode import unidecode

text = open('teste.txt','r').read()
#text = unidecode(texto)
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(text)
palavras = word_tokenize(text.lower())

from nltk.corpus import stopwords
from string import punctuation
stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

#from collections import Counter
#palavras = text2.replace('\n',' ').replace('\t','').split(' ')
#contador = Counter(palavras)

from nltk.probability import FreqDist
from heapq import nlargest
frequencia = FreqDist(palavras_sem_stopwords)
idx_palavras_importantes = nlargest(20, frequencia, frequencia.get)

#for i in contador.items():
 #   print i
from collections import defaultdict
sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

from heapq import nlargest
idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)


nuvem = WordCloud(max_font_size=100,width = 1520, height = 535).generate(text)
plt.figure(figsize=(16,9))
plt.imshow(nuvem)
plt.axis("off")
plt.show()

print(idx_palavras_importantes)
print(idx_sentencas_importantes)