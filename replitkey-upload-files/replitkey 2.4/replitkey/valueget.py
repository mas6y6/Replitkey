# Hey to You might went to see this.
# Just do not edit any code or the package will not work correctly
# @mas6y6 on github
import os

class URLError(Exception):
    pass
class KeyNotFound(Exception):
    pass
class Communicationerror(Exception):
    pass

def getlen(text):
  stop = 0
  len = 1
  name = text
  while stop == 0:
    try:
      a = name[len]
    except:
      stop = 1
    finally:
      len = len + 1
  return len

def remove_char(string, n):
    begin = string[:n]
    end = string[n+1:]
    return begin + end

def getdomain():
    return os.getenv("REPLIT_DB_URL")

class key:
    def __init__(self,URL):
        os.system("clear")
        print("Installing Requests Package")
        os.system("pip install requests")
        os.system("clear")
        import requests
        print(f"Attempting to connect to {URL} ...\n")
        try:
            requests.get(URL)
        except requests.exceptions.MissingSchema:
            raise URLError(f"""An Unknown Error Occurred. the process while connecting to {URL} has stopped Unexpectedly
                            
The URL may be invalid Did you Forget https://
                            
Error: 500""")
        except:
            raise Communicationerror(f"""An Unknown Error Occurred. the process while connecting to {URL} has stopped Unexpectedly more information below
                            
A Unknown Error Occurred
                            
Error: 500""")
        finally:
            print("Connected")
            print("Ready")
            self.URL = URL
            # Connects to Replit Server
    
    def __str__(self):
        return f"Connected to {self.URL} Replit Server"
        #This is the code that returns URL data
    
    def set(self,key,value):
        try:    
            os.system(f"curl {self.URL} -d '{key}={value}'")
        except:
            raise Communicationerror("Unknown error has occurred")
        finally:
            pass
        #This is the code that sets a key

    
    def get(self,key):
        try:
            os.system(f"curl {self.URL}/{key}")
        except:
            raise Communicationerror("Unknown error has occurred")
        finally:
            return os.system(f"curl {self.URL}/{key}")
        #This is the code that gets a key's value
    
    def delete(self,key):
        try:
            os.system(f"curl -XDELETE {self.URL}/{key}")
        except:
            raise Communicationerror("Unknown error has occurred")
        finally:
            pass
        #This is the code that delates a key
    
    def list(self,key):
        try:
            value = os.system(f'curl "{self.URL}?prefix={key}"')
        except:
            raise Communicationerror("Unknown error has occurred")
        finally:
            return value
        #This is the code that lists key's