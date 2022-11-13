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

# How to getKeys setKeys etc... with a object `database.get("Key"),database.set("Key","Value / Text") database.delate("Key") database.list("Key")`

**Setup Key `database.set()`**

The Key can Be Set as new OR Set a existing key
```python3

```
