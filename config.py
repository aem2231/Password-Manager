import string
import os
import json
from cryptography.fernet import Fernet

class Config():
    def __init__(self):
        self.encryptionKeyFilePath = "data/encryptionKey.txt"
        self.passwordFilePath = "data/passwords"
        self.masterPasswordFilePath = "data/masterPassword.txt"
        self.passwords = "data/passwords.json"
        
    def getKey(self):        
        if not os.path.exists("data"):
            os.makedirs("data")
        
        if os.path.exists(self.encryptionKeyFilePath):
            with open(self.encryptionKeyFilePath) as f:
                encryptionKey = f.read()
        else:
            encryptionKey = Fernet.generate_key()
            with open(self.encryptionKeyFilePath, "w") as f:
                f.write(encryptionKey)
                
    def getMasterPassword(self):
        if os.path.exists(self.masterPasswordFileFilePath):
            with open(self.masterPasswordFilePath) as f:
                masterPassword = f.read()
                attempts = 0
                passwordAttempt = ""
                while passwordAttempt!= masterPassword:
                    attempts+=1
                    if attempts < 5:
                        attempt = str(input(f"[Attempt {attempt}/5]\nEnter your master Password: "))
                    elif attempts == 5:
                        print("Final attempt!")
                        attempt = str(input("Enter your master Password: "))
                    if attempt == masterPassword:
                        print("Master Password Correct!")
                    
  
                    
                
    