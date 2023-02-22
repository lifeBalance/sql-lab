# Installing PostgreSQL
One of the things I tried when working on this setup, was to install [PostgreSQL][2] in the **system**, which in my case was **Fedora 37**. I followed instructions from [here](https://developer.fedoraproject.org/tech/database/postgresql/about.html):
```
sudo dnf install postgresql postgresql-server
```

Next, initialize [the cluster][3], which will generate a folder containing the data:
```
sudo postgresql-setup --initdb --unit postgresql
* Initializing database in '/var/lib/pgsql/data'
* Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log
```

> A **database cluster** is a collection of databases that are managed by a **single server** instance.

Then, start the service:
```
sudo systemctl start postgresql
```

> To check the status of the service at any point in time, we'd do ``sudo systemctl status postgresql``.

## Login into Postgres
The Postgres installation process creates a new user named `postgres`. But if we try to log in using this user:
```
psql -U postgres
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "postgres"
```

That error happens because the ``postgres`` user doesn't have a password. In order to create one, we can substitute our current user for ``postgres``:
```
sudo su postgres
```

Note that we can log into Postgres without using a password:
```
psql -U postgres
postgres=# \q
```

## Create a New User
To add a new user we have to substitute our current user for ``postgres``:
```
sudo su postgres
```

And use the [createuser][5] command:
```
$ createuser bob -P
Enter password for new role: 
Enter it again:
```

## Edit the ``pg_hba.conf`` File
Now we have to edit the [pg_hba.conf][https://www.postgresql.org/docs/15/auth-pg-hba-conf.html] file:
```
sudo nvim /var/lib/pgsql/data/pg_hba.conf
```

> You can locate this file in the same directory where the database cluster was generated.

And add the following line:
```
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             bob                                     md5
```

> Make sure you change ``peer`` by ``md5``. Peer authentication means that the connection is only allowed if the name of the database user is the same as the name of the operating system user.

Now we can finally log in with using ``bob`` and his password.
```
psql -U bob -d postgres
Password for user bob: 
psql (14.3)
Type "help" for help.

postgres=>
```

## Creating a Superuser
To create users we use the [createuser][5] command:
```
createuser --encrypted -sP bob
```

In the command above we're using the options:

* ``--encrypted`` is obsolete but still accepted for backward compatibility.
* ``-s``, short for ``--superuser``.
* ``-P``, short for ``--pwprompt``, so that we'll be prompted for a password for the new user.

## Creating a Database
To create a database we must use the [createdb][6] command:
```
createdb --owner=bob bobDB
```

* The ``--owner`` option specifies the database user who will own the new database. 
* Note that we must give the **database name** as the last argument, in this case ``bobDB``.

## Testing new User and Database
In order to test the new user and database, we can use the [psql][7] command:
```
psql --username=bob --db=bobDBpsql --username=bob --db=bobDB
psql (12.9)
Type "help" for help.

bobDB=# 
```

> You can run commands in Jupyter Book cells by prepending them with ``!``. If you do it from the Jupyter Lab terminal, make sure you activate the conda virtual environment: ``conda activate db-lab``.


[1]: https://jupyter.org/
[2]: https://www.postgresql.org
[3]: https://www.pgadmin.org/
[4]: https://conda.io/projects/conda/en/latest/index.html

[3]: https://www.postgresql.org/docs/15/app-initdb.html
[4]: https://www.postgresql.org/docs/15/app-pg-ctl.html
[5]: https://www.postgresql.org/docs/15/app-createuser.html
[6]: https://www.postgresql.org/docs/15/app-createdb.html
[7]: https://www.postgresql.org/docs/current/app-psql.html