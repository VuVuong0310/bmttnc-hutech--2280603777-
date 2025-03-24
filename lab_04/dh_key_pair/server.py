from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Tạo tham số Diffie-Hellman
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

# Tạo cặp khóa cho server
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # Bước 1: Tạo tham số DH
    parameters = generate_dh_parameters()

    # Bước 2: Tạo cặp khóa DH
    private_key, public_key = generate_server_key_pair(parameters)

    # Bước 3: Lưu khóa công khai của server vào file
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Server public key has been saved to 'server_public_key.pem'.")

if __name__ == "__main__":
    main()
