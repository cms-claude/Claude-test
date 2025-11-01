#!/usr/bin/env python3
"""
JWT Decoder Application
A simple command-line tool to decode and verify JSON Web Tokens
"""

import json
import sys
import argparse
from typing import Dict, Any, Optional
import jwt
from jwt.exceptions import (
    DecodeError,
    InvalidSignatureError,
    ExpiredSignatureError,
    InvalidTokenError
)


class JWTDecoder:
    """Class to handle JWT decoding operations"""

    def __init__(self):
        self.algorithms = ['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512']

    def decode_without_verification(self, token: str) -> Dict[str, Any]:
        """
        Decode JWT without verifying the signature

        Args:
            token: JWT token string

        Returns:
            Dictionary containing header and payload
        """
        try:
            # Decode header
            header = jwt.get_unverified_header(token)

            # Decode payload without verification
            payload = jwt.decode(token, options={"verify_signature": False})

            return {
                "header": header,
                "payload": payload
            }
        except DecodeError as e:
            raise ValueError(f"Invalid token format: {e}")
        except Exception as e:
            raise ValueError(f"Error decoding token: {e}")

    def decode_with_verification(
        self,
        token: str,
        secret: str,
        algorithms: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Decode JWT with signature verification

        Args:
            token: JWT token string
            secret: Secret key or public key for verification
            algorithms: List of allowed algorithms (default: ['HS256'])

        Returns:
            Dictionary containing header and verified payload
        """
        if algorithms is None:
            algorithms = ['HS256']

        try:
            # Get header
            header = jwt.get_unverified_header(token)

            # Decode and verify
            payload = jwt.decode(token, secret, algorithms=algorithms)

            return {
                "header": header,
                "payload": payload,
                "verified": True
            }
        except ExpiredSignatureError:
            raise ValueError("Token has expired")
        except InvalidSignatureError:
            raise ValueError("Invalid signature")
        except InvalidTokenError as e:
            raise ValueError(f"Invalid token: {e}")
        except Exception as e:
            raise ValueError(f"Error verifying token: {e}")

    def pretty_print(self, data: Dict[str, Any]) -> str:
        """
        Format decoded JWT data for display

        Args:
            data: Dictionary containing decoded JWT data

        Returns:
            Formatted string
        """
        output = []
        output.append("=" * 60)
        output.append("JWT DECODED")
        output.append("=" * 60)

        if "header" in data:
            output.append("\nHEADER:")
            output.append("-" * 60)
            output.append(json.dumps(data["header"], indent=2))

        if "payload" in data:
            output.append("\nPAYLOAD:")
            output.append("-" * 60)
            output.append(json.dumps(data["payload"], indent=2))

        if data.get("verified"):
            output.append("\n" + "=" * 60)
            output.append("✓ SIGNATURE VERIFIED")
            output.append("=" * 60)
        else:
            output.append("\n" + "=" * 60)
            output.append("⚠ WARNING: Signature not verified!")
            output.append("=" * 60)

        return "\n".join(output)


def main():
    """Main entry point for the application"""
    parser = argparse.ArgumentParser(
        description="Decode and optionally verify JSON Web Tokens (JWT)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Decode without verification
  python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

  # Decode with verification
  python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." --secret "your-secret-key"

  # Decode with verification and specific algorithm
  python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." --secret "your-secret-key" --algorithm HS256

  # Output as JSON
  python jwt_decoder.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." --json
        """
    )

    parser.add_argument(
        "token",
        help="JWT token to decode"
    )

    parser.add_argument(
        "-s", "--secret",
        help="Secret key for verification (if provided, signature will be verified)"
    )

    parser.add_argument(
        "-a", "--algorithm",
        help="Algorithm to use for verification (default: HS256)",
        default="HS256"
    )

    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output as JSON instead of formatted text"
    )

    args = parser.parse_args()

    decoder = JWTDecoder()

    try:
        if args.secret:
            # Decode with verification
            result = decoder.decode_with_verification(
                args.token,
                args.secret,
                [args.algorithm]
            )
        else:
            # Decode without verification
            result = decoder.decode_without_verification(args.token)
            result["verified"] = False

        # Output results
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(decoder.pretty_print(result))

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
