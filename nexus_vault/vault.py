import os
import shutil
from .crypto import CryptoManager

class NexusVault:
    """Core logic for managing encrypted files."""
    
    def __init__(self, master_password: str):
        self.password = master_password

    def lock_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'rb') as f:
            data = f.read()
        
        crypto = CryptoManager(self.password)
        encrypted_data = crypto.encrypt(data)
        
        # Save salt + encrypted data
        with open(file_path + ".nvlt", 'wb') as f:
            f.write(crypto.salt)
            f.write(encrypted_data)
        
        os.remove(file_path)

    def unlock_file(self, vault_path: str):
        if not vault_path.endswith(".nvlt"):
            raise ValueError("Invalid vault file format.")
            
        with open(vault_path, 'rb') as f:
            salt = f.read(16)
            encrypted_data = f.read()
        
        crypto = CryptoManager(self.password, salt)
        decrypted_data = crypto.decrypt(encrypted_data)
        
        original_path = vault_path[:-5]
        with open(original_path, 'wb') as f:
            f.write(decrypted_data)
            
        os.remove(vault_path)
