#!/usr/bin/env python
# coding: utf-8

# # Notebook do Curso de Pandas realizado por Marina Lima

# # Relatório de Análise VI

# # Criando Novas Variáveis

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[3]:


dados.head(10)


# In[4]:


dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']


# In[6]:


dados.head(10)


# In[7]:


dados['Valor m2'] = dados['Valor']/dados['Area']


# In[8]:


dados.head(10)


# In[9]:


dados['Valor m2'] = dados['Valor m2'].round(2) #Arrendondar duas casas decimais


# In[10]:


dados.head(10)


# In[11]:


dados['Valor Bruto m2'] = (dados['Valor Bruto']/dados['Area']).round(2)


# In[12]:


dados.head(10)


# In[15]:


casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']


# O método apply() permite que apliquemos uma função à cada registro do DataFrame. Para tanto, criaremos uma função lambda : 'lambda x: 'Casa' if x in casa else 'Apartamento'

# In[16]:


dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento') 


# In[17]:


dados


# In[20]:


pd.set_option('display.max_row', 21826)


# In[22]:


dados


# ## Excluindo Variáveis

# DUAS FORMAS:

# In[24]:


dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])


# In[25]:


dados_aux.head(10)


# In[26]:


del dados_aux['Valor Bruto']


# In[27]:


dados_aux.head(10)


# Outra maneira de excluir variáveis é utilizar o método pop(). Excluiremos neste exemplo a variável Valor Bruto m2

# In[28]:


dados_aux.pop('Valor Bruto m2')


# In[29]:


dados_aux


# Uma maneira de excluirmos múltiplas variáveis é utilizando o método drop(). Dessa vez, utilizaremos nosso DataFrame original, realmente deletando as variáveis Valor Bruto e Valor Bruto m2. No caso do método drop(), precisaremos especificar o eixo em que se dará a exclusão, uma vez que ele pode atuar especificamente em linhas ou colunas. Então, escreveremos axis = 1, afinal o eixo 0 corresponde às linhas e o 1 colunas. Precisaremos, ainda, assinalar inplace como True

# In[30]:


dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)


# In[31]:


dados.head(10)


# In[32]:


dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)


# In[ ]:




