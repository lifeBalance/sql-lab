# SQL Lab
To get the lab up and running you have to:

- Start the Docker services.
- Start Jupyter Lab.

## Dependencies
The set up has the following dependencies:

- Docker.
- Conda.

## Recreate Jupyter Lab Environment
Once you've cloned this repo, you may want to recreate the environment:
```
conda env create -f environment.yml
```

> The ``environment.yml`` file is included in this repo; it was created with ``conda env export > environment.yml``.

If you want to **remove** the environment:
```
conda env remove -n sql-lab
```

## Start Jupyter Lab Environment
Before starting the lab, make sure the environment is enabled:
```
conda activate sql-lab
```

For the command above to work, we should have created the ``sql-lab`` environment beforehand.

> If you don't remember if the environment already exists, you can run ``conda env list``.

## Docker Services
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