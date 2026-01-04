Title: Install a Maria DB instance with Docker
Date: 2026-01-03.
Summary: Setup Maria DB with Docker 

Quick instructions to set up a Maria DB instance. 

### Install and run

Retrieve the Docker image using

```console
sudo docker pull mariadb
```
Start the docker image my mounting a local directory to where the datbase will be stored to the `/var/lib/mysql` directory.

```console
sudo docker run --name mariadb-container -e MARIADB_ROOT_PASSWORD=my_very_complicated_password -p 3306:3306 -v ~/mysql:/var/lib/mysql -d mariadb:latest
```

For more detailed instructions, look at this [tutorial](https://www.bytebase.com/reference/mariadb/how-to/how-to-install-mariadb-using-docker/).

### Add tables and users

To connect as root to the database, tap into the Docker image
```console
sudo docker exec -it  mariadb-container /bin/bash
```
and call `mariadb --password`.

Start with creating a database. 
Call the `CREATE_DATABASE` method as explained [here](https://mariadb.com/kb/en/create-database/).
After creating the database `mydb`, switch to this database by typing
```console
use mydb
```
Create a table following the examples in [this page](https://www.mariadbtutorial.com/mariadb-basics/mariadb-create-table/).

Create users and grant privileges using 
```console
CREATE USER tintin IDENTIFIED BY 'my_password';
GRANT ALL ON `mydb`.* TO tintin;
```
See more examples [here](https://www.daniloaz.com/en/how-to-create-a-user-in-mysql-mariadb-and-grant-permissions-on-a-specific-database/).

### Local client
To test the database, you can install this client in ubuntu:
```console
sudo apt install mariadb-client
```
and test your connection for the newly created user with
```console
mariadb --user tintin --password --port 3306
```