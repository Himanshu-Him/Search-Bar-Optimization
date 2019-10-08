#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import Levenshtein as lp
import math
import sys


# In[11]:


df = pd.read_excel('mmv.xlsx')


# In[12]:


r = []
ind = 0
for i in df['model_name']:
    j = i.split(' ')
    r.append(j[len(j)-1])


# In[13]:


df['r']=r


# In[6]:


# merging
df1 = []
df2 = []
for j in range(2):
    for i in df['model_name']:
        df2.append(str(i))
for i in df['make_name']:
    df1.append(str(i))
for i in df['r']:
    df1.append(str(i))
df1 = {'make_name' : df1, 'model_name' : df2}
df1 = pd.DataFrame(df1)


# In[8]:


df2 = {}
make = df1['make_name']
for i in make:
    make1 = []
    x = str(i)
    for j in range(3,len(x)):
        if(x[j - 1] == ' '):
            continue
        make1.append(x[0:j])
    make1.append(x)
    df2[x] = make1
#     print(x, ':', df2[x])
model1 = []
make_sub1 = []
ct = 0
for i in range(len(df1['make_name'])):
    make = df1['make_name'].iloc[i]
    model = df1['model_name'].iloc[i]
    for make_sub in df2[make]:
        model1.append(model)
        make_sub1.append(make_sub)
df3 = {'make_name' : make_sub1, 'model_name' : model1}
df3 = pd.DataFrame(df3)
df3=df3.apply(lambda x: x.astype(str).str.lower())


# In[ ]:


#Taking the input value and comparing edit distance with every value in the dataset
inp = input()
ed = {}
for names in df3['make_name']:
    if names in ed:
        continue
    else:
        ed[names] = lp.distance(str(names), inp)


# In[ ]:


mi = sys.maxsize
mi_name = ''
for i in ed:
    if ed[i] < mi:
        mi = ed[i]
        mi_name = str(i)
mi, mi_name


# In[ ]:


edi = []
for make in df3['make_name']:
    edi.append(ed[make])
df3['make_ed'] = edi

c = mi
li = []
for k in range(len(df3['model_name'])):
    if df3['make_ed'].iloc[k] == c:
        li.append(df3['model_name'].iloc[k])
# converting into set to get rid of same values in our dataset
li = set(li)
# coverting back into list as further operations can be implemented only on list
li_list = list(li)
li_list


# In[ ]:


# check the first letter match
for i in range (len(li)):
    if li_list[i][0] == inp[0]:
        print (li_list[i])


# In[ ]:


# for i in range(len(li_list)):
#     te = li_list[i].split()
# for j in range(len(te)):
#     if te[j] == inp:
#         print (li[i])
#     elif te[j][0] == inp[0]:
#         print (li_list[i])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




