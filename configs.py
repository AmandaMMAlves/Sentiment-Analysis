# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:02:37 2018

@author: Amanda Mayara Menino   | GitHub: https://github.com/AmandaMMAlves
@author: Carla A. Madureira     | GitHub: https://github.com/carlalmadureira
"""

import pandas as pd
import numpy as np
import pre_processamento
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold

cv = KFold(n_splits=10, random_state=None, shuffle=True)

def extracaoDados(filename):
    dataset = pd.read_excel(filename, dtype={'ID':str, 'Tweets':str, 'Rotulacoes': str}, index_col=None)
    tweets = dataset['Tweets'].values
    classes = dataset['Rotulacoes'].values
    
    return classes,tweets

def extracaoDadosCSV(filename):
    dataResult = pd.read_csv(filename, sep=',')
    
    tweets = []
    classes = []
    
    for index, row in dataResult.iterrows():
        if row['Key'] == 'pos' and row['Classify'] == 'P':
            tweets.append(row['TXT'])
            classes.append('P')
        elif row['Key'] == 'neg' and row['Classify'] == 'N':
            tweets.append(row['TXT'])
            classes.append('N')
    
    return np.array(classes),np.array(tweets)

def criacaoBagOfWords(textos, bigrama=False):
    if bigrama == True:
        vectorizer = CountVectorizer(ngram_range=(1,2))
    else:
        vectorizer = CountVectorizer(analyzer="word") 
    frequencia = vectorizer.fit_transform(textos) 
    return frequencia 

def instanciaCountVectorizer(textos, bigrama=False):
    
    frequencia = vectorizer.fit_transform(textos) 
    return frequencia     
    


def criacaoTreinamentoModelo(freq, classes, classificador):
    if classificador == "MBayes":
        modelo = MultinomialNB()
    elif classificador == "KNN":
        modelo = KNeighborsClassifier(n_neighbors=3)
    elif classificador == "LR":
        modelo = LogisticRegression()
    elif classificador == "RF":
        modelo = RandomForestClassifier(n_estimators=20, random_state=0)
    elif classificador == "SVM_RBF":
        modelo = svm.SVC(kernel='rbf', C=1, gamma=10)
    elif classificador == "SVM_L":
        modelo =  svm.SVC(kernel='linear')
    elif classificador == "SVM_SVC":
        modelo = svm.LinearSVC()
    
    modelo.fit(freq, classes)
    return modelo

def convertResult(sample):
    result = []
    for s in sample:
        if(s == 'B'):
            result.append(0)
        else:
            result.append(1)
    return result

def demonstracaoResultados(freq, classes, modelo, teste=False):
    if (teste == True):
        resultados = modelo.predict(freq)
    else:
        resultados = cross_val_predict(modelo,freq, classes, cv=cv)
    
    accuracy = metrics.accuracy_score(classes,resultados)

    sentimento = ['B','H']
    print(metrics.classification_report(classes,resultados,sentimento, digits=3))
    print("\n\nAcurácia do modelo: ", accuracy)
    print("\n\nMatriz de confusão\n\n")
    print(pd.crosstab(classes, resultados, rownames=["Real"], colnames=["Predito"], margins=True), '')
    print("\nMSE (Mean squared error)  ", metrics.mean_squared_error(convertResult(classes),convertResult(resultados), multioutput='uniform_average'))
    print("\nRMSE (Root mean squared error)  ", np.sqrt(metrics.mean_squared_error(convertResult(classes),convertResult(resultados), multioutput='uniform_average')))
    print("\n\n\n")
    
def extracaoMassaTesteTreinamento(massa,divisao, Ifstemming):
    dataset = pd.read_excel(massa, dtype={'ID':str, 'Tweets':str, 'Rotulacoes': str}, index_col=None)
    train, test = train_test_split(dataset, test_size=divisao, random_state=1)
    t_1 = train[train['Rotulacoes']=='B'].sample(1285, replace=True) #Balanceando a massa de treino
    t_2 = train[train['Rotulacoes']=='H'].sample(1285,replace=True)
    training_bs = pd.concat([t_1, t_2])
    X_train = pre_processamento.tratamentoDados(training_bs['Tweets'], stemming=Ifstemming)
    Y_train = training_bs['Rotulacoes']
    X_test = pre_processamento.tratamentoDados(test['Tweets'],False)
    Y_test = test['Rotulacoes']
    
    return X_train, Y_train, X_test, Y_test
    
         
def tratandoDemonstrandoDados(classes, tweets, Ifstemming, Ifbigrama, classificador):
    tweets = pre_processamento.tratamentoDados(tweets, stemming=Ifstemming)
    freq_tweets = criacaoBagOfWords(tweets, bigrama=Ifbigrama)
    model = criacaoTreinamentoModelo(freq_tweets,classes, classificador)
    demonstracaoResultados(freq_tweets, classes, model)
    
def tratandoDemonstrandoDadosTesteTreinamento(massa, divisao,Ifstemming, Ifbigrama, classificador):
    X_train, Y_train, X_test, Y_test = extracaoMassaTesteTreinamento(massa,divisao, Ifstemming)
    cvec = CountVectorizer()
    if Ifbigrama:
        cvec = CountVectorizer(ngram_range=(1,2))
    else:
        cvec = CountVectorizer(analyzer="word")
    cvec.fit(X_train)
    train_data = cvec.transform(X_train)
    model = criacaoTreinamentoModelo(train_data,Y_train,classificador)
    test_data = cvec.transform(X_test)    
    demonstracaoResultados(test_data,Y_test,model)
    
def testeTreinamento(massaTreino, massaTeste,Ifstemming, Ifbigrama, classificador):
    df_train = pd.read_excel(massaTreino, dtype={'ID':str, 'Tweets':str, 'Rotulacoes': str}, index_col=None)
    df_test = pd.read_excel(massaTeste, dtype={'ID':str, 'Tweets':str, 'Rotulacoes': str}, index_col=None)

    X_train = pre_processamento.tratamentoDados(df_train['Tweets'], stemming=Ifstemming)
    Y_train = df_train['Rotulacoes']
    X_test = pre_processamento.tratamentoDados(df_test['Tweets'],False)
    Y_test = df_test['Rotulacoes']
    cvec = CountVectorizer()
    if Ifbigrama:
        cvec = CountVectorizer(ngram_range=(1,2))
    else:
        cvec = CountVectorizer(analyzer="word")
    cvec.fit(X_train)
    train_data = cvec.transform(X_train)
    model = criacaoTreinamentoModelo(train_data,Y_train,classificador)
    test_data = cvec.transform(X_test)    
    demonstracaoResultados(test_data,Y_test,model)
    