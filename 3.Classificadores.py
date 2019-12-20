# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:17:08 2018


@author: Amanda Mayara Menino   | GitHub: https://github.com/AmandaMMAlves
@author: Carla A. Madureira     | GitHub: https://github.com/carlalmadureira
"""

import sys
import time
import configs as cf

orig_stdout = sys.stdout
f = open('Resultados_Massa2570_FINAL_2.txt', 'w')
sys.stdout = f

        
classificadores = ["MBayes", "KNN", "LR", "RF", "SVM_RBF", "SVM_L", "SVM_SVC"]

classes, tweets = cf.extracaoDados('massa_2570_balanceada.xlsx') 
for classificador in classificadores:
    start_time = time.time()
    print("\n\n" + classificador)
    
    start_time_sb = time.time()
    print("\n\nAplicando Stemming e Bigrama")
    cf.tratandoDemonstrandoDados(classes, tweets, True, True, classificador)
    print("Tempo de Stemming e Bigrama: %s segundos" % (time.time() - start_time_sb))
    
    start_time_s = time.time()
    print("\n\nAplicando apenas Stemming")
    cf.tratandoDemonstrandoDados(classes, tweets, True, False, classificador)
    print("Tempo de apenas Stemming: %s segundos" % (time.time() - start_time_s))
    
    start_time_b = time.time()
    print("\n\nAplicando apenas Bigrama")
    cf.tratandoDemonstrandoDados(classes, tweets, False, True, classificador)
    print("Tempo de apenas Bigrama: %s segundos" % (time.time() - start_time_b))
    
    start_time_p = time.time()
    print("\n\nDemonstrando resultados puros")
    cf.tratandoDemonstrandoDados(classes, tweets, False, False, classificador)
    print("Tempo de resultados puros: %s segundos" % (time.time() - start_time_p))
    
    print("\n\n--------------------------------------------------")
    print("\nTempo total: %s segundos" % (time.time() - start_time))
    
sys.stdout = orig_stdout
f.close()