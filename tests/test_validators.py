from src.validators import (
    validate_email,
    validate_password,
    validate_dni,
)


def test_valid_email():
    assert validate_email("harry@example.com") is True


def test_invalid_email():
    assert validate_email("harry-example.com") is False


def test_empty_email():
    assert validate_email("") is False


def test_valid_password():
    assert validate_password("Password1") is True


def test_password_too_short():
    assert validate_password("Pass1") is False


def test_password_without_uppercase():
    assert validate_password("password1") is False


def test_password_without_lowercase():
    assert validate_password("PASSWORD1") is False


def test_password_without_number():
    assert validate_password("Password") is False


def test_valid_dni():
    assert validate_dni("12345678") is True


def test_invalid_dni_length():
    assert validate_dni("1234567") is False


def test_invalid_dni_letters():
    assert validate_dni("1234ABCD") is False


def test_empty_dni():
    assert validate_dni("") is False
    
def test_empty_password():
    assert validate_password("") is False