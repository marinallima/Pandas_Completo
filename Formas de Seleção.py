#!/usr/bin/env python
# coding: utf-8

# # Notebook do Curso de Pandas realizado por Marina Lima

# In[1]:


import pandas as pd


# In[2]:


data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())


# In[3]:


df


# In[4]:


df['c1']


# In[5]:


type(df['c1'])


# In[6]:


df[['c3','c1']]


# In[7]:


#Seleção de linhas
df[:]


# In[8]:


df[1:]


# In[9]:


df[1:3]


# In[10]:


df[1:][['c3','c1']]


# In[11]:


# Loc - seleções a partir dos rótulos das linhas
df.loc['l3']


# In[12]:


df.loc[['l3', 'l2']]


# In[13]:


df.loc['l1', 'c2']


# In[14]:


#iloc usa índices numéricos
df.iloc[0,1]


# In[15]:


df.loc[['l3', 'l1'], ['c4','c1']]


# In[16]:


df


# In[17]:


df.iloc[[2,0],[3,0]]

