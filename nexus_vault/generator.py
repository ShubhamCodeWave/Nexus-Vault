import secrets
import string

def generate_secure_password(length: int = 16, include_symbols: bool = True) -> str:
    """Generates an industrially secure random password."""
    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation
    
    return ''.join(secrets.choice(alphabet) for i in range(length))
