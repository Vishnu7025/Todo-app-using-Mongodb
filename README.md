
# Todo app
 ### I made this Todo app to learn Django integration with MongoDB




## 🚀 About Me
I’m a Python | Django developer based in Trivandrum, Kerala, curious to learn more about developing scalable distributed systems, loves problem solving and cares about writing readable as well as maintainable code.


## Connect Django to MongoDB

 ### There are three ways to connect Django to MongoDB:
-  **PyMongo**: PyMongo is the standard driver through which MongoDB can interact with Django.
     It is the official and preferred way of using MongoDB with Python. PyMongo provides functionality 
     to perform all the database actions like search, delete, update, and insert. Since PyMongo is available with PyPI,
     you can quickly install it using a pip command.
- **MongoEngine**: MongoEngine is a Python Object-Document-Mapper. It’s similar to Object-Relational-Mapper
  in relational databases. MongoEngine has a declarative API that is easy to learn and use.
- **Djongo**: If you are using a relational database like SQL and want to migrate to MongoDB, 
   for that you can use Djongo. Without changing the Django ORM, Djongo transpiles all the
   SQL queries to MongoDB syntax queries.
## Integration
I am using Djongo becauase it is the easiest way to integrate with Django.

you can also use other two method visit the below link:
https://www.mongodb.com/compatibility/mongodb-and-django

 First install Djongo:

      pip install djongo

##### Now, go to your project folder (example, MyFirstDjangoProj), and open settings.py file. You can edit it on   IDE,
or any editor. Search for DATABASES, and change the settings to point to MongoDB. The ENGINE will be djongo and the database name (NAME)
will be your MongoDB database name.

**DATABASES = {**

       'default': {
           'ENGINE': 'djongo',
           'NAME': 'db-name',
       }
    }

###### If your database is not on localhost or is secured, you should also fill in the CLIENT information like HOST, USERNAME, PASSWORD, etc.


**DATABASES = {**

        'default': {
            'ENGINE': 'djongo',
            'NAME': 'your-db-name',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
            }  
        }
    }

##### Now that we have the Django project (and app), you can create the collections in MongoDB using the commands:

     python manage.py makemigrations

### if you are seeing this type of error

**django.core.exceptions.ImproperlyConfigured: 'djongo' isn't an available database backend or couldn't be imported. Check the above exception.
To use one of the built-in backends, use 'django.db.backends.XXX', where XXX is one of:\
'mysql', 'oracle', 'postgresql', 'sqlite3'**

install below library to solve this error:

     pip install pytz==2022.2.1   


#### After installing this library the error changed to:
**NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None**

install below library to solve this error:

    pip install pymongo==3.12.3.  

## After doing all this installation you can successfully migrate all the datas into your MongoDB database.
## Screenshots



![Screenshot (31)](https://user-images.githubusercontent.com/105106551/191688527-c6294ef5-7d51-4c11-ba5f-f51b96e0037d.png)

