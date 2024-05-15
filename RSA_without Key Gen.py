import rsa
import time


def measure_rsa_operations_with_file(key_sizes, message_file="message.txt"):
    # Read the message from file
    with open(message_file, "r") as file:
        message = file.read()

    for size in key_sizes:
        print(f"\nTesting with key size: {size} bits")

        # Load the keys from files
        public_key_filename = f"public_key_{size}.pem"
        private_key_filename = f"private_key_{size}.pem"

        with open(public_key_filename, 'rb') as pub_file:
            publicKey = rsa.PublicKey.load_pkcs1(pub_file.read())

        with open(private_key_filename, 'rb') as priv_file:
            privateKey = rsa.PrivateKey.load_pkcs1(priv_file.read())

        print(f"Public and private keys loaded from '{public_key_filename}' and '{private_key_filename}'")

        # Measure encryption time
        start_time = time.time()
        encrypted_message = rsa.encrypt(message.encode(), publicKey)
        encryption_time = time.time() - start_time
        print(f"Encryption time: {encryption_time:.4f} seconds")

        # Measure decryption time
        start_time = time.time()
        decrypted_message = rsa.decrypt(encrypted_message, privateKey).decode()
        decryption_time = time.time() - start_time
        print(f"Decryption time: {decryption_time:.4f} seconds")

        # Ensure the message is the same
        assert message == decrypted_message, "Original and decrypted messages do not match!"


# Key sizes to test
key_sizes = [1024, 2048, 3072, 4076, 7680, 15360]

# Run the measurement
measure_rsa_operations_with_file(key_sizes)
