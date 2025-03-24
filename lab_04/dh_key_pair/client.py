from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Tạo cặp khóa DH cho client
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Tạo khóa bí mật chia sẻ từ khóa riêng của client & khóa công khai của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Bước 1: Load khóa công khai của server từ file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Bước 2: Lấy tham số DH từ khóa công khai của server
    parameters = server_public_key.parameters()

    # Bước 3: Tạo cặp khóa DH cho client
    private_key, public_key = generate_client_key_pair(parameters)

    # Bước 4: Tạo khóa bí mật chia sẻ
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
