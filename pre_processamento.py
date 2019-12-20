# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:52:33 2018

@author: Amanda Mayara Menino   | GitHub: https://github.com/AmandaMMAlves
@author: Carla A. Madureira     | GitHub: https://github.com/carlalmadureira
"""
import nltk
import re
import unicodedata
import string
from nltk.corpus import stopwords

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\S_]+)', # @-mentions
    r"(?:\#+[\S_]+[\S\'_\-]*[\S_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    #r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r'(?:[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)',
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\S_]+)' # other words
    r'(?:\S)', # anything else
    r'[A-Z]\S+\s*']
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

punctuation = list(string.punctuation)
wordsToBeIgnored = ['rt', 'via', '…', 'de','um', 'porque', 'coisa','mesmo', 'mesma', 'é', 'para', 'sobre', 'a', 'o', 'que']
    
stop = stopwords.words('portuguese') + punctuation + wordsToBeIgnored


def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s):
    tokens = tokenize(s)
    tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return " ".join(tokens)

def remove_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def PreprocessamentoSemStopWords(instancia):
    #remove links dos tweets
    #remove stopwords
    instancia = re.sub(r"http\S+", "", instancia).lower().replace(',','').replace('.','').replace(';','').replace('-','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def Stemming(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    # stemmer = SnowballStemmer('portuguese')
    palavras=[]
    for w in instancia.split():
        palavras.append(stemmer.stem(w))
    return (" ".join(palavras)) 

def normal_filter(s, stopwords):
    filtrado = []
    for w in s.split():
        if w not in stopwords and not w.startswith('@') and not w.startswith('https://') and not w.startswith('http://') and not w.endswith('…'):
            if not w.startswith('(') and not w.endswith(')') and not w.startswith('/') and not len(w) < 4 and "." not in w and not w.startswith('!'):
                if not w.startswith(';') and not w.startswith(':') and not w.startswith('|') and not w.endswith('.') and not w.endswith(',') and not w.startswith('\\'):
                    if "kkk" not in w and "ksjekeksk" not in w and "ahsfx" not in w and "???" not in w and "aaa" not in w:
                        filtrado.append(w)
    return " ".join(filtrado)

def Preprocessamento(instancia):
    #remove links, pontos, virgulas,ponto e virgulas dos tweets
    #coloca tudo em minusculo
    instancia = re.sub(r"http\S+", "", instancia).lower().replace(',','').replace('.','').replace(';','').replace('-','').replace(':','')
    return (instancia)  

#--------------------------------------------------------------------------------------------------------

def aplicandoPreProcessamento(textos):
#     textos = textos.tolist()
     txts = []
     for txt in textos:
         sem_acentos = remove_accents(txt)
         pre_process = preprocess(sem_acentos)
         txts.append(normal_filter(pre_process, stop))
     return txts

#def aplicandoPreProcessamento(textos):
#    textos = textos.tolist()
#    txts = []
#    for txt in textos:
#        txts.append(PreprocessamentoSemStopWords(txt))
#    return txts

def aplicandoStemming(textos):
    txts_stemming = []
    for txt in textos:
        txts_stemming.append(Stemming(txt))
    return txts_stemming


#---------------------------------------------------------------------------------------------------------



def tratamentoDados(textos, stemming=True):
    textos = aplicandoPreProcessamento(textos)
    if(stemming == True):
        textos = aplicandoStemming(textos)
    return textos