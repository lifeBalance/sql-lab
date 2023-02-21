# SQL Lab
This is a setup for learning SQL with the help of Jupyter notebooks. The idea is to be able of executing SQL queries from the notebook against PostgreSQL, all running within a [Conda][1] virtual environment.

> The **original idea** was to run the MySQL service from within a Docker container, but couldn't make it work.

These notes assume the Conda package is installed in our system.

## Setting up the virtual environment
To create a virtual environment using Anaconda we run:
```
conda create --name sql-lab
```

Let's also create a folder to put the files (our database cluster and jupyter notebooks) we'll be using on this environment:
```
mkdir sql-lab
```

## Installing PostgreSQL
Since we want to install [PostgreSQL][2] in the **virtual environment**, first thing we want to do is **enable** it:
```
conda activate sql-lab
conda install postgresql
```

### Create a DB cluster
Now we have to [create a database cluster][3], which will generate a folder containing the data, so let's do that from within our ``sql-lab`` folder:
```
cd sql-lab
initdb -D bob_data
```

> A database cluster is a collection of databases that are managed by a single server instance.

### Starting the Service
Now we can start the ``postgres`` service (note that we have to use the [pg_ctl][4] with the ``-D`` option, passing the location of the cluster):
```
pg_ctl -D bob_data -l logfile start
```

> The ``-l logfile`` is, as you may have imagined, to log any incidence of the service into the ``logfile`` file.

### Creating a Superuser
To create users we use the [createuser][5] command:
```
createuser --encrypted -sP bob
```

In the command above we're using the options:

* ``--encrypted`` is obsolete but still accepted for backward compatibility.
* ``-s``, short for ``--superuser``.
* ``-P``, short for ``--pwprompt``, so that we'll be prompted for a password for the new user.

### Creating a Database
To create a database we must use the [createdb][6] command:
```
createdb --owner=bob bobDB
```

* The ``--owner`` option specifies the database user who will own the new database. 
* Note that we must give the **database name** as the last argument, in this case ``bobDB``.

### Testing new User and Database
In order to test the new user and database, we can use the [psql][7] command:
```
psql --username=bob --db=bobDBpsql --username=bob --db=bobDB
psql (12.9)
Type "help" for help.

bobDB=# 
```

> You can run commands in Jupyter Book cells by prepending them with ``!``. If you do it from the Jupyter Lab terminal, make sure you activate the conda virtual environment: ``conda activate db-lab``.

## Installing Jupyter Lab
For the Jupyter Lab with PostgreSQL set up, we'll be needing [Jupyter Lab][https://jupyter.org/] itself, and several dependencies. All the packages below should be installed in the Conda virtual environment, so make sure is activated.

* [jupyterlab](https://anaconda.org/conda-forge/jupyterlab).
* [theme-darcula](https://anaconda.org/conda-forge/theme-darcula), a cool theme for jupyter lab.
* [ipython-sql](https://anaconda.org/conda-forge/ipython-sql) to get SQL magic functions (``%sql``).
* [pgspecial](https://anaconda.org/conda-forge/pgspecial) so we can run Postgres **metacommands** (``\dt``).
* [sqlalchemy](https://anaconda.org/conda-forge/sqlalchemy) to create the connection to the database.

Just follow the instructions in the links above to install the packages.

Additionally, I installed:

* [jupyter-book](https://anaconda.org/conda-forge/jupyter-book), to create the book you're reading.
* [ghp-import](https://anaconda.org/conda-forge/ghp-import), to publish our book to GitHub.

## Launching the Lab
Once everything is installed, we can run:
```
jupyter lab
```

That will start a local server, where we can reach the Jupyter lab interface. In the next section, we'll go over how to create a connection to the database.

[1]: https://conda.io/projects/conda/en/latest/index.html
[2]: https://www.postgresql.org
[3]: https://www.postgresql.org/docs/15/app-initdb.html
[4]: https://www.postgresql.org/docs/15/app-pg-ctl.html
[5]: https://www.postgresql.org/docs/15/app-createuser.html
[6]: https://www.postgresql.org/docs/15/app-createdb.html
[7]: https://www.postgresql.org/docs/current/app-psql.html