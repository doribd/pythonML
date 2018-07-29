
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[7]:


sns.distplot(tips['total_bill'],kde=False)


# In[9]:


sns.jointplot(x='total_bill',y='tip',data=tips)


# In[10]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[11]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[12]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[13]:


sns.pairplot(tips)


# In[14]:


sns.pairplot(tips,hue='sex')


# In[16]:


sns.rugplot(tips['total_bill'])


# In[17]:


sns.barplot(x='sex',y='total_bill',data=tips)


# In[18]:


import numpy as np;
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[19]:


sns.boxplot(x='day',y='total_bill',data=tips)

