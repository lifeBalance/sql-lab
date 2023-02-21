#!/usr/bin/env python
# coding: utf-8

# # Metacommands
# In Postgres can use [psql metacommands](https://www.postgresql.org/docs/current/app-psql.html) also known as slash or backslash commands.

# In[1]:


import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/dvdrental')
engine.execution_options(isolation_level="AUTOCOMMIT")
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', '$engine.url')


# In[2]:


get_ipython().run_line_magic('sql', '\\dt')


# In[ ]:




