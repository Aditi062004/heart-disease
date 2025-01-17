#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("D:/heart_disease_data.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.info()


# In[9]:


data.isnull().sum()


# In[11]:


val=data.duplicated().any()
print(val)


# In[12]:


data=data.drop_duplicates()


# In[13]:


data.head()


# In[14]:


data.shape


# In[16]:


data.corr()


# In[24]:


plt.figure(figsize = (20, 6))
sns.heatmap(data.corr(),annot=True, annot_kws = {"size":11})


# In[25]:


data.columns


# In[29]:


import warnings
warnings.filterwarnings("ignore")
sns.countplot(data["target"])
plt.show()


# In[31]:


sns.countplot(data["sex"])
plt.show()


# In[34]:


sns.countplot(x=data["sex"],hue=data["target"])
plt.xticks([0,1],["female","male"])
plt.legend(labels=["no disease","disease"])


# In[36]:


sns.distplot(data["age"],bins=30)
plt.show()


# In[38]:


sns.countplot(data["cp"])
plt.xticks([0,1,2,3],["Typical Angina","Atypical Angina","Non-anginal pain","Asymptomatic"])
plt.show()


# In[47]:


sns.countplot(x=data["cp"], hue=data["target"])
plt.legend(labels=["no disease","disease"])
plt.show()


# In[48]:


data["trestbps"].hist()


# In[49]:


data["chol"].hist()


# In[ ]:




