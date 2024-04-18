## To Connect to Postgresdatabase from terminal, use the command:
```psql -h public-server-ip -p 5432 -U postgres -W```


## How to specify the django database connection in settings.py to use for running migrations:

In Django, you can specify the database connection to use for running migrations by utilizing the --database option with the manage.py command. This allows you to target specific databases configured in your settings.py file. Here's how you can do it:

```python manage.py migrate --database=<database_alias>``` E.g. 
```py manage.py migrate --database=pgConnect```

To make migrations for a single/specific application, use the sample command below:
```py manage.py makemigrations poll --database=pgConnect```

After making the migrations, to actually <b>SEE</b> the output of migrations that would be created against specfic db, use the below command:
```python manage.py sqlmigrate <app_name> 0001 --database=<database_alias>``` 
E.g ```py manage.py sqlmigrate poll 0001 --database=pgConnect```

#### The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

- If you’re interested, you can also run ```python manage.py check```; this checks for any problems in your project without making migrations or touching the database.

- Now, run migrate again to create those model tables in your database:
```py manage.py migrate --database=pgConnect```

Creating an admin user¶
First we’ll need to create a user who can login to the admin site. Run the following command:

```py manage.py createsuperuser```
