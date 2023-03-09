#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)


# In[3]:


s


# In[4]:


s.fillna(0)


# Existem outros métodos para realizarmos a interpolação, um deles é o ffill(). Esse método, analisa a Series do primeiro elemento ao último, e uma vez que for encontrada um valor nulo, ele coletará o valor da última assinatura válida.

# In[5]:


s.fillna(method = 'ffill')


# Outro método que conheceremos é o bfill(), que por sua vez realiza a mesma análise das assinaturas em uma Series, mas dessa vez de baixo para cima, isto é, do último elemento da Series ao primeiro.

# In[6]:


s.fillna(method = 'bfill')


# Podemos, inclusive, não utilizar método algum para realizar uma interpolação. Por meio de fillna(), coletaremos a média de todos os valores não-nulos e a usaremos como preenchimento. Para tanto, basta escrever s.mean()

# Por meio de fillna(), coletaremos a média de todos os valores não-nulos e a usaremos como preenchimento. Para tanto, basta escrever s.mean()

# In[7]:


s.fillna(s.mean())


# In[8]:


s


# Existe outro parâmetro que pode nos ajudar a não cometer esse tipo de erro no banco de dados. Primeiramente chamaremos nossa Series s, em seguida adicionaremos o método ffill, seguido do parâmetro limit, que receberá como valor 1

# In[10]:


s.fillna(method = 'ffill', limit = 1)


# In[13]:


s1 = s.fillna(method = 'ffill', limit = 1)


# In[14]:


s1


# In[15]:


s1 = s.fillna(method = 'bfill', limit = 1)


# In[16]:


s1


# In[ ]:




