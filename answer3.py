#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
from collections import Counter


# In[23]:


df = pd.read_csv("Captions.csv")


# In[26]:


df['date'] = pd.to_datetime(df['date'])


# In[57]:


temp_df = df[df['date']>'13/11/2021']
d = {}
for sentence in temp_df['caption']:
    if type(sentence) == str:
        for char in sentence:
            if not char.isalnum() and char!=' ':
                if char in d:
                    d[char]+=1
                else:
                    d[char] =1
k = Counter(d)
top_3 = k.most_common(3)
top3 = []
for i in top_3:
    top3.append((i[0],i[1]))
print(top3)


# In[52]:


d


# In[ ]:




