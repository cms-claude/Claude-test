# JWT Decoder

A simple and powerful command-line Python application to decode and verify JSON Web Tokens (JWT).

## Features

- **Decode JWTs** without signature verification
- **Verify JWTs** with signature validation
- **Multiple algorithm support**: HS256, HS384, HS512, RS256, RS384, RS512
- **Pretty-printed output** for easy reading
- **JSON output option** for programmatic use
- **Detailed error messages** for debugging
- **Command-line interface** for easy integration

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Claude-test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable (optional):
```bash
chmod +x jwt_decoder.py
```

## Usage

### Basic Decoding (Without Verification)

Decode a JWT token without verifying its signature:

```bash
python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
```

### Decoding with Verification

Decode and verify a JWT token using a secret key:

```bash
python jwt_decoder.py "your-jwt-token" --secret "your-secret-key"
```

### Specify Algorithm

Decode with a specific algorithm:

```bash
python jwt_decoder.py "your-jwt-token" --secret "your-secret-key" --algorithm HS256
```

### JSON Output

Get output in JSON format for programmatic use:

```bash
python jwt_decoder.py "your-jwt-token" --json
```

## Command-Line Options

```
positional arguments:
  token                 JWT token to decode

optional arguments:
  -h, --help            Show help message and exit
  -s SECRET, --secret SECRET
                        Secret key for verification (if provided, signature will be verified)
  -a ALGORITHM, --algorithm ALGORITHM
                        Algorithm to use for verification (default: HS256)
  -j, --json            Output as JSON instead of formatted text
```

## Examples

### Example 1: Decode without verification

```bash
python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
```

Output:
```
============================================================
JWT DECODED
============================================================

HEADER:
------------------------------------------------------------
{
  "alg": "HS256",
  "typ": "JWT"
}

PAYLOAD:
------------------------------------------------------------
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

============================================================
⚠ WARNING: Signature not verified!
============================================================
```

### Example 2: Decode with verification

```bash
python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" --secret "your-256-bit-secret"
```

Output:
```
============================================================
JWT DECODED
============================================================

HEADER:
------------------------------------------------------------
{
  "alg": "HS256",
  "typ": "JWT"
}

PAYLOAD:
------------------------------------------------------------
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

============================================================
✓ SIGNATURE VERIFIED
============================================================
```

### Example 3: JSON output

```bash
python jwt_decoder.py "your-jwt-token" --json
```

Output:
```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  },
  "verified": false
}
```

## Supported Algorithms

- **HS256**: HMAC using SHA-256
- **HS384**: HMAC using SHA-384
- **HS512**: HMAC using SHA-512
- **RS256**: RSASSA-PKCS1-v1_5 using SHA-256
- **RS384**: RSASSA-PKCS1-v1_5 using SHA-384
- **RS512**: RSASSA-PKCS1-v1_5 using SHA-512

## Error Handling

The application provides clear error messages for common issues:

- **Invalid token format**: When the JWT structure is malformed
- **Expired token**: When the token has passed its expiration time
- **Invalid signature**: When signature verification fails
- **Invalid algorithm**: When an unsupported algorithm is specified

## Security Notes

- **Signature verification is optional**: By default, the tool decodes without verification. This is useful for inspecting tokens but should not be used for authentication/authorization decisions.
- **Always verify in production**: When using JWTs for authentication, always verify the signature using the appropriate secret or public key.
- **Keep secrets secure**: Never commit secret keys to version control.

## Use Cases

- **Debugging**: Quickly inspect JWT tokens during development
- **Testing**: Verify token contents and signatures in test environments
- **Analysis**: Examine token structure and claims
- **Integration**: Use JSON output for automated workflows

## Dependencies

- **PyJWT**: Python library for encoding/decoding JWTs
- **cryptography**: Required for RSA and other advanced algorithms

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
