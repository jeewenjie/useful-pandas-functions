# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:32:57 2018

@author: Wen Jie
"""

import pandas as pd
import numpy as np

# Ratio to split data into train/test
cutoff = 0.8
traintest_cutoff = int(np.ceil(cutoff*50000))

df = pd.read_csv('\path')

# frac is an argument that returns the fractional number of total rows randomly
# So frac=1 means it returns everything randomly. reset_index renumbers the 
# indices to running order. Can set to False if unimportant/
df = df.sample(frac=1).reset_index(drop=True)

# :traintest_cutoff = traintest_cutoff
# traintest_cutoff: = 1-traintest_cutoff
train,test = df[:traintest_cutoff],df[traintest_cutoff:]
