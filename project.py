
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64


def generate_keys():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message):
    return private_key.sign(message.encode())


def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message.encode())
        return True
    except Exception:
        return False


if __name__ == "__main__":
    # Generate keys
    priv_key, pub_key = generate_keys()

    # Serialize public key to base64 for sharing
    pub_key_bytes = pub_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    pub_key_base64 = base64.b64encode(pub_key_bytes).decode()

    print("Keys generated successfully.")
    print("Public Key (base64):", pub_key_base64)

    while True:  # Loop to allow repeated steps
        print("\nOptions:")
        print("1. Sign a message")
        print("2. Verify a signature")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            # Ask for a message to sign
            message = input("Enter a message to sign: ").strip()
            signature = sign_message(priv_key, message)

            # Serialize signature to base64 for sharing
            signature_base64 = base64.b64encode(signature).decode()
            print("\nMessage signed.")
            print("Signature (base64):", signature_base64)

        elif choice == "2":
            # Ask for the public key, message, and signature to verify
            pub_key_input = input("\nEnter the public key (base64 encoded): ").strip()

            # Verify and load the public key
            try:
                pub_key_bytes = base64.b64decode(pub_key_input)
                if len(pub_key_bytes) != 32:
                    raise ValueError("Invalid public key length: Must be exactly 32 bytes.")
                public_key = ed25519.Ed25519PublicKey.from_public_bytes(pub_key_bytes)
            except (ValueError, base64.binascii.Error) as e:
                print("Failed to load the public key:", e)
                continue

            verify_msg = input("Enter the message to verify: ").strip()
            signature_input = input("Enter the signature (base64 encoded): ").strip()

            # Verify the signature
            try:
                signature = base64.b64decode(signature_input)
                result = verify_signature(public_key, verify_msg, signature)
                print("\nVerification result:", result)
            except base64.binascii.Error as e:
                print("Invalid signature encoding:", e)
            except Exception as e:
                print("Verification failed:", e)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select from the options.")
