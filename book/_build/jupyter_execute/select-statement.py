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


# ## Querying All columns
# Most of the times, the [SELECT](https://www.postgresql.org/docs/current/sql-select.html) statement is used to fetch rows from a given table. To query data from **all** the columns in a given table we would use the following syntax:
# ```sql
# SELECT * FROM table_name;
# ```
# 
# > If for some reason, you don't remember the **names of the tables** in a given database, you can use the `\dt` meta-command. Or if you're using pgAdmin, you can **right-click** on `sql-lab > Databases > dvdrental > Schemas > public > Tables`.
# 
# In the query above we're using the `*` [special character](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-SPECIAL-CHARS). For example, let's pull all the columns from the `actor` table:

# In[2]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM actor LIMIT 5;\n')


# By the way, in the query above, we can see we're using the [LIMIT](https://www.postgresql.org/docs/15/queries-limit.html) statement in order to limit the number of rows in the result.
# 
# ## Querying Some Columns
# For tables tables with small amount of columns, using the `*` in the `SELECT` statement is just fine. But for tables with a lot of columns, this is not a good practice. It'd increase the amount of data that our application has to deal with, slowing it down. It's better to be specific about what columns we're interested in pulling out. The general syntax for doing that is quite simple:
# ```sql
# SELECT column1, column2 FROM table_name;
# ```
# 
# As you can see, we have to separate the column names by a comma (`,`). For example, let's say we want to pull out the `first_name` and `last_name` of the first five actors in the `actor` table:

# In[3]:


get_ipython().run_cell_magic('sql', '', 'SELECT first_name, last_name FROM actor LIMIT 5;\n')


# ### A trick to get the Column Names
# Often times, we won't remember the names of the columns in a given table. In that case, the following query may come in handy:

# In[4]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM actor WHERE false;\n')


# Don't worry too much right now about the meaning of the [WHERE](https://www.postgresql.org/docs/current/sql-select.html) clause ;-)
# 
# ## The DISTINCT clause
# Another useful clause we can use with the [WHERE](https://www.postgresql.org/docs/current/sql-select.html) statement is the `DISTINCT` clause. For example, let's say we're interested in the rate for renting movies; if we do:

# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT rental_rate FROM film LIMIT 5;\n')


# We can see that among the first movies, we have different rates (`4.99` and `0.99`) but we don't want to check all of the rows to see how many different rates are available. To easily find out how many **different** rates exist in this table, we could add a little tweak to our last statemement:

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT rental_rate FROM film;\n')


# As we can see, now it's clear that there are only three type of rates. Another example, imagine we want to know how many **movie ratings** are available in the USA:

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT rating FROM film;\n')

