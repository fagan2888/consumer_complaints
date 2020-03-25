#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv
import itertools
from operator import itemgetter
import collections


# ### Read contents of the CSV

# * Identify columns in the CSV

# In[22]:


complaints = '/Users/chinmay/Documents/GitHub/consumer_complaints/insight_testsuite/test_1/input/complaints.csv'
with open(complaints, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        break 


# #### Problem Statement

# For each financial product and year, the total number of complaints, number of companies receiving a complaint, 
# and the highest percentage of complaints directed at a single company

# Group by using financial product and year
# - total number of complaints
# - number of companies receiving a complaint
# - highest percentage of complaints directed at a single company

# Compute for each financial product and year, the total number of complaints,
# number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

# ### Create dictionary from CSV using 'DictReader'

# In[26]:


rd = csv.DictReader(open(complaints, 'r'))
cc_list = []
for line in rd:
    cc_list.append(line)


# In[27]:


cc_list # Resultant dictionary created from DictReader


# #### Group by using 'Product' and 'Year'

# In[37]:


grouped_cc = collections.defaultdict(list)
for item in cc_list:
    grouped_cc[item['Product']].append(item)


# In[43]:


grouped_cc


# ### Calculate number of complaints for each type of complaint

# In[44]:


len(grouped_cc['Credit reporting, credit repair services, or other personal consumer reports'])


# In[45]:


len(grouped_cc['Debt collection'])


# #### Number of companies receiving the complaint

# In[46]:


company_cc = collections.defaultdict(list)
for item in cc_list:
    company_cc[item['Company']].append(item)


# In[54]:


company_cc


# ### Highest percentage of complaints directed at a single company


# In[ ]:




