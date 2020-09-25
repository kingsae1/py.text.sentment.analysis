import numpy as np # numpy 도 함께 import
import pandas as pd
# import matplotlib as plt

data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data)
# print(df[['name','points']])

df['test'] = [0.1, 0.2, 0.3, 0.4, 0.5]

# print(df.test.sum())
# print(df[df['test'] == 0.2])
print(df.points.iloc[0])