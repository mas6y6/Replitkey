# Hey to You might went to see this.
# Just do not edit any code or the package will not work correctly
# @mas6y6 on github


import os
import requests
def remove_char(string, n):
    begin = string[:n]
    end = string[n+1:]
    return begin + end
class key:
    def __init__(self,URL):
        os.system("pip install requests")
        os.system("clear")
        print(f"Attempting to connect to {URL}")
        try:
            requests.get(URL)
        except:
            raise TypeError("UNABLE TO CONNECT TO A REPLIT SERVER URL BE HAVE A ERROR OR NOT TYPED IN CORRECTLY")
        finally:
            print("Connected")
            self.URL = URL
        # Connects to Replit Server
    
    def __str__(self):
        return f"Connected to {self.URL} Replit Server"
    #This is the code that returns URL data
    
    def set(self,key,value):
        os.system(f"curl {self.URL} -d '{key}={value}'")
    #This is the code that sets a key

    
    def get(self,key):
        value = os.system(f"curl {self.URL}/{key}")
        return value
    #This is the code that gets a key's value
    
    def delete(self,key):
        os.system(f"curl -XDELETE {self.URL}/{key}")
        #This is the code that delates a key
    
    def list(self,key):
        return os.system(f'curl "{self.URL}?prefix={key}"')
    #This is the code that lists key's