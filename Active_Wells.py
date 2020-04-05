

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

# In[5]:


#read in datafile - all wells (2 million +)
data=pd.read_csv('di_data_for_input.csv', sep=',')

#remove negative production volumes
data.LATEST_GAS[data.LATEST_GAS <0]=0
data.LATEST_LIQ[data.LATEST_LIQ <0]=0

# In[6]:


#pull year out of first and last production date and make new column
data['year_first']=pd.DatetimeIndex(data['FIRST_PROD_DATETIME']).year
data['year_last']=pd.DatetimeIndex(data['LAST_PROD_DATETIME']).year


# In[5]:


#data


# In[6]:


active_types = ['ACTIVE']


# In[7]:


active_wells=data[data.STATUS.isin(active_types)]


# In[8]:
#Calculate Monthly average for all wells

active_wells['MONTHLY_GAS_PROD'] = active_wells.GAS_CUM/(active_wells.MONTHS_PRODUCED)


# In[9]:


active_wells['MONTHLY_LIQ_PROD'] = active_wells.LIQ_CUM/(active_wells.MONTHS_PRODUCED)


# In[10]:


#Drop Data with NaN in critical columns
active_wells = active_wells.dropna(subset=['MONTHLY_GAS_PROD','MONTHLY_LIQ_PROD'])


# In[11]:


#active_wells


# In[12]:


df1 = active_wells.groupby('STATE').sum()
#df1


# In[13]:


df2 = active_wells.groupby('STATE').count()
df1['Number_Active_Wells'] = df2['Unnamed: 0']


# In[35]:


#df2


# In[15]:


Summary = df1[['Number_Active_Wells','LATEST_GAS','MONTHLY_GAS_PROD','LATEST_LIQ','MONTHLY_LIQ_PROD']]
Summary

Summary_Final = df1[['Number_Active_Wells','MONTHLY_GAS_PROD','MONTHLY_LIQ_PROD']]
Summary_Final

# In[61]:


print(Summary)
print(Summary_Final)

