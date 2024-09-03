from cryptography.fernet import Fernet


class Criptografo():
    def __init__(self, clave):
        self.clave=clave
    def generate_key(self,clave):
        key = Fernet.generate_key()
        with open(f"{clave}.key", "wb") as key_file:
            key_file.write(key)
    def load_key(self, clave):
        return open(f"{clave}.key", "rb").read()

    def encrypt_file(self,file_name):
        key = self.load_key(self.clave)
        fernet = Fernet(key)
        with open(file_name, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(f"{file_name}.encrypted", "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(self,encrypted_file_name):
        key = self.load_key(self.clave)
        fernet = Fernet(key)
        with open(encrypted_file_name, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(f"{encrypted_file_name}.decrypted", "wb") as file:
            file.write(decrypted_data)
            


  