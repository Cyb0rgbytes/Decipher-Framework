#!/usr/bin/env python3 

import colorama
from colorama import init, Fore
import base64


def welcome():
    print(f'{Fore.WHITE}\nWelcome to Decipher Framework {Fore.RED} Follow the instructions to navigate the script')
    operation()

def operation():
    print(f'''{Fore.RED}
    Please select the cipher you want to use
    1 for Base64
    2 for Caesar Cipher
    3 for ROT13''')
    operation = input('Operation: ')

    operation_options = ['1', '2', '3']
    if operation not in operation_options:
        print (f'\n{Fore.WHITE} Please Enter a Number from the List!')
    operation_base64()

    ########################################
    # Base64
def operation_base64():
    if operation == '1': operation_base64()
        print(f'''{Fore.RED}Do You want to Encrypt or Decrypt?
        E for Encrypt
        D for Decrypt''')
        operation_base64 = input('Operation: ')

        operation_base64_options = ['E', 'e', 'D', 'd']
    if  operation_base64 not in operation_base64_options:
        print (f'\n{Fore.WHITE} Please Enter a letter from the list!')


        operation_base64()
    operation()
welcome()

