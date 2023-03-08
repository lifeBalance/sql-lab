# SQL Lab
This is a setup for learning SQL with the help of [Jupyter][1] notebooks. The idea is to be able of executing SQL queries from the notebook against a [PostgreSQL][2] server. We need two ingredients to make this happen:

- Jupyter Lab, which will be running within a [Conda][4] virtual environment.
- A [PostgreSQL][1] server and [pgadmin][2], which will be running in Docker containers.

The **original idea** was to run PostgreSQL from within the Conda environment, but couldn't make it work. Packages installed in such an environment, can't work as system services, so I could only reach them from within the environment; they weren't available when trying to reach them from, for example, [pgadmin][3] running in a Docker container.

## Setting up the virtual environment
To create a virtual environment using Anaconda we run:
```
conda create --name sql-lab
```

> These notes assume the [Conda][4] package is [installed](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) in our system.

Let's also create a folder to put the files (our database cluster and jupyter notebooks) we'll be using on this environment:
```
mkdir sql-lab
```

## Installing Jupyter Lab
For the Jupyter Lab with PostgreSQL set up, we'll be needing [Jupyter Lab](https://jupyter.org/) itself, and several dependencies. All the packages below should be installed in the Conda virtual environment, so make sure is activated.

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

## Launching Postgres and PgAdmin
In order to launch Postgres and PgAdmin I wrote a couple targets in a `Makefile`. Check the `compose-postgres.yml` as well, to get familiar with both services.

> Something **weird** I experienced when creating connections to Postgres, was that I had to use ``localhost`` and not the name of the Docker service (``postgres``) in order to create connections to the database 🤔.

[1]: https://jupyter.org/
[2]: https://www.postgresql.org
[3]: https://www.pgadmin.org/
[4]: https://conda.io/projects/conda/en/latest/index.html
