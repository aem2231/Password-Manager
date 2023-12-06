import os
from cryptography.fernet import Fernet
import manager
import json

class Config():
    def __init__(self):
        self.encryptionKeyFilePath = "data/encryptionKey.txt"
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
            with open(self.encryptionKeyFilePath, "wb") as f:
                f.write(encryptionKey)
        return encryptionKey
    
    def loadKey(self):
        with open(self.encryptionKeyFilePath, "rb"):
            return open(self.encryptionKeyFilePath, "rb").read()
                
    def getMasterPassword(self):
        fernet = Fernet(self.loadKey())
        if os.path.exists(self.masterPasswordFilePath):
            with open(self.masterPasswordFilePath) as f:
                encryptedPassword = f.read()
                masterPassword = fernet.decrypt(encryptedPassword)
                masterPassword = masterPassword.decode()
                attempts = 0
                passwordAttempt = ""
                while passwordAttempt != masterPassword:
                    attempts+=1
                    if attempts < 5:
                        passwordAttempt = str(input(f"[Attempt {attempts}/5]\nEnter your master Password: "))
                    elif attempts == 5:
                        print("Final attempt!")
                        passwordAttempt = str(input("Enter your master Password: "))
                    if passwordAttempt == masterPassword:
                        print("Master Password Correct!")
        else:
            with open(self.masterPasswordFilePath, "wb") as f:
                masterPassword = str(input("Please choose a master Password: "))
                masterPassword = masterPassword.encode()
                encryptedPassword = fernet.encrypt(masterPassword)
                f.write(encryptedPassword)
                print("Master Password Created!")
                Config().getMasterPassword()

def main():                        
    config = Config()
    config.getKey()
    config.getMasterPassword()
    manager.manager()
    
main()