from cryptography.fernet import Fernet

def encrypted(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    byte_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(byte_password)
    return encrypted_password.decode('ascii')

def decrypt(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    byte_password = bytes(password, 'ascii')
    decrypt_password = f.decrypt(byte_password)
    return decrypt_password.decode('ascii')
