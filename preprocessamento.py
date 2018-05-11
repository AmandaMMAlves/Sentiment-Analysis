# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:48:07 2018

@author: Amanda Mayara Menino   | GitHub: https://github.com/AmandaMMAlves
@author: Carla A. Madureira     | GitHub: https://github.com/carlalmadureira

"""

import nltk
from nltk.corpus import stopwords

"""
"""

#Aqui serão listadas outras palavras que podem complementar o recurso automatico do NLTK:
stop = ['rt', 'a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

startswith = ['@', 'https://', 'http://', "(?:\#+[\S_]+[\S\'_\-]*[\S_]+)", "(?:(?:\d+,?)+(?:\.?\d+)?)"]
endswith = ['…']

#Recurso automatico do NLTK

stopwordsnltk = nltk.corpus.stopwords('portuguese')

#Definir uma funcao que mantenha so a raiz das palavras e retire stopwords ao mesmo tempo:

def stemmerestopwords(texto, lowercase=True):
    stemmer = nltk.stem.RSLPStemmer()
    frases = []
    for (palavras,emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop and not stopwordsnltk and not startswith and not endswith]
        frases.append((comstemming, emocao))
    return frases

frasesstemstop = stemmerestopwords(entrada)

#Funcao que faz a busca de todas as palavras que temos na base de dados
def buscapalavras(frases):
    todaspalavras = []
    for(palavras,emocao) in frases:
        todaspalavras.extend(palavras)
    return palavras

#Definir uam funcao que busque a frequencia relativa das palavras

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequencia = buscafrequencia(palavras)
#Escolher o numero de palavras mais frequente
print(frequencia.most_common(50))

#Funcao que buscara palavras unicas  - evitara frequencia  de palavras repetidas
def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicas = buscapalavrasunicas(frequencia)

#Funcao que recebe cada frase e retorna se tem cada uma das principais palvras e quais nao tem
def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

#Funcao apply features vai pegar cada uma dessas duas variaveis extratorpalavras e 
#frasestemstop e jogar tudo para a variavel basecompleta
basecompleta = nltk.classify.apply_features(extratorpalavras, frasesstemstop)



        






        




