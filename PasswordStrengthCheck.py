import re
import random
from sys import argv
from math import *

def uppercase_check(password):
    if re.search('[A-Z]', password):
        return True
    return False

def lowercase_check(password):
    if re.search('[a-z]', password):
        return True
    return False

def digit_check(password):
    if re.search('[0-9]', password):
        return True
    return False

def special_char_check(password):
    if re.search('[@_!#$%^&*()<>?/\|}{~:]', password):
        return True
    return False


def user_input_password_check():
    password = input("Enter password : ")
    if len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password) and special_char_check(password):
        print("Strong Password")
    else:
        print("Weak Password")
        

print(user_input_password_check())