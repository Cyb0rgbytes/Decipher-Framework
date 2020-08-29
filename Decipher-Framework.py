#!/usr/bin/env python3 

import base64
from colorama import Fore, Back


def welcome():
    print(f'{Fore.WHITE}\nWelcome to Decipher Framework {Fore.RED} Follow the instructions to navigate the script')

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def decipher():
    print(f'''{Fore.RED}
    Please select the cipher you want to use
    1 for Base64
    2 for Caesar Cipher
    3 for ROT13
    4 to Exit''')
    operation = input('Operation: ')

    operation_options = ['1', '2', '3', '4']
    if operation not in operation_options:
        print(f'\n{Fore.WHITE} Please Enter a Number from the List!')
    else:
        return operation

    ########################################
    # Base64


def decipher_base64():
    options = ['e', 'd']
    print(f'''{Fore.RED}Do You want to Encrypt or Decrypt?
  E for Encrypt
  D for Decrypt''')
    user_input = input('Operation: ').lower()

    if user_input == 'e':
        print(f'''{Fore.RED}Do you want to encrypt a file?
        Y for Yes
        N for Decrypting or encrypting on terminal''')
    else:
        print(f'''{Fore.RED}Do you want to decrypt a file?
        Y for Yes
        N for Decrypting or encrypting on terminal''')
    file_choice = input('Operation: ').lower()

    if file_choice == 'y':
        file_path = input("What is the path of the file? ")
        file_content = read_file(file_path)
    else:
        print('Please enter the string you would like Base64 encoded')
        string_input = input('String: ')

    if user_input in options:
        if user_input == 'e' and file_choice == 'y':
            encoded_string = base64.b64encode(file_content.encode()).decode()
            print(f'\n{Fore.WHITE}Your Ecrypted Text >>> {encoded_string}')
            write_file(file_path, encoded_string)
        elif user_input == 'd' and file_choice == 'y':
            encoded_string = base64.b64decode(file_content.encode()).decode()
            print(f'\n{Fore.WHITE}Your Ecrypted Text >>> {encoded_string}')
            write_file(file_path, encoded_string)
        elif user_input == 'e':
            print(f'\n{Fore.WHITE}Your Ecrypted Text >>> {base64.b64encode(string_input.encode()).decode()}')
        elif user_input == 'd':
            print(f'\n{Fore.WHITE}Your Decrypted Text >>> {base64.b64decode(string_input.encode()).decode()}')
    else:
        print(f'\n{Fore.WHITE} Please Enter a letter from the list!')

    ###########################################
    # ROT13


def decipher_rot13():
    print("WIP")

def decipher_caesar():
    print("WIP")


def main():
    quit = 0
    while quit == 0:
        user_answer = decipher()
        if user_answer == '1':
            decipher_base64()
        elif user_answer == '2':
            decipher_caesar()
        elif user_answer == '3':
            decipher_rot13()
        elif user_answer == '4':
            quit = 1


if __name__ == "__main__":
    welcome()
    main()
