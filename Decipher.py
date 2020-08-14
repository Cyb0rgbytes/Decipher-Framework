#! /usr/bin/env python3
import sys
import base64


def welcome():
    print(f'{Fore.WHITE}\nWelcome to Decipher.py {Fore.RED}')
    
    
def Ecrypt():
    print(f'''{Fore.RED}
    Please Pick the Algorithm you want to Encrypt with.
    1 for Base64
    2 for The Caesar shift
    3 for The Vigenère square''')
    
    
    Choice = input('Choice: ')
    Choice_bytes = Choice.encode('ascii')
    base64_bytes = base64.b64encode(Choice_bytes)
    base64_Choice = base64_bytes.decode('ascii')
    
    print(base64_Choice)
