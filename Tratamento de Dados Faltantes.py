#!/usr/bin/env python
# coding: utf-8

# # Notebook do Curso de Pandas realizado por Marina Lima

# # Relatório de Análise  V

# ## Tratamento de Dados Faltantes 

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[3]:


dados.head(10)


# In[4]:


dados.isnull()


# In[5]:


dados.notnull()


# In[7]:


dados.info() #Ver se alguma variável tem valor nulo


# In[11]:


dados['Valor'].isnull()


# In[13]:


dados[dados['Valor'].isnull()] #Ver os da variável Valor que estão nulos


# In[15]:


#Eliminar os null do banco
A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True)
B = dados.shape[0]
A - B


# In[16]:


dados[dados['Valor'].isnull()]


# In[17]:


dados[dados['Condominio'].isnull()].shape[0]


# In[18]:


selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())


# In[19]:


A = dados.shape[0]
dados = dados[~selecao] # Para eliminar as assinaturas nulas selecionadas ao invés de coletá-las, 
#iremos adicionar ~ em selecao, que inverte a Series booleana.
B = dados.shape[0]
A - B


# In[20]:


dados[dados['Condominio'].isnull()].shape[0]


# In[21]:


dados = dados.fillna({'Condominio': 0, 'IPTU': 0})


# In[22]:


dados[dados['Condominio'].isnull()].shape[0]


# In[23]:


dados[dados['IPTU'].isnull()].shape[0]


# In[24]:


dados.info()


# In[25]:


dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)


# In[ ]:




