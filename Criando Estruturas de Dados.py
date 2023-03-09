#!/usr/bin/env python
# coding: utf-8

# # Notebook do Curso de Pandas realizado por Marina Lima

# In[1]:


import pandas as pd


# # Series

# In[3]:


data = [1, 2, 3, 4, 5]


# In[4]:


s = pd.Series(data)


# In[5]:


s


# In[6]:


index = ['Linha' + str(i) for i in range(5)]


# In[7]:


index


# In[8]:


s = pd.Series(data = data, index = index)


# In[9]:


s


# In[10]:


data = {'Linha' + str(i) : i + 1 for i in range(5)}


# In[11]:


data


# In[12]:


s = pd.Series(data)


# In[13]:


s


# In[14]:


s1 = s + 2


# In[15]:


s1


# In[16]:


s2 =  s + s1


# In[17]:


s2


# # Dataframe - Concatenando Dataframes

# In[18]:


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]


# In[19]:


data


# In[20]:


df1 = pd.DataFrame(data = data)


# In[21]:


df1


# In[22]:


index = ['Linha' + str(i) for i in range(3)]


# In[23]:


index


# In[24]:


df1 = pd.DataFrame(data = data, index = index)


# In[25]:


df1


# In[26]:


columns = ['Coluna' + str(i) for i in range(3)]


# In[27]:


columns


# In[28]:


df1 = pd.DataFrame(data = data, index = index, columns = columns)


# In[29]:


df1


# In[30]:


data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}


# In[31]:


data


# In[32]:


df2 = pd.DataFrame(data)


# In[33]:


df2


# In[34]:


data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]


# In[35]:


data


# In[36]:


df3 = pd.DataFrame(data = data, index = index, columns = columns)


# In[37]:


df3


# In[38]:


## Concatenando Dataframes


# In[39]:


df1[df1 > 0] = 'A'
df1


# In[40]:


df2[df2 > 0] = 'B'
df2


# In[41]:


df3[df3 > 0] = 'C'
df3


# In[42]:


# CONCAT - Ferramenta de concatenação no Pandas
df4 = pd.concat([df1, df2, df3])
df4


# In[43]:


df4 = pd.concat([df1, df2, df3], axis = 1)
df4


# In[ ]:




