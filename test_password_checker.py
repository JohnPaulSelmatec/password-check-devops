from password_checker import is_valid_password


def test1():
    passwords = [
        "Abcde123",
        "abcde123",
        "Abcdefgh",
        "123aV",
        "abcdefgh",
        "abch3",
        "abcH",
        "ABD"
    ]

    for password in passwords:
        print(password, is_valid_password(password))
