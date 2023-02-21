#!/usr/bin/env python
# coding: utf-8

# # Loading a sample Database
# To practice our SQL-fu, we'll be using a sample database named `dvdrental` downloaded from [here](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/). This database can be found online in several places, usually as a [zip file](https://en.wikipedia.org/wiki/ZIP_(file_format)) which we have to extract. The result is a [tar file](https://en.wikipedia.org/wiki/Tar_(computing)) that we'll be loading into our database using [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).
# 
# > You should find the `dvdrental.tar` file in the repository files.
# 
# First thing we have to do is to create a connection to Postgres:

# In[1]:


import sqlalchemy
# Let's create a connection to the bobDB database for bob.
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/bobDB')
engine.execution_options(isolation_level="AUTOCOMMIT")

# While we're at it, let's also load the `ipython-sql` extension
get_ipython().run_line_magic('load_ext', 'sql')


# ## Restoring a Database
# Now we can use `pg_restore` to restore the database from the `dvdrental.tar` file. We'll be using several options:
# 
# - `-c` (short for `--clean`) is for dropping database objects before recreating them.
# - `-d` (short for `--dbname`) is for restoring the data directly into the database used as argument (the `dvdrental` we created before).

# In[2]:


get_ipython().system('pg_restore -U bob -c -d dvdrental ./dvdrental.tar')


# ## Connecting to the New Database
# One thing I noticed about `sqlalchemy` is that once we create an engine for a database, we can't use it connect to another database. So if, for example, we wanted to use:

# In[3]:


get_ipython().run_line_magic('sql', '\\connect dvdrental')


#  We'd get an **error**. The **solution** is to create an additional engine for this database:

# In[4]:


engine2 = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/dvdrental')
engine2.execution_options(isolation_level="AUTOCOMMIT")
get_ipython().run_line_magic('sql', '$engine2.url')


# To test out our connection, let's list the **tables** in the `dvdrental` database:

# In[5]:


get_ipython().run_line_magic('sql', '\\dt')

