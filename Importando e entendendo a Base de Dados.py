#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise I

# # Importando a base de dados

# In[1]:


import pandas as pd


# In[5]:


pd.read_csv('dados/aluguel.csv' , sep = ';')


# In[6]:


dados = pd.read_csv('dados/aluguel.csv' , sep = ';')


# In[7]:


dados


# In[8]:


type(dados)


# In[10]:


dados.info()


# In[11]:


dados.head(10)


# # Informações gerais sobre a Base de Dados

# In[12]:


dados.dtypes


# In[14]:


tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])


# In[15]:


tipos_de_dados.columns.name = 'Variáveis'


# In[16]:


tipos_de_dados


# In[17]:


dados.shape


# In[18]:


dados.shape[0]


# In[19]:


dados.shape[1]


# In[20]:


print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0], dados.shape[1]))


# In[ ]:




