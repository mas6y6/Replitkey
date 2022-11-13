# Replitkey
Replitkey is for connection from a local device to a online replit database server
#How to install

Type this command into your shell or terminal
```
pip install replitkey
```
**OR**

Type this on the very top of your Python program
```python
import os

os.system("pip install replitkey")
```

# Connect to a REPLIT Database`replitkey.key()`
To connect yo a database its to type this into your repl
```python
import os

print(os.getenv("REPLIT_DB_URL")) # Note the input NEEDS to be the same Don’t remove "REPLIT_DB_URL"
```
Once the URL appears Copy it the URL it the Getaway to the Repl's database

Type this into the local python program

```python
import replitkey

DATABASE = replitkey.key("URL") # Replace the Input with the URL that you Copyed
```
Once thats done then you are connected

# How to getKeys setKeys etc... with a object `database.get("Key"), etc...`

**Set Key `database.set()`**

The Key can Be Set as new OR Set a existing key
```python
database.set("Key","Value/text")
```

**Get a keysvalue`database.get()`
To key's get a value, type this into your local python project

Note note on the replit server it displays the actual value but on local displays the actual value but follows of a unknown character

```python
database.get("Key")
```

**Delate a Key`database.delete()`**

To delete a Key, type this into your local python project
```python
database.delete("Key")
```

**List key`database.list()`**

To list a Key, type this into your local python project

Note i dont know what this does but I had to add it.

```python
database.list("Key")
```

# Update Replitkey `Shell`

type this into your terminal or Shell

Note, make sure that you're always in the latest version replit can update the database as well.

```
pip install replitkey --upgrade
```

This will update the replitkey module

# Who wrote this?

**mas6y6**
@mas6y6 on scratch

@mas6y6 on replit

@mas6y6 on github

@mas6y6 on pypi
