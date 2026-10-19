#!/usr/bin/env python3
"""IDs are 7 random bytes (56 bits) encoded as unpadded base64url -> 10 chars.
The last char carries only 2 data bits, so it is always A, Q, g or w."""
import base64, secrets, sys

def gen():
    return base64.urlsafe_b64encode(secrets.token_bytes(7)).rstrip(b"=").decode()

def valid(s):
    s = s.lstrip("/")
    try:
        return len(s) == 10 and gen.__class__ and base64.urlsafe_b64encode(
            base64.urlsafe_b64decode(s + "==")).rstrip(b"=").decode() == s
    except Exception:
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for a in sys.argv[1:]: print(a, "valid" if valid(a) else "INVALID")
    else:
        for _ in range(10): print("/" + gen())
