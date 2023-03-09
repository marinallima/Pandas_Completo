#!/usr/bin/env python
# coding: utf-8

# # Organizando Dataframes

# In[1]:


import pandas as pd


# In[2]:


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[3]:


data


# In[4]:


list('321')


# In[5]:


df = pd.DataFrame(data, list('321'), list('ZYX'))    #Passou a lista como Index


# In[6]:


df


# In[7]:


df.sort_index(inplace = True)


# In[8]:


df


# In[9]:


df.sort_index(inplace = True, axis = 1)


# In[10]:


df


# In[11]:


df.sort_values(by = 'X', inplace = True)
df


# In[12]:


df.sort_values(by = '3', axis = 1, inplace = True)
df


# In[13]:


df.sort_values(by = ['X','Y'], inplace = True)
df


# In[ ]:




