#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy-financial')


# In[3]:


import numpy_financial as npf


# In[8]:


rate = .12
cashflows = [-425000,150000,150000,150000,150000,150000]


# In[7]:


print (f' "$" {npf.npv( rate,cashflows):,.2f}').plot()


# In[8]:


discounted = []
for year in range(len(cashflows)):
    discounted.append(cashflows[year]/ (1 + rate )** year)
discounted


# In[9]:


sum(discounted)


# In[11]:


irr = npf.irr(cashflows)


# In[5]:


npf.npv(irr,cashflows)


# In[4]:


import matplotlib.pyplot as plt 


# In[2]:


from matplotlib import rcParams 
rcParams['figure.figsize']= 8,6


# In[19]:


print (f' $ {npf.npv( rate,cashflows):,.2f}')


# In[ ]:





# In[ ]:




