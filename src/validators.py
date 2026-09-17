import re


def validate_email(email: str) -> bool:
    if not email:
        return False

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(password: str) -> bool:
    if not password:
        return False

    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit


def validate_dni(dni: str) -> bool:
    if not dni:
        return False

    return dni.isdigit() and len(dni) == 8