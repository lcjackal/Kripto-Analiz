import json
from cryptography.fernet import Fernet

class Security:
    def __init__(self, key_file="config/secret.key"):
        self.key_file = key_file
        self.key = self.load_key()

    def load_key(self):
        try:
            with open(self.key_file, "rb") as file:
                return file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as file:
                file.write(key)
            return key

    def encrypt(self, data):
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode()).decode()

    def decrypt(self, token):
        fernet = Fernet(self.key)
        return fernet.decrypt(token.encode()).decode()

    def save_api_keys(self, keys, file_path="config/api_keys.json"):
        encrypted_keys = {k: self.encrypt(v) for k, v in keys.items()}
        with open(file_path, "w") as file:
            json.dump(encrypted_keys, file)

    def load_api_keys(self, file_path="config/api_keys.json"):
        try:
            with open(file_path, "r") as file:
                encrypted_keys = json.load(file)
                return {k: self.decrypt(v) for k, v in encrypted_keys.items()}
        except FileNotFoundError:
            return {}