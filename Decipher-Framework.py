#!/usr/bin/env python3
import base64
import codecs
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

console = Console()

# ------------------------------
# Cipher Functions
# ------------------------------

def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            # Shift within the alphabet
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def vigenere_cipher(text: str, key: str, mode: str = "encode") -> str:
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            # Calculate shift from key letter
            k = ord(key[key_index % key_length]) - ord('a')
            if mode == "decode":
                k = -k
            result += chr((ord(char) - offset + k) % 26 + offset)
            key_index += 1
        else:
            result += char
    return result

def base64_encode(text: str) -> str:
    encoded_bytes = base64.b64encode(text.encode())
    return encoded_bytes.decode()

def base64_decode(text: str) -> str:
    try:
        decoded_bytes = base64.b64decode(text.encode())
        return decoded_bytes.decode()
    except Exception as e:
        return f"Error decoding Base64: {e}"

# Morse Code mappings
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

def morse_encode(text: str) -> str:
    result = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[char])
        else:
            result.append(char)
    return " ".join(result)

def morse_decode(morse: str) -> str:
    # Build reverse mapping
    reverse_morse = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse.split(" / ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = "".join(reverse_morse.get(letter, letter) for letter in letters)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)

# ------------------------------
# Interface Functions
# ------------------------------

def display_menu():
    table = Table(title="Decipher Framework Menu", style="cyan", show_lines=True)
    table.add_column("Option", style="magenta", justify="center")
    table.add_column("Cipher/Algorithm", style="green")
    table.add_row("1", "Caesar Cipher")
    table.add_row("2", "ROT13")
    table.add_row("3", "Vigenère Cipher")
    table.add_row("4", "Base64 Encode/Decode")
    table.add_row("5", "Morse Code")
    table.add_row("0", "Exit")
    console.print(table)

def main():
    console.print(
        Panel(
            "[bold cyan]Welcome to Decipher Framework Made by : Cyb0rgBytes! [/bold cyan]\nA Terminal-based Cryptography Utility for Hackers & Crypto Enthusiasts",
            title="Decipher Framework",
            style="bold green"
        )
    )
    
    while True:
        display_menu()
        choice = Prompt.ask("Enter your choice", choices=["0", "1", "2", "3", "4", "5"], default="0")
        
        if choice == "0":
            console.print("Exiting... Goodbye!", style="bold red")
            break
        
        elif choice == "1":  # Caesar Cipher
            mode = Prompt.ask("Select mode", choices=["encode", "decode"], default="encode")
            text = Prompt.ask("Enter text")
            shift = IntPrompt.ask("Enter shift value (e.g., 3)")
            # For decoding, reverse the shift
            if mode == "decode":
                shift = -shift
            result = caesar_cipher(text, shift)
            console.print(Panel(f"[bold yellow]Result:[/bold yellow]\n{result}", style="blue"))
        
        elif choice == "2":  # ROT13
            text = Prompt.ask("Enter text for ROT13")
            result = codecs.encode(text, 'rot_13')
            console.print(Panel(f"[bold yellow]Result:[/bold yellow]\n{result}", style="blue"))
        
        elif choice == "3":  # Vigenère Cipher
            mode = Prompt.ask("Select mode", choices=["encode", "decode"], default="encode")
            text = Prompt.ask("Enter text")
            key = Prompt.ask("Enter key")
            result = vigenere_cipher(text, key, mode)
            console.print(Panel(f"[bold yellow]Result:[/bold yellow]\n{result}", style="blue"))
        
        elif choice == "4":  # Base64
            mode = Prompt.ask("Select mode", choices=["encode", "decode"], default="encode")
            text = Prompt.ask("Enter text")
            if mode == "encode":
                result = base64_encode(text)
            else:
                result = base64_decode(text)
            console.print(Panel(f"[bold yellow]Result:[/bold yellow]\n{result}", style="blue"))
        
        elif choice == "5":  # Morse Code
            mode = Prompt.ask("Select mode", choices=["encode", "decode"], default="encode")
            if mode == "encode":
                text = Prompt.ask("Enter text to convert to Morse Code")
                result = morse_encode(text)
            else:
                text = Prompt.ask("Enter Morse Code (use '/' for space between words)")
                result = morse_decode(text)
            console.print(Panel(f"[bold yellow]Result:[/bold yellow]\n{result}", style="blue"))
        
        console.print("\n")

if __name__ == '__main__':
    main()
