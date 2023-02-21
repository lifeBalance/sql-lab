#!/usr/bin/env python
# coding: utf-8

# # Setting up the Postgres Connection
# In order to create a connection to the database (from this Jupyter notebook), we gotta import `sqlalchemy`, and [configure the engine](https://docs.sqlalchemy.org/en/20/core/engines.html), according to the settings we used when creating the user and the database.

# In[1]:


import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/bobDB')
engine.connect()
# engine.execution_options(isolation_level="AUTOCOMMIT")


# ## Magic Commands
# Now we want to [load the ipython-sql extension](https://ipython.readthedocs.io/en/stable/config/extensions/index.html):

# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# Thanks to the extension above, now we can run magic commands, aka [magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html) (the ones that start with `%` or `%%`). For example, if we wanted to check the connection, we could run:

# In[3]:


get_ipython().run_line_magic('sql', '$engine.url')


# Another variation is to use `%%sql` on its own line (the first line), and the SQL below it:

# In[4]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM pg_database;\n')


# ## Postgres Metacommands
# We can even run **metacommands** using the magic thing:

# In[5]:


get_ipython().run_line_magic('sql', '\\du')


# We can also run the `psql` command (or any other shell command) prepending a `!`, but note that we don't get an **interactive prompt**, just the static output.

# In[6]:


get_ipython().system('psql --username=bob --db=bobDB')


# In[ ]:




