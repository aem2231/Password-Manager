import os
from cryptography.fernet import Fernet
import json

class Main():
    def __init__(self):
        self.encryptionKeyFilePath = "data/encryptionKey.txt"
        self.passwords = "data/passwords.json"
        self.template = {
            "USERNAME": "",
            "PASSWORD": "",
        }
        
    def addPassword(self):
        with open(self.encryptionKeyFilePath) as f:
            key = f.read()
        fernet = Fernet(key)
        
        username = str(input("Enter Username: "))
        password = str(input("Enter Password: "))
        encodedUsername = username.encode()
        encodedPassword = password.encode()
        encryptedUsername = fernet.encrypt(encodedUsername)
        encryptedPassword = fernet.encrypt(encodedPassword)
        data = self.template.copy()
        data["USERNAME"] = str(encryptedUsername)
        data["PASSWORD"] = str(encryptedPassword)
        try: 
            with open(self.passwords, "r") as f:
                existingData = json.load(f)
        except:
            existingData = []
        existingData.append(data)
        print(existingData)
        with open(self.passwords, "w") as f:
            json.dump(existingData, f, indent=4)
        print("Password Added!")

def manager():
    instance = Main()
    instance.addPassword()