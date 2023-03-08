#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


json = open('dados/aluguel.json')
print(json.read())


# In[3]:


df_json = pd.read_json('dados/aluguel.json')
df_json 


# In[4]:


txt = open('dados/aluguel.txt')
print(txt.read())


# In[5]:


df_txt = pd.read_table('dados/aluguel.txt')
df_txt


# In[6]:


df_xlsx = pd.read_excel('dados/aluguel.xlsx')
df_xlsx


# In[7]:


df_html = pd.read_html('dados/dados_html_1.html')
df_html[0]


# In[ ]:




