from src.validators import (
    validate_email,
    validate_password,
    validate_dni,
)


def register_user(
    name: str,
    email: str,
    password: str,
    dni: str
) -> dict:

    if not name:
        raise ValueError("El nombre es obligatorio")

    if not validate_email(email):
        raise ValueError("Email inválido")

    if not validate_password(password):
        raise ValueError("Contraseña inválida")

    if not validate_dni(dni):
        raise ValueError("DNI inválido")

    return {
        "name": name,
        "email": email,
        "dni": dni,
        "status": "registered",
    }