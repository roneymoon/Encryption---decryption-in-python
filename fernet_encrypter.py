import glob
from cryptography.fernet import Fernet

# creating a Encrypting secret phrase
secret_phrase = input("Create a secret Phrase (to decrypt later): ").lower()

# Generate a key and store it in a file
key = Fernet.generate_key()

# writing the key down to the key.key file
with open("key.key", "wb") as key_file:
    key_file.write(key)

# writing the secret_phrase to the key.key file
with open("key.key", "a") as key_file:
    key_file.write("\n" + secret_phrase)

# Read the key from the file
with open("key.key", "rb") as key_file:
    keyvalue = key_file.readlines()[0]

# Initialize the Fernet object using the key
fernet = Fernet(keyvalue)

# Encrypt all files in the current directory except .py files
for file in glob.glob("*"):
    if not (file.endswith("encrypter.py") or file.endswith(".key") or file.endswith("decrypter.py")) or file.endswith("txt_files_generator.py") :
        with open(file, "rb") as f:
            # Read the contents of the file
            data = f.read()

        # Encrypt the data
        encrypted_data = fernet.encrypt(data)

        # Write the encrypted data to a new file
        with open(file, "wb") as f:
            f.write(encrypted_data)