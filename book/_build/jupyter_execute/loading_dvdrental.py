#!/usr/bin/env python
# coding: utf-8

# # Loading a sample Database
# To practice our SQL-fu, we'll be using a sample database named `dvdrental` downloaded from [here](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/). This database can be found online in several places, usually as a [zip file](https://en.wikipedia.org/wiki/ZIP_(file_format)) which we have to extract. The result is a [tar file](https://en.wikipedia.org/wiki/Tar_(computing)) that we'll be loading into our database using [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).
# 
# > You should find the `dvdrental.tar` file in the repository files.
# 
# ## Create a Database
# First thing we have to do is to create a database named `dvdrental`:
# ```
# createdb -h localhost -p 5432 -U bob dvdrental
# ```
# 
# > You'll be **interactively** prompted for a password, so run the command above in a **terminal**.
# 
# ## Restore data
# Once the database has been created, we can **restore** the data from the `dvdrental.tar` file. We'll be using the `pg_restore` command, with several options:
# 
# - `-c` (short for `--clean`) is for dropping database objects before recreating them.
# - `-d` (short for `--dbname`) is for restoring the data directly into the database used as argument (the `dvdrental` we created before).
# - `--no-owner`, because I was getting an error related to the user `postgres` (maybe the data dump was created with this user).
# 
# ```
# pg_restore -h localhost -U bob --no-owner -c -d dvdrental ./dvdrental.tar
# ```
# 
# > The command above will also run interactively, so that we can enter the **password** of `bob`.
# 
# ## Connecting to the New Database
# Now let's create a connection to the `dvdrental` database:

# In[1]:


import sqlalchemy
# Let's create a connection to the bobDB database for bob.
engine = sqlalchemy.create_engine('postgresql://bob:1234@localhost:5432/dvdrental')
engine.execution_options(isolation_level="AUTOCOMMIT")

# While we're at it, let's also load the `ipython-sql` extension
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', '$engine.url')


# > One thing I noticed about `sqlalchemy` is that once we create an engine for a database, we can't use it connect to another database. If we wanted to connect to another database, we should create an additional engine for it.
