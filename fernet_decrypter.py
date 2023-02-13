import glob
from cryptography.fernet import Fernet


# Read the key from the key file
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet object using the key
fernet = Fernet(key)

# checking if the user has the secret phrase to decrypt Files
phrase = input("Enter your Secret-Phrase to Gain Access: ")
with open("key.key", "rt") as key_file:
    secretphrase = key_file.readlines()[1]
    if phrase == secretphrase:
    
        # Decrypt all files in the current directory
        for file in glob.glob("*"):
            if not (file.endswith("encrypter.py") or file.endswith(".key") or file.endswith("decrypter.py") or file.endswith("generator.py")):
                
                # Read the contents of the encrypted file
                with open(file, "rb") as f:
                    encrypted_data = f.read()

                # Decrypt the data
                data = fernet.decrypt(encrypted_data)

                # Write the decrypted data to a new file
                with open(file, "wb") as f:
                    f.write(data)
    else:
        print("Wrong Secret Phrase. Try Again.")
