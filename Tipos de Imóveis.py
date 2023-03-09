#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise II

# # Tipos de Imóveis

# In[19]:


import pandas as pd


# In[20]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[21]:


dados.head(10)


# In[22]:


dados['Tipo']


# In[23]:


dados.Tipo


# In[24]:


tipo_de_imovel = dados['Tipo']


# In[25]:


type(tipo_de_imovel)


# In[26]:


tipo_de_imovel.drop_duplicates()


# In[27]:


tipo_de_imovel.drop_duplicates(keep='first', inplace=False)


# In[28]:


tipo_de_imovel


# ## Organizando a Visualização

# In[29]:


tipo_de_imovel = pd.DataFrame(tipo_de_imovel)


# In[30]:


tipo_de_imovel


# In[31]:


tipo_de_imovel.index


# In[32]:


tipo_de_imovel.shape[0]


# In[33]:


range(tipo_de_imovel.shape[0])


# In[34]:


for i in range(tipo_de_imovel.shape[0]):
    print(i)


# In[35]:


tipo_de_imovel.index = range(tipo_de_imovel.shape[0])


# In[36]:


tipo_de_imovel


# In[37]:


tipo_de_imovel.columns.name = 'id'
tipo_de_imovel


# In[39]:


pd.get_option('display.max_rows')


# In[40]:


pd.set_option('display.max_rows', 19831)


# In[41]:


tipo_de_imovel

