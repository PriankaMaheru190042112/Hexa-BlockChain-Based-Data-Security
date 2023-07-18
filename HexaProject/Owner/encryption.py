from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    
    plaintext = file_path.read()
    print("File Path :",file_path)

    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(plaintext)
    encrypted_file_path = 'media/documents/'+str(file_path) + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)

    print(f"File '{file_path}' encrypted successfully. Encrypted file saved as '{encrypted_file_path}'.")

    return encrypted_file_path




def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        ciphertext = encrypted_file.read()

    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext)

    decrypted_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
    idx = 0
    for i in range(len(decrypted_file_path)-1,0,-1):
        if decrypted_file_path[i]=='/':
            idx=i 
            break 
    decrypted_file_path = 'media/ReadOnlyDocument/'+decrypted_file_path[idx+1:]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

    print(f"File '{encrypted_file_path}' decrypted successfully. Decrypted file saved as '{decrypted_file_path}'.")

    return decrypted_file_path