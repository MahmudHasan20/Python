# -*- coding: utf-8 -*-
"""Demo code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BDs99XJ-sbSD5IEYxAB9JINa_rMkkBpn
"""

import pandas as pd
import numpy as np

s = pd.Series([12,-4,7,9])

s

s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
 s

s.values

s.index

s/2

np.log(s)

data = {'color' : ['blue','green','yellow','red','white'],
 'object' : ['ball','pen','pencil','paper','mug'],
 'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)
 frame

frame2 = pd.DataFrame(data, columns=['object','price'])

frame2

s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
 s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])

s1 + s2

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),index=['blue','green','white','yellow'],columns=['mug','pen','ball'])

frame1

frame2

frame1.add(frame2)

frame = pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])

frame

frame.sum()

frame.mean()

frame.describe()

seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])

seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008',
'2009','2010','2011','2012','2013'])

seq.corr(seq2)

seq.cov(seq2)