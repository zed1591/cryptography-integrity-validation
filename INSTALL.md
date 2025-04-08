# Installation Instructions

This guide will help you get the EdDSA Signature Generation and Verification Tool running on your system.

## Prerequisites

* **Python 3.6 or higher:** Ensure you have Python 3.6 or a later version installed on your system. You can check your Python version by running:
    ```bash
    python --version
    ```
    or
    ```bash
    python3 --version
    ```

* **pip:** Python's package installer. It usually comes bundled with Python. You can check if you have pip installed by running:
    ```bash
    pip --version
    ```
    or
    ```bash
    pip3 --version
    ```

## Installation Steps

1.  **Clone the repository (if you haven't already):**
    If you have the project files in a Git repository (e.g., on GitHub), clone it to your local machine using:
    ```bash
    git clone [repository_url]
    cd [repository_directory_name]
    ```
    Replace `[repository_url]` with the actual URL of your repository and `[repository_directory_name]` with the name of the directory that was created after cloning.

2.  **Install the required dependencies:**
    This project relies on the `cryptography` library. You can install it using pip:
    ```bash
    pip install cryptography
    ```
    or
    ```bash
    pip3 install cryptography
    ```

## Running the Tool

Once the dependencies are installed, you can run the script directly from your terminal:

```bash
python ed25519_tool.py
