#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('WineQT.csv')


# In[3]:


df.head()


# In[4]:


# information about data set
df.info()


# In[5]:


#describe
df.describe()


# In[6]:


#shhape of a data set
df.shape


# In[7]:


df.columns


# In[8]:


df['quality'].unique()


# In[9]:


# it is a imbalnce data set
df['quality'].value_counts()


# In[10]:


# missing value
df.isnull()


# In[11]:


# missing value count
df.isnull().sum()


# In[12]:


# to check dubllicated record
df[df.duplicated()]


# In[13]:


# removing duplicate
df.drop_duplicates(inplace=True)


# In[14]:


df


# In[15]:


df.shape


# In[16]:


df.corr()


# In[17]:


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True)


# In[18]:


df.quality.value_counts().plot(kind='bar')


# In[19]:


df.quality.value_counts().plot(kind='box')


# In[20]:


df.quality.value_counts().plot(kind='hist')


# In[21]:


sns.distplot(df['fixed acidity'])


# In[22]:


for i in df.columns:
    sns.histplot(df[i],kde=True)


# In[23]:


# categrocial plot
sns.catplot(x='alcohol',y='pH',data=df,hue='quality')


# In[ ]:





# In[ ]:





# In[ ]:




