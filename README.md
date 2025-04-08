# cryptography-integrity-validation
# EdDSA Signature Generation and Verification Tool

This Python script demonstrates the generation of EdDSA (Ed25519) cryptographic key pairs, signing of messages, and verification of signatures using the `cryptography` library. It provides an interactive command-line interface for easy experimentation.

## Features

* **Key Generation:** Generates a new Ed25519 private and public key pair.
* **Public Key Output:** Displays the generated public key in base64 encoding for easy sharing.
* **Message Signing:** Allows you to input a message and sign it using the generated private key.
* **Signature Output:** Displays the generated signature in base64 encoding.
* **Signature Verification:** Enables you to input a base64-encoded public key, a message, and a base64-encoded signature to verify their authenticity.
* **Error Handling:** Includes basic error handling for invalid public key formats and signature decoding.
* **Interactive Interface:** Provides a simple command-line menu to perform different operations.

## Prerequisites

* **Python 3.6+**
* **`cryptography` library:** You can install it using pip:
    ```bash
    pip install cryptography
    ```

## How to Use

1.  **Save the code:** Save the provided Python script (the one you shared previously) as a `.py` file (e.g., `ed25519_tool.py`).

2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run it using:
    ```bash
    python ed25519_tool.py
    ```

3.  **Follow the on-screen instructions:**

    * The script will first generate a new key pair and display the public key in base64 format.
    * You will then be presented with the following options:
        ```
        Options:
        1. Sign a message
        2. Verify a signature
        3. Exit
        Enter your choice (1/2/3):
        ```

    * **To sign a message (Option 1):**
        * Enter `1` and press Enter.
        * You will be prompted to enter the message you want to sign.
        * The script will sign the message using the generated private key and display the base64-encoded signature.

    * **To verify a signature (Option 2):**
        * Enter `2` and press Enter.
        * You will be asked to enter the base64-encoded public key. You can copy and paste the public key that was generated earlier or one you have received from someone else.
        * Enter the original message that was signed.
        * Enter the base64-encoded signature you want to verify.
        * The script will attempt to verify the signature and display the result (True or False).

    * **To exit the script (Option 3):**
        * Enter `3` and press Enter.

## Important Security Considerations

* **Private Key Security:** The private key generated by this script is held in memory only during the script's execution. In a real-world application, **it is crucial to store and manage private keys securely**. This script does not implement any secure storage mechanisms.
* **Do not use the keys generated by this script for production systems or sensitive data without implementing proper security measures for private key management.**
* This tool is primarily for educational and demonstration purposes.

## Potential Future Enhancements

* **Saving and Loading Keys:** Implement functionality to save and load key pairs from files (with appropriate security considerations).
* **Different Output Formats:** Support outputting keys and signatures in other formats (e.g., PEM).
* **More Robust Input Validation:** Add more comprehensive input validation to prevent errors.
* **Command-Line Arguments:** Allow users to perform actions (e.g., sign, verify) directly from the command line without the interactive menu.


## Author

[Zemed Abeje /zed1591]
