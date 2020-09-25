import pandas as pd
import numpy as np
import warnings
from math import log

# 경고 메세지를 숨기기 위한 모듈
warnings.filterwarnings('ignore')

# 데이터 불러오기
data = pd.read_excel('./data/review.xlsx')
# print(data.shape)

# 데이터 정규 분포
data['score'].value_counts(sort=False, ascending=False).plot(kind='bar', figsize=(8,4))

# Null 찾기
print('### null isExist: ',data.isnull().values.any(), ', count :',data.isnull().values.sum())
data.loc[data['content'].isnull()]

data = data.dropna(how='any')

# 불용어 정의
stopword = ['의','가','은','수','들','더','는','잘','강',
            '과','를','으로','에게','자','에','와','한','하다',
            '.','..', '...', '?','\n', '^', '에서', '!']

def without_stopword (words) :
    word_without_stopword = []
    for word in words.split() :
        if word not in stopword:
            word_without_stopword.append(word)
    
    return word_without_stopword

# TF-IDF 직접 구현하기
# 단어 저장
vocab = list(set(word for item in data.iterrows() for word in without_stopword(item[1].content)))
vocab.sort()

N = len(data)

# TF, IDF, TF-IDF 값 구하는 함수

# TF(d,t) : 특정 문서 d에서의 특정 단어 t의 등장 횟수.
# DF :특정 단어 t가 등장한 문서의 수.
# IDF : df(t)에 반비례하는 수.

# TF-IDF는 TF와 IDF를 곱한 값으로 점수가 높은 단어일수록 다른 문서에는 
# 많지 않고 해당 문서에서 자주 등장하는 단어를 의미한다.

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for item in data.iterrows():
        df += int(str(t) in item[1].content)
    return log(N/ (df + 1))

def tfidf(t,d):
    return tf(t,d) * idf(t)

res_tf = []
res_idf = []
res_tf_idf = []

# for i in range(N):
#     res_tf.append([])
#     res_tf_idf.append([])

#     d = data.content[i]
#     for j in range(len(vocab)):
#         t = vocab[j]
#         res_tf[-1].append(tf(t,d))
#         # res_tf_idf[-1].append(tfidf(t,d))

for j in range(len(vocab)):
    res_idf.append(idf(j))

# DTM (문서 단어 행렬)로 표시
# result_tf = pd.DataFrame(res_tf, columns=vocab)
result_idf = pd.DataFrame(res_idf, index=vocab, columns=['IDF'])
# result_tf_idf = pd.DataFrame(res_tf_idf, columns=vocab)

# print(result_tf)
print(result_idf)
# print(result_tf_idf)

txt_idf = open('./data/review.idf.txt', 'w')
txt_idf.write(str(vocab))
txt_idf.close()