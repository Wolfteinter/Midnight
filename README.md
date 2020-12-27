# Midnight

This is a project developed in python, using flask framework

# How to up the project

You need:

* [Docker](https://www.docker.com/get-started)
* [Docker compose](https://docs.docker.com/compose/install/)


### Commands for start

When you already have all requirements you need do a fork in your repository you need clone in your Document folder, or where you want.

You use this command for up the containers:
`$ docker-compose up`.
This command show all proccess which container makes, if you dont want see them and run on backgrown run the next command:
`$ docker-compose up -d`.

For run flask application you go inside of container `midnight_flask` follow the next command:

`$ docker exec -it midnight_flask bash`

If the first time to upload the project maybe you need run the migrations
`root@midnight_flask:/src# flask db upgrade`

now you can run flask:
`root@midnight_flask:/src# flask run --host=0.0.0.0`

Access to:
[localhost](http://localhost)


# Command for update migrations

If you change some field on a any Model you should run the next command:
You first run this command before to apply this change on database 
`root@midnight_flask:/src# flask db migrate`
When the proccess finish correctly you can run 
`root@midnight_flask:/src# flask db upgrade`
