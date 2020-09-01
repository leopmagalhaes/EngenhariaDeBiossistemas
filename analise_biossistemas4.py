#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:33:24 2020

@author: usuario
"""


import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

book_text = open('teste.txt','r').read()
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(book_text)
palavras = word_tokenize(book_text.lower())

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
idx_palavras_importantes = nlargest(100, frequencia, frequencia.get)

#split at pov changes
book_text = book_text.replace('—From', ' * * * ')
sections = book_text.split('* * *')

#remove all dialogue
cleaned_sections = []

for section in sections:
    quotes = re.findall("“.*?”", section)
    for quote in quotes:
        section = section.replace(quote, " ")
    cleaned_sections.append(section)

#Create characters list and cooccurnce matrix
characters = ['engenharia','biossistemas','produção','sistemas','agrícola',
'agropecuária','curso','energia','área','desenvolvimento',
'automação','mercado','precisão','pode','engenheiro',
'alimentos','tecnologias','agricultura','agronegócio','animal',
'trabalho','produtos','gestão','profissional','disciplinas',
'outros','universidade','materiais','produtividade','profissionais',
'biocombustíveis','matérias','além','novo','brasil',
'ainda','equipamentos','setor','biologia','atuação',
'irrigação','tecnologia','biológicos','zootecnia','agrícolas',
'meio','usp','outras','sobre','graduação',
'robótica','processos','vegetal','desde','infraestrutura',
'formação','atuar','fazer','controle','qualidade',
'faz','federal','bastante','distribuição','novas','ambiente',
'ser','cursos','campo','armazenamento','atua','disso',
'matemática','pesquisa','estágio','anos',
'grande','então','país','física','máquinas',
'trabalhar','imagens','condições','ramo','lida',
'limpa','biomassa','sustentabilidade','incorporação','criação',
'necessidades','população','sociedade','drenagem']
characters = [character.title() for character in characters] #oops title case

#--> iterate through each and store in dictionary
sections_dictionary = {}
iterative = 0
for section in cleaned_sections:
    iterative += 1
    for char in characters:
        if char in section:
            if str(iterative) in sections_dictionary.keys():
                sections_dictionary[str(iterative)].append(char)  
            else:
                sections_dictionary[str(iterative)] = [char]  

##set base df (co-occurance matrix)
df = pd.DataFrame(columns = characters, index = characters)
df[:] = int(0)

#iterate through each POV of book and add one for each character-character relationship
#-> in this case, relationship equates to appearing in the same POV
for value in sections_dictionary.values():
    for character1 in characters:
        for character2 in characters:
            if character1 in value and character2 in value:
                df[character1][character2] += 1
                df[character2][character1] += 1
                
#add weights to edges
edge_list = [] #test networkx
for index, row in df.iterrows():
    i = 0
    for col in row:
        weight = float(col)/464
        edge_list.append((index, df.columns[i], weight))
        i += 1

#Remove edge if 0.0
updated_edge_list = [x for x in edge_list if not x[2] == 0.0]

#create duple of char, occurance in novel
node_list = []
for i in characters:
    for e in updated_edge_list:
        if i == e[0] and i == e[1]:
           node_list.append((i, e[2]*6))
for i in node_list:
    if i[1] == 0.0:
        node_list.remove(i)

#remove self references
for i in updated_edge_list:
    if i[0] == i[1]:
        updated_edge_list.remove(i)

#set canvas size
plt.subplots(figsize=(14,14))

#networkx graph time!
G = nx.Graph()
for i in sorted(node_list):
    G.add_node(i[0], size = i[1])
G.add_weighted_edges_from(updated_edge_list)

#check data of graphs
#G.nodes(data=True)
#G.edges(data = True)

#manually copy and pasted the node order using 'nx.nodes(G)'
#Couldn't determine another route to listing out the order of nodes for future work
node_order = ['engenharia','biossistemas','produção','sistemas','agrícola',
'agropecuária','curso','energia','área','desenvolvimento',
'automação','mercado','precisão','pode','engenheiro',
'alimentos','tecnologias','agricultura','agronegócio','animal',
'trabalho','produtos','gestão','profissional','disciplinas',
'outros','universidade','materiais','produtividade','profissionais',
'biocombustíveis','matérias','além','novo','brasil',
'ainda','equipamentos','setor','biologia','atuação',
'irrigação','tecnologia','biológicos','zootecnia','agrícolas',
'meio','usp','outras','sobre','graduação',
'robótica','processos','vegetal','desde','infraestrutura',
'formação','atuar','fazer','controle','qualidade',
'faz','federal','bastante','distribuição','novas','ambiente',
'ser','cursos','campo','armazenamento','atua','disso',
'matemática','pesquisa','estágio','anos',
'grande','então','país','física','máquinas',
'trabalhar','imagens','condições','ramo','lida',
'limpa','biomassa','sustentabilidade','incorporação','criação',
'necessidades','população','sociedade','drenagem']

#reorder node list
updated_node_order = []
for i in node_order:
    for x in node_list:
        if x[0] == i:
            updated_node_order.append(x)
            
#reorder edge list - this was a pain
test = nx.get_edge_attributes(G, 'weight')
updated_again_edges = []
for i in nx.edges(G):
    for x in test:
        if i[0] == x[0] and i[1] == x[1]:
            updated_again_edges.append(test[x])
            
#drawing custimization
node_scalar = 800
edge_scalar = 100
sizes = [x[1]*node_scalar for x in updated_node_order]
widths = [x*edge_scalar for x in updated_again_edges]

#draw the graph
pos = nx.spring_layout(G, k=0.42, iterations=17)

nx.draw(G, pos, with_labels=True, font_size = 12, font_weight = 'bold', 
        node_size = sizes, width = widths)

#plt.axis('off')
#plt.savefig("imgs/sl_network2.png") # save as png