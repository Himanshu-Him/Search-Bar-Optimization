#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import Levenshtein as lp
import pandas as pd
import sys


# In[16]:


'''Creating a dataframe which consists of:
Color, Fuel_type, Accessories, Transmission_Type, Features, Body-types''' 

data_excel = pd.read_csv('All_Features.csv')
data_excel['name'] = data_excel['name'].str.lower() 
data_excel['display_name'] = data_excel['display_name'].str.lower()


# In[17]:


secondary_dictionary = {}  ## Secondary dictionary is used as a decoy for making the final processed dictionary.
make = data_excel['name']
for i in make:
    make1 = []
    x = str(i)
    for j in range(3,len(x)):
        if(x[j - 1] == ' '):
            continue
        make1.append(x[0:j])
    make1.append(x)
    secondary_dictionary[x] = make1
model1 = []
make_sub1 = []
ct = 0
for i in range(len(data_excel['name'])):
    make = data_excel['name'].iloc[i]
    model = data_excel['display_name'].iloc[i]
    for make_sub in secondary_dictionary[make]:
        model1.append(model)
        make_sub1.append(make_sub)
df_split = {'name' : make_sub1, 'display_name' : model1}   #df_split is the dataframe made from the dictionary which has sliced elements upto 3 letters from the original dataset entries
df_split = pd.DataFrame(df_split)


# # Calculating Edit Distance

# In[18]:


inp = input()
edit_dist = {}  ## Making a dictionary that'll calculate the edit distance between incorrect and correct entries in our dataset.
for names in df_split['name']:
    if names in edit_dist:
        continue
    else:
        edit_dist[names] = lp.distance(str(names), inp)


# In[19]:


minimum = sys.maxsize
min_name = ''
for i in edit_dist:
    if edit_dist[i] < minimum:
        minimum = edit_dist[i]
        min_name = str(i)
minimum, min_name


# In[27]:


edi = []
for make in df_split['name']:
    edi.append(edit_dist[make])
df_split['ed'] = edi

c = minimum
result = []
for k in range(len(df_split['display_name'])):
    if df_split['ed'].iloc[k] == c:
        result.append(df_split['display_name'].iloc[k])
result = list(set(result))
result


# In[28]:


# checking the first letter match
for i in range (len(result)):
    if result[i][0] == inp[0]:
        print (result[i])

