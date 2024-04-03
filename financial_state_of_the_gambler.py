#!/usr/bin/env python
# coding: utf-8

# <h1>RANDOM WALK CASE STUDY: GAMBLER FINANCIAL STATE</h1>

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


np.random.seed(123)


# In[3]:


def bet(amount,stake=10)->int:
    if np.random.randint(0,2):
        return amount + stake
    return 0


# In[4]:


def bet_experiment(balance=[10],bets=10)->list:
    for b in range(bets):
        balance.append(bet(balance[b]))
    return balance
    


# In[5]:


bet_experiment([50],1)


# In[6]:


distribution = []
for sim in range(1000):
    distribution.append(bet_experiment([50],10)[-1])    


# In[8]:


plt.hist(distribution)
plt.show()

