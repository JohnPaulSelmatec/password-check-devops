from password_checker import is_valid_password


def test1():
  assert is_valid_password("Abcde123") == True

#is_valid_password("Abcde123")
#is_valid_password("abcde123")
#is_valid_password("Abcdefgh")
#is_valid_password("123aV")
#is_valid_password("abcdefgh")
#is_valid_password("abch3")
#is_valid_password("abcH")
#is_valid_password("ABD")

