#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:56:41 2020

@author: usuario
"""

# Program to measure the similarity between  
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
X = "A Engenharia de Biossistemas é um novo ramo da engenharia no Brasil que lida com a produção agropecuária, de certos materiais, alimentos, energia limpa e biomassa, buscando sustentabilidade através da incorporação e criação de novas tecnologias, isto é, garantindo um volume de produção que atenda às necessidades da população, sem prejudicar o ambiente e a sociedade. Pode-se dizer, com certa ressalva, que a Engenharia de Biossistemas é uma evolução da Engenharia Agrícola, na medida em que aborda e complementa os conhecimentos desta. Ao incorporar aos sistemas clássicos de irrigação e drenagem, construções rurais, mecanização agrícola, entre outros, avanços tecnológicos como tecnologia da informação, robótica, computação gráfica, mecatrônica, biossensores, engenharia de materiais, GPS etc.a engenharia de biossistemas dá um novo significado ao termo suporte à produção agropecuária. Embora seja nova no Brasil, a Engenharia de Biossistemas já é um curso tradicional em países como Austrália, Estados Unidos e Irlanda. Sua concepção começou a ser estabelecida na década de 1960 em uma reunião da ASABE (American Society of Agricultural and Biological Engineers). Muitos pesquisadores dessa sociedade pensavam que a Engenharia Agrícola não poderia apenas se preocupar com a aplicação de sistemas e insumos na agricultura, como deveria entender e modelar sistemas biológicos. Dessa ideia que surgiu a Engenharia de Biossistemas, que se consolidou a partir da década de 1990 nos EUA com a inclusão ou troca de nome de muitos Departamentos e cursos que passaram de Engenharia Agrícola para: Engenharia Agrícola e Biológica ou de Biossistemas."
#Y = "O Curso de Bacharelado em Engenharia de Biossistemas é voltado para o estudo de sistemas ambientais que favoreçam a produção sustentada de alimentos, fibras e energia, mediante o uso de tecnologias inovadoras. A Engenharia de Biossistemas surge como uma modernização e ampliação dos estudos em Engenharia englobando os aspectos biológicos e as estruturas relacionadas ao beneficiamento, processamento ou tratamento dos produtos agropecuários. Portanto, nesta grande área estão incluídos os estudos de grãos, fibras, outros produtos de origem biológica, microorganismos responsáveis por fermentações e tratamentos de efluentes. Para que este sistema biológico seja estudado é necessário um suporte em outras áreas da Engenharia como energia, estruturas, eletricidade, automação e agricultura de precisão. O curso destina-se a jovens e adultos que tenham concluído o ensino médio, e que desejam, enquanto qualificados no campo das Ciências Exatas e da Natureza, atuar como um profissional que possa auxiliar tecnicamente os produtores rurais. O egresso deste curso tem um campo de atuação relacionado à pesquisa e desenvolvimento dos processos de especialização do sistema produtivo da agricultura e agroindústria de origem familiar além do agronegócio, determinados não somente pelo potencial de uma região, mas, em grande parte, pela agregação de tecnologia na produção."
#Y = "Desenvolver tecnologia para produção eficiente de alimentos e energia para um mundo ameaçado por mudanças climáticas. Este é o curso de Engenharia de Biossistemas do Câmpus de Tupã. Concebido para atender a um mercado promissor que demanda profissionais com formação moderna, que agreguem competências das áreas de produção vegetal e animal, instrumentação, tecnologia de informação, automação e meio ambiente. Cada vez mais os sistemas de produção vegetal e animal (biossistemas) têm adotado novas tecnologias de controle da produção, envolvendo automação e robotização para reduzirem perdas produtivas e aumentarem a produtividade, atendendo a uma demanda global crescente por alimentos e energias renováveis. A avicultura, por exemplo, é uma das cadeias produtivas que mais investe em inovação tecnológica, na qual a automação dos processos já está presente. O Brasil é o segundo maior produtor e o maior exportador de carne de frango do mundo, mostrando o enorme potencial de nosso país em inovação tecnológica aplicada ao campo. Outras cadeias produtivas têm potencial para melhor desempenho, desde que disponham de profissionais que compreendam os biossistemas e atuem no controle e automação dos processos produtivos. O engenheiro de biossistemas é o profissional que atende a essa demanda. A importância da área pode ser quantificada pela participação do agronegócio no PIB brasileiro. Em 2011, o agronegócio correspondeu a 22,74% do PIB nacional e no comparativo de dois anos cresceu 13,51%. O salário inicial de R$ 6.102,00 reflete a necessidade do Brasil pela formação de engenheiros de biossistemas capazes de promover o desenvolvimento produtivo e econômico do país, atuando em empresas dos segmentos de energias eólica e solar, bioenergia, implementos agrícolas, equipamentos para produção animal, software, controle e automação, geoprocessamento, pesquisa científica e consultoria."
Y = "A Engenharia de Biossistemas integra o uso eficiente e sustentável de novas tecnologias à produção agropecuária, de energia, de fibras e alimentos. Para tanto, o curso de graduação em engenharia de biossistemas reúne em sua matriz curricular conhecimentos nas áreas de energias renováveis, agropecuária digital, economia ecológica, biotecnologia e produção de alimentos e fibras. O engenheiro egresso poderá atuar em diversos setores da indústria e produção de conhecimento sendo capaz de entender, otimizar e modelar sistemas biológicos diversos, considerando os impactos futuros de suas ações."
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('portuguese')  
l1 =[];l2 =[] 
  
# remove stop words from the string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine)