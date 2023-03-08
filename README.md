# SQL Lab
This is a Jupyter book to practice [SQL][1] interactively.

> You can reach the published version of the book [here][2].

In order to play around with queries you have to get the lab up and running by:

- Starting the Docker services (``postgres`` and ``pgadmin``).
- Start Jupyter Lab.

## Dependencies
The set up has the following dependencies:

- Docker (where we run a ``postgres`` and ``pgadmin`` containers as services).
- [Conda][3] (where we run Jupyter Lab).

## Start Jupyter Lab Environment
Before starting the lab, make sure to [activate the environment][4]:
```
conda activate sql-lab
```

For the command above to work, we should have created the ``sql-lab`` environment beforehand.

> If you don't remember if the environment already exists, you can run ``conda env list``.

The instructions above assume you have created a [Conda environment][5] and install its dependencies, if that's not the case, read the next section.

### Recreate Jupyter Lab Environment
Once you've cloned this repo, you may want to recreate the environment:
```
conda env create -f environment.yml
```

> The ``environment.yml`` file is included in this repo; it was created with ``conda env export > environment.yml``.

If you want to **remove** the environment:
```
conda env remove -n sql-lab
```

## Start Docker Services
To easily start both the ``postgres`` and the ``pgadmin`` services we've created a couple targets in the ``Makefile``:
```
make dbUp
```

### Create PGAdmin Connection
To create a PGAdmin connection we have to use (under the **Connection** tab):

- **Host name/address**: ``postgres`` (the name of the Docker service)
- **Maintenance database**: ``postgres``
- **Username**: ``bob``
- **Password**: ``1234``

<!-- links -->
[1]: https://en.wikipedia.org/wiki/SQL
[2]: https://lifebalance.github.io/sql-lab/README.html
[3]: https://docs.conda.io/en/latest/
[4]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment
[5]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
