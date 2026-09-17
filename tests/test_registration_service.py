import pytest

from src.registration_service import register_user


def test_register_valid_user():
    user = register_user(
        name="Harry Gonzales",
        email="harry@example.com",
        password="Password1",
        dni="12345678",
    )

    assert user["status"] == "registered"
    assert user["name"] == "Harry Gonzales"


def test_register_user_without_name():
    with pytest.raises(ValueError, match="El nombre es obligatorio"):
        register_user(
            name="",
            email="harry@example.com",
            password="Password1",
            dni="12345678",
        )


def test_register_user_with_invalid_email():
    with pytest.raises(ValueError, match="Email inválido"):
        register_user(
            name="Harry Gonzales",
            email="correo-invalido",
            password="Password1",
            dni="12345678",
        )


def test_register_user_with_invalid_password():
    with pytest.raises(ValueError, match="Contraseña inválida"):
        register_user(
            name="Harry Gonzales",
            email="harry@example.com",
            password="123",
            dni="12345678",
        )


def test_register_user_with_invalid_dni():
    with pytest.raises(ValueError, match="DNI inválido"):
        register_user(
            name="Harry Gonzales",
            email="harry@example.com",
            password="Password1",
            dni="ABC",
        )