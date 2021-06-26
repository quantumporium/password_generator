import sys
sys.path.append("../")

from app.password_generator import correct_size_password as correct_size_function

def test_if_correction_function_enter_valid_lenght_for_password():
    assert correct_size_function(1) == 5, "it should give five because the password can not be shorter than 5"
    assert correct_size_function(6) == 6, "it should give 6 because the password lenght exceed the minimum requirement"
    assert correct_size_function(5) == 5, "it should give 5 because the password lenght is the minimum requirement"

