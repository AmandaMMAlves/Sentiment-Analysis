# Sentiment-Analysis

Projeto de Iniciação Científica - FATEC Rubens Lara (Análise e Desenvolvimento de Sistemas) 

Esse estudo teve como objetivo classificar as opiniões contidas nos tweets no momento do 2º turno das eleições de 2018, por meio de experimentos realizados com diversos modelos de classificação textual. Após a coleta feita a partir da API do Twitter, foram rotulados mais de 9000 tweets, com a finalidade de gerar uma massa de dados para ser balanceada, pré-processada e utilizada para o aprendizados e testes desses modelos de classificação, auxiliando-os para melhores resultados preditivos.

Etapas Completas: 
1. Twitter Search
    Nesse momento por meio da API do Twitter, extraímos os tweets de acordo com data e hashtag.

2. Extração da Rotulação e Balanceamento da Massa
    Com massas extraídas e manualmente rotuladas por hashtags (armazenadas na pasta massas-extraidas-rotuladas), utilizamos um script para juntar as rotulações e balancear a massa, ou seja, ter a mesma quantidade de tweets pró Haddad e pró Bolsonaro, totalizando em 2570 tweets, de uma massa total de 9757.

3. Classificadores
    Tendo a massa balanceada, nesse momento utilizamos técnicas de pré processamento textual com o objetivo de facilitar no aprendizado dos modelos preditivos. Com essa massa mais preparada para o treinamento seguindo o conceito de cross-validation, usamos a seguinte listagem de classificadores nesse estudo:
        - Multinomial Naive Bayes
        - Suport Vector Machine
            - Utilizando o kernel RBF
            - Utilizando o kernel Linear
            - Utilizando o modelo Linear SVC
        - K-Nearest Neighbors
        - Random Florest
        - Regressão Logística
    Treinamos esses modelos, alternando os métodos de pré processamento com as seguintes técnicas: steeming e bigrama, o resultado disso tudo você pode conferir no arquivo Resultados_Finais.xlsx.


