#!/usr/bin/env python
# coding: utf-8

# # Notebook desenvolvido por Marina Lima no curso completo de Pandas.

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15,8))


# In[13]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head()


# In[14]:


area = plt.figure() 


# In[15]:


# area.add_subplot(2, 2, 1)
# esse (2, 2, 1) significa que dentro desse grágico vão ter 2 linhas 2 colunas e ele estará na posição 1


# In[16]:


g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)


# ### Scatterplot - gráfico de dispersão.

# In[17]:


g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor X Área')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100) # sample = amostra de tamanho 100
dados_g3.index = range(dados_g3.shape[0]) #refazendo o índice
g3.plot(dados_g3)
g3.set_title('Amostra (Valor)')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')


# In[18]:


area


# ### Incluímos os argumentos dpi, que configura a resolução, e o bbox, que remove a borda branca da área do gráfico, tornando nossa apresentação mais elegante.

# In[19]:


area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')

