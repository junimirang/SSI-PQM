import rsa
import time


def measure_rsa_operations_with_file(key_sizes, message_file="message.txt"):
    # Read the message from file
    with open(message_file, "r") as file:
        message = file.read()

    for size in key_sizes:
        print(f"\nTesting with key size: {size} bits")

        # Measure key generation time
        start_time = time.time()
        publicKey, privateKey = rsa.newkeys(size)
        key_gen_time = time.time() - start_time
        print(f"Key generation time: {key_gen_time:.4f} seconds")

        # Save the keys with _[keysize] suffix
        public_key_filename = f"public_key_{size}.pem"
        private_key_filename = f"private_key_{size}.pem"

        with open(public_key_filename, 'wb') as pub_file:
            pub_file.write(publicKey.save_pkcs1('PEM'))

        with open(private_key_filename, 'wb') as priv_file:
            priv_file.write(privateKey.save_pkcs1('PEM'))

        print(f"Public and private keys saved as '{public_key_filename}' and '{private_key_filename}'")



# Key sizes to test
key_sizes = [1024, 2048, 3072, 4076, 7680, 15360]

# Run the measurement
measure_rsa_operations_with_file(key_sizes)
