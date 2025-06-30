# utils/helpers.py
import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из букв и цифр"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def generate_random_email(domain="example.com"):
    """Генерирует случайный email"""
    local_part = generate_random_string(8)
    return f"{local_part}@{domain}"


def generate_weak_password():
    """Генерирует слабый пароль (без заглавных букв)"""
    return "weakpass123"


def generate_short_password(min_length=8):
    """Генерирует слишком короткий пароль"""
    return "short1A"
