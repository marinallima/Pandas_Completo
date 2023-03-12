#!/usr/bin/env python
# coding: utf-8

# # Notebook desenvolvido por Marina Lima durante o curso completo de Pandas

# # Relatório de Análise VII

# ## Criando Agrupamentos

# In[17]:


import pandas as pd


# In[18]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[19]:


dados.head(10)


# In[20]:


dados['Valor'].mean()


# In[21]:


bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]


# In[22]:


dados['Bairro'].drop_duplicates()


# In[23]:


grupo_bairro = dados.groupby('Bairro')


# In[24]:


type(grupo_bairro)


# In[25]:


grupo_bairro.groups


# In[26]:


for bairro, dados in grupo_bairro: 
    print(bairro)


# In[27]:


for bairro, data in grupo_bairro: 
    print('{} -> {}'.format(bairro, dados.Valor.mean()))


# In[28]:


grupo_bairro[['Valor']].mean()


# In[29]:


grupo_bairro[['Valor', 'Condominio']].mean().round(2)


# # Estatísticas Descritivas

# #### https://pandas.pydata.org/pandas-docs/stable/api.html#api-dataframe-stats

# ## Com a função describe() teremos um DataFrame com as colunas count a frequência; mean a média; std o desvio padrão; mino valor mínimo; 25% o primeiro quartil, 50% a mediana, 75% o terceiro quartil e max, o valor máximo.

# In[31]:


grupo_bairro['Valor'].describe().round(2)


# ## O método aggregate() só mostra o conjunto de estatísticas que eu quero.

# In[33]:


grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = {'min': 'Mínimo', 'max': 'Máximo', 'sum': 'Soma'})


# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))


# In[36]:


fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')


# In[37]:


fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})


# In[38]:


fig = grupo_bairro['Valor'].max().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Máximo do Aluguel por Bairro', {'fontsize': 22})


# In[ ]:




