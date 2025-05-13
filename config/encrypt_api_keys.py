from cryptography.fernet import Fernet

# Generate a key and save it if not exists
def generate_key():
    key = Fernet.generate_key()
    with open("config/secret.key", "wb") as key_file:
        key_file.write(key)

# Encrypt API keys
def encrypt_api_key(api_key):
    with open("config/secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    encrypted_key = fernet.encrypt(api_key.encode())
    return encrypted_key

if __name__ == "__main__":
    generate_key()
    sample_key = "your_api_key_here"
    encrypted = encrypt_api_key(sample_key)
    print(f"Encrypted API Key: {encrypted}")