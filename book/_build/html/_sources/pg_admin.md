# pgAdmin
[pgAdmin][1] is a very popular GUI for [PostgreSQL][2] administration.

## Logging In
Once the Docker services (`postgres` and `pgadmin`) have started, we can point our browser to http://localhost:8080 and log in, using the **username** and **password** we set in our `compose-postgres.yml` file:

![log in into pgadmin](/images/login.png)

## Creating a Server
First thing we have to do once we've logged in, it's to create a server, which we can do from the **dashboard**:

![create a server](/images/add_server.png)

We have to choose a name for our server (whatever we want):

![server name](/images/server_name.png)

And also specify the details for our connection, i.e.:

* **Host name**, in this case the name of the service in our Docker compose file.
* **Maintenance database, we can choose the default, `postgres`.
* **Username**, also in the Docker compose file.
* **Password**, ditto.

![connection](/images/connection.png)

## Running SQL Queries
Even though we'll be running most of our SQL within Jupyter notebooks, we could also use **pgAdmin** for that. We just have to **right click** on any existing database, and select the **query tool**:

![query tool](/images/query_tool.png)

That would open a window like in the image below. We can just write our SQL queries in the window, and run them by pressing **F5**. 

![query example](/images/query_example.png)

All the queries we run are saved into a **Query History**, in case we want to use them again.

[1]: https://www.pgadmin.org/
[2]: https://www.postgresql.org