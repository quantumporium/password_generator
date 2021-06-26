#!/usr/bin/env python3

import random
import array
import sys


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' ,'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_symbols = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_lower + rand_upper + rand_lower

def correct_size_password(MAX_LEN):
    """Make sure that the password has a minimum of 5 character"""
    if MAX_LEN < 5:
        MAX_LEN = 5
    else:
        MAX_LEN = MAX_LEN

    return MAX_LEN

if __name__ == "__main__":

    print("------"*10)
    print(f"Program: {sys.argv[0]}")
    print("------"*10)

    try:
        MAX_LEN = int(sys.argv[1])
        MAX_LEN = correct_size_password(MAX_LEN)
    except IndexError:
        try:
            MAX_LEN = int(input("Enter lenght of password: "))
            MAX_LEN = correct_size_password(MAX_LEN)    
        except:
            print("An error occur")

    except:
        print("An error occur")


    for character in range( MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for character in temp_pass_list:
        password = password + character

    print(password)


