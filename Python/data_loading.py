#!/usr/bin/env python
# coding: utf-8

# # Data Loading
# 
# This notebook contains the steps for the loading the dataset and gathering info on the dataset.

# In[1]:


# Import required libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Locate the CSV whether the notebook is opened from the same folder
# or executed from the ChatGPT working directory.

df = pd.read_csv(r"MonthlyCrimeDashboard_KnifeCrimeData.csv")

# Keep separate copies for raw-data comparison and cleaning.
raw_df = df.copy()
clean_df = df.copy()


# In[3]:


# Display the first five rows to inspect the dataset structure.
clean_df.head()


# In[4]:


# Display the last five rows to inspect the end of the dataset.
clean_df.tail()


# In[5]:


# Check the number of rows and columns.
clean_df.shape


# In[6]:


clean_df.columns


# In[7]:


clean_df.info()


# In[8]:


clean_df.isnull().sum()


# In[9]:


clean_df.duplicated().sum()


# In[10]:


clean_df.describe()

