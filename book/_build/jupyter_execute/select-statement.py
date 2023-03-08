#!/usr/bin/env python
# coding: utf-8

# # The SELECT statement
# Before going into details, let's create a **connection** to our database:

# In[1]:


import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/dvdrental')
engine.execution_options(isolation_level="AUTOCOMMIT")
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', '$engine.url')


# Most of the times, the [SELECT](https://www.postgresql.org/docs/current/sql-select.html) statement is used to fetch rows from a given table. Its general syntax is:
# ```sql
# SELECT column1, column2 FROM table_name;
# ```
# 
# In the example above, we're querying data from `column1` and `column2`, but we could also query data from **all** the columns by using the `*` [special character](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-SPECIAL-CHARS). For example:
# 

# In[2]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM actor LIMIT 5;\n')


# By the way, it's not good practice to use the asterisk ``*`` in the `SELECT` statement. For tables with a lot of columns, it will increase the amount of data that our application has to deal with, slowing it down. It's better to be specific about the the columns we're interested in pulling out. But for tables with small amount of columns, the `*` is just fine.

# [1]: 
# [2]: 
