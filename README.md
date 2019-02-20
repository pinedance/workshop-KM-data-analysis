# How to Analysis Text Data of Traditional Chinese Medicine

강의를 준비하며 데이터 분석에 필요한 내용들을 정리해 본다. 

이 곳에 소개된 방법은 자연어처리 및 기계학습 등 데이터 분석에서 일반적으로 널리 사용되는 방법이다. 다만 사용된 데이터는 한의학 자료로 예시를 두었다. 

기본 개념을 설명할 때에는 toy data를 가지고 코드를 써가며 소개하고, 

그런 뒤에 실제 활용을 설명할 때에는 전문 package들에 구비되어 있는 high level api를 이용하였다. 

코드는 파이썬3를 기준으로 하였다. 

내용과 코드는 앞으로 조금씩 계속 업데이트 될 것이다. 


## Contents


### 로드맵

### A. 데이터 준비

1. 데이터 모으기

* 웹스크래핑
* 데이터 불러오고 저장하기1 ( plain text / csv, tsv, json, yaml )
* 데이터 불러오고 저장하기2 ( binary / pickle )
* 데이터 형태 ( vector, matrix, data_frame )

2. 데이터 전처리

* 정규식
* 필터링과 맵핑

3. 데이터 살펴보기

* item and feature ( Documents and term )
* token and type
* tokenization (or segmentation)


### B. 데이터 임베딩(정량화)

1. Vectorization

* 기본 전제 : distribution hyperthesis
* 1st order vector ( doc-feature matrix / tf, tfidf )
* 2nd order vector ( feature-feature matrix / co-word )
* special word embedding ( word2vec )

2. similarity & distance

### C. 숨은 의미 탐색

1. Latent Analysis & Topic modeling

* Latent Analysis & Topic modeling 
* Matrix Decomposition 


### D. 암묵지 확인

1. Observed value & Expected value

* contingency table ( 2x2 table )

2. Co-occurrence (or Collocations)

* co-occurrence measure1 ( co-word )
* co-occurrence measure2 ( t-value, simple log likelyhood ratio, mutual information )

3. Comparing

* Pearson correlation coefficient
* chi-square

4. Clustering

* hierarchical clustering
* knn clustering

5. Network Analysis

* node and edge
* matrix vs list
* build network
* visualization


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

### F. Visualization

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


