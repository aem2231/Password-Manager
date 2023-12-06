from cryptography.fernet import Fernet
import json

class Main():
    def __init__(self):
        self.encryptionKeyFilePath = "data/encryptionKey.txt"
        self.passwords = "data/passwords.json"
        self.template = {
            "ACCOUNT": "",
            "USERNAME": "",
            "PASSWORD": "",
        }
        

    def addPassword(self):
        with open(self.encryptionKeyFilePath) as f:
            key = f.read()
        fernet = Fernet(key)
        
        account = str(input("Enter Account: "))       
        with open(self.passwords, "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
                
            sameAccounts = sum(1 for item in data if item["ACCOUNT"] == account)
            if sameAccounts > 0:
                choice = " "
                while choice.lower()!= "y" and choice.lower()!= "n":
                    choice = input(f"Account {account} already exists.\nUse {account + str(sameAccounts)} instead? [y/n]? ")
                    if choice == "y":
                        account = account + str(sameAccounts)
                    else:
                        self.addPassword()
                    
        username = str(input("Enter Username: "))
        password = str(input("Enter Password: "))
        encodedUsername = username.encode()
        encodedPassword = password.encode()
        encryptedUsername = fernet.encrypt(encodedUsername)
        encryptedPassword = fernet.encrypt(encodedPassword)
        data = self.template.copy()
        data["ACCOUNT"] = str(account)
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