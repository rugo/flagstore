# RSA Signature Verification Flask App

This is a simple Flask application that verifies RSA signed messages using a public key. It provides both a JSON API endpoint and an HTML form for submitting messages and signatures.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

### API Endpoint

You can verify signatures by sending a POST request to `/verify` with a form payload containing the `message` and `signature` fields.

Example using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/verify -F "message=test message" -F "signature=<hex_encoded_signature>"
```

