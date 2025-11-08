# Claude-test Repository

This repository contains two Python applications:

1. **JWT Decoder** - A command-line tool to decode and verify JSON Web Tokens
2. **Brainfuck Hello World** - A Brainfuck program that prints "Hello World!" with interpreter

---

## JWT Decoder

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

---

## Brainfuck Hello World

A classic "Hello World!" program written in the esoteric programming language Brainfuck, along with a Python interpreter to execute it.

### What is Brainfuck?

Brainfuck is a minimalist esoteric programming language created by Urban Müller in 1993. Despite having only 8 commands, it is Turing-complete. The language operates on an array of memory cells (tape) and uses a pointer to navigate and modify these cells.

### Brainfuck Commands

- `>` - Move pointer right
- `<` - Move pointer left
- `+` - Increment byte at pointer
- `-` - Decrement byte at pointer
- `.` - Output byte at pointer as ASCII character
- `,` - Input one byte and store at pointer
- `[` - Jump forward past matching `]` if byte at pointer is zero
- `]` - Jump back to matching `[` if byte at pointer is nonzero

### Files

- **hello_world.bf** - The Brainfuck source code that prints "Hello World!"
- **brainfuck_interpreter.py** - A Python interpreter to execute Brainfuck programs

### Running the Hello World Program

```bash
python brainfuck_interpreter.py hello_world.bf
```

Output:
```
Hello World!
```

### Using the Brainfuck Interpreter

The interpreter can run any Brainfuck program:

```bash
python brainfuck_interpreter.py <your-program.bf>
```

### Features of the Interpreter

- **30,000 memory cells** (expandable automatically)
- **8-bit cells** with wrapping (0-255)
- **Bracket matching** for loop validation
- **Error handling** for malformed programs
- **Comment support** (ignores non-Brainfuck characters)

### Example Programs

You can write your own Brainfuck programs! Here are some simple examples:

**Print 'A' (ASCII 65):**
```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>-.
```

**Print numbers 0-9:**
```brainfuck
++++[>++++++++++<-]>[>+>+<<-]>>[<<+>>-]<[>+.<-]
```

### The Hello World Code Explained

The `hello_world.bf` program uses nested loops to efficiently generate the ASCII values for each character in "Hello World!" and then prints them. The algorithm minimizes the number of operations by using multiplication through loops rather than incrementing each character value individually.

### Fun Facts

- Brainfuck programs are notoriously difficult to read and write
- The language is designed to challenge programmers, not for practical use
- Despite its simplicity, you can write complex programs including interpreters for other languages
- The name is often sanitized to "Brainf*ck" or "BF" in formal contexts
