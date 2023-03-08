#!/usr/bin/env python
# coding: utf-8

# # Metacommands
# In Postgres can use [psql metacommands](https://www.postgresql.org/docs/current/app-psql.html) also known as slash or backslash commands. Let's create a connection to the database we created in the last section (`dvdrental`):

# In[1]:


import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/dvdrental')
engine.execution_options(isolation_level="AUTOCOMMIT")
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', '$engine.url')


# ## Listing Databases in the Server
# To list the **databases** in a server, we could use `\list` [meta-command][0]:

# In[2]:


get_ipython().run_line_magic('sql', '\\list')


# ## Listing Tables in a Database
# Once we're connected to a database, we may want to list the tables, which can be easily done using the `\dt` [meta-command](https://www.postgresql.org/docs/current/app-psql.html):

# In[3]:


get_ipython().run_line_magic('sql', '\\dt')


# We could also use a proper `SQL` query, but as you can see, it's way more verbose:

# In[4]:


get_ipython().run_cell_magic('sql', '', "SELECT *\nFROM pg_catalog.pg_tables\nWHERE schemaname != 'information_schema' \n  AND schemaname != 'pg_catalog';\n")


# ## Meta-commands are `psql` shortcuts
# We've shown a couple of meta-commands exampls, but you may be wondering where and how can you run them (outside a Jupyter notebook). For example, let's log in into the **PostgreSQL server** we have running locally in our Docker container, using the credentials we set in our Docker compose file:
# ```
# psql -U bob -d postgres -h 127.0.0.1                                     
# Password for user bob: 
# psql (12.9, server 15.2 (Debian 15.2-1.pgdg110+1))
# WARNING: psql major version 12, server major version 15.
#          Some psql features might not work.
# Type "help" for help.
# 
# postgres=#
# ```
# 
# In the example above, we're connecting to a PostgreSQL server running locally using the flags:
# 
# - `-U` to specify the username, `bob`.
# - `-d` to specify the database.
# - `-h` to connect to the server running at `localhost`.
# 
# By the way, you can exit the connection with the `\q` meta-command ;-)
# 
# > Something that has me scratching my head is that even though the Docker service is running with the name `postgres` (which I use to set up a server in pgAdmin), I need to use `localhost` to connect to it via `psql` (and Alchemy too). 
