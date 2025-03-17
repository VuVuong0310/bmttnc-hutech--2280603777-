import ecdsa
import os

# Create directory if it doesn't exist
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Generate private key (Signing Key)
        sk = ecdsa.SigningKey.generate()

        # Generate public key (Verifying Key)
        vk = sk.get_verifying_key()

        # Save the private key to a PEM file
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Save the public key to a PEM file
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load the private key from a PEM file
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Load the public key from a PEM file
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        # Load keys and get only the public key for verification
        _, vk = self.load_keys()

        try:
            # Verify the signature using the public key (vk)
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            # Return False if the signature is invalid
            return False
