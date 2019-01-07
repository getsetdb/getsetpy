# getsetpy
Python connector for GetSetDB with official support.

Some familiarity with GetSetDB would come a long way in using getsetpy as most of the API calls by the `space.Space` and `database.Database` inter-actors comes directly from it. To learn GetSetDB, refer to [A Tour of GetSetDB](https://medium.com/@mentix02/a-tour-of-getsetdb-8716c39e354d)

## Installation
```sh
$ pip install getsetpy
```

## Usage

getsetpy provides an interface to GetSetDB by using inter-actors that provide a similar and easy to use API for sending commands to the Space or a particular Database.

### Space API
To run Space commands, use the `space.Space` inter-actor - 

```python
from getsetpy.space import Space

space = Space()
databases = space.ls() # returns list of all databases

space.new('users') # creates a new database
space.delete('old_database') # deletes an old database

space.rename('users', 'people') # renames 'user' database to 'people'

commands = space.commands() # returns a list of commands for "space"

```

### Database API
To run commands for a specific Database, use the `database.Database` inter-actor - 

```python
from getsetpy.database import Database

# connects to the 'users' database
users = Database('users') 
# if it does not exist, it raises a DatabaseNotFound exception

# returns a dictionary with all the user keys as values and a redundant number as the key
users = users.all() 
# returns an empty dictionary if no pairs are found
# but if the users database was populated like this - 
# manan : yadav
# bruce : wayne
# martha : stewart
# kunal : pahuja
# peter : parker
# donald : trump
# barry : allen
# sheldon : cooper
# then the dictionary would look like
# {1.0: 'manan', 2.0: 'bruce', 3.0: 'martha', 4.0: 'kunal', 5.0: 'peter', 6.0: 'donald', 7.0: 'barry', 8.0: 'sheldon'}

# deletes the pair - donald : trump to database 'users'
users.delete('donald')

# gets the value for key 'barry'
users.get('barry')
# 'allen'

# adds the pair - wonder : woman to database 'users'
users.set('wonder', 'woman')

# returns a dictionary containg info about the database 'users'
# like its size in bytes and the path to its file
users.info()
# {'size': '136 bytes', 'path': '/tmp/gsdb/users.gsdb'}

# returns the number of pairs in the 'users' database
users.count()
# 8

```
