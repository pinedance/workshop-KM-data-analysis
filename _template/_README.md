# How to Analysis Text Data of Traditional East Asian Medicine

강의를 준비하며 데이터 분석에 필요한 내용들을 정리해 본다. 

이 곳에 소개된 방법은 자연어처리 및 기계학습 등 데이터 분석에서 일반적으로 널리 사용되는 방법이다. 다만 사용된 데이터는 한의학 자료로 예시를 두었다. 

기본 개념을 설명할 때에는 toy data를 가지고 코드를 써가며 소개하고, 

그런 뒤에 실제 활용을 설명할 때에는 전문 package들에 구비되어 있는 high level api를 이용하였다. 

코드는 파이썬3를 기준으로 하였다. 

내용과 코드는 앞으로 조금씩 계속 업데이트 될 것이다. 

[PROJECT PAGE](*URL*/README.ipynb)


## Contents


### A. 데이터 분석 개요

1. [데이터 분석이란]

* 데이터 분석의 목적
* 데이터 분석의 가정


### B. 데이터 준비

1. [데이터 모으기](*URL*/B0100_Get_Data.ipynb)

* 웹스크래핑
* 데이터 불러오고 저장하기1 ( plain text / csv, tsv, json, yaml )
* 데이터 불러오고 저장하기2 ( raw object / pickle, joblib )

2. Pre-precessing

* [text normalization](*URL*/B0201_Text_Normalization.ipynb)
* [text manipulation & regular expression](*URL*/B0202_Preprocessing.ipynb)
* mapping & filtering

3. Tokenization (or Segmentation)

* [n-gram & others](*URL*/B0301_Tokenization.ipynb)
* [score based segmentation](*URL*/B0302_Tokenization2.ipynb), [lib](*URL*/B0302_Tokenization3_lib.ipynb)

4. 데이터 살펴보기

* item and feature ( Documents and term )
* [token and type](*URL*/B0401_Token_and_Type.ipynb)



### B. 데이터 임베딩(정량화)

* data structure ( vector, matrix, data_frame )

1. [Vectorization](*URL*/C0100_Vectorization.ipynb)

* 기본 전제 : distribution hyperthesis
* 1st order vector ( doc-feature matrix / tf, tfidf )
* 2nd order vector ( feature-feature matrix / co-word )
* special word embedding ( word2vec )

2. [Similarity & Distance](*URL*/C0200_Similarity_and_Distance.ipynb)


### C. 암묵지 확인1

1. [Observed value & Expected value](*URL*/D0100_Observed_value_Expected_value.ipynb)

* contingency table ( 2x2 table )

2. [Co-occurrence (or Collocations)](*URL*/D0200_Co-occurrence_Measures.ipynb)

* association measure1 ( co-word )
* association measure2 ( t-value, simple log likelyhood ratio, mutual information )

3. [Comparing](*URL*/D0300_Comparing.ipynb)

* Pearson correlation coefficient
* chi-square

### D. 암묵지 확인2

1. [Latent Analysis or Topic modeling](*URL*/E0100_Latent_Analysis_or_Topic_Modeling.ipynb)

* Latent Analysis or Topic modeling 
* Matrix Decomposition 

2. Clustering

* hierarchical clustering
* knn clustering

3. Network

* [Node and Edge ( Adjacency Matrix / Edge Lists )](*URL*/E0301_Node_and_Edge.ipynb)
* Visualize_network : [1. MDS](*URL*/E0302_Visualize_network1.ipynb), [2. VOS](*URL*/E0302_Visualize_network2.ipynb)
* community detection


### E. 학습과 예측

Modeling

* modeling, training(fitting), prediction

Regression

* linear regression

Classification

* logistic regression
* SVM

Neural Networking

* hyperthesis
* objective functon
* activation function
* optimization

### [F. Visualization](*URL*/G0200_Plots.ipynb)

dimension reduction

Plot 1

* 수치형 → histogram

Plot 2

* 범주형 × 수치형  →  box plot
* 수치형 × 수치형  →  scatter plot

Plot 3

* 수치형 × 수치형 × 범주형  →  scatter plot with color,  treemap
* 수치형 × 수치형 × 수치형  →  bubble chart 
* 범주형 × 범주형 × 수치형  →  heatmap

Plot 4 / Special

* Star(spider) chart
* Sankey Diagram


## Citation

please cite it as:

```yaml
author : Junho Oh
e-mail: pinedance@gmail.com / junho@kiom.re.kr
title : How to Analysis Text Data of Traditional East Asian Medicine
year : 2019
month : 02
keywords : Data Analysis, Traditional East Asian Medicine, Traditional Korean Medicine, Traditional Chinese Medicine
available from : https://github.com/pinedance/workshop-KM-data-analysis
```

© 2019 Junho Oh.