#!/usr/bin/env python3
"""
DECIPHER FRAMEWORK v2.0 - CYBERPUNK EDITION
Advanced Cryptography Toolkit with Neural Network Integration
Author: Cyb0rgBytes
"""

import base64
import codecs
import math
import itertools
import string
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from collections import Counter

# Rich imports for cyberpunk aesthetics
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box
from rich.align import Align
import time

console = Console()

# ASCII Art for cyberpunk aesthetics
CYBER_ASCII = """
╔══════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ║
║  ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ║
║  ██║  ██║█████╗  ██║     ██║██████╔╝███████║█████╗  ██████╔╝    ║
║  ██║  ██║██╔══╝  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    ║
║  ██████╔╝███████╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║    ║
║  ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ║
║                                                                  ║
║                [bold cyan]CRYPTOGRAPHIC NEURAL INTERFACE[/bold cyan]                ║
║                      [bold magenta]v2.0 - 2077 EDITION[/bold magenta]                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ------------------------------
# ENHANCED CIPHER FUNCTIONS
# ------------------------------

def caesar_cipher(text: str, shift: int, decode: bool = False) -> str:
    """Enhanced Caesar cipher with frequency analysis hint"""
    if decode:
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_bruteforce(text: str) -> List[Tuple[int, str, float]]:
    """Brute force Caesar cipher with frequency scoring"""
    results = []
    english_freq = {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0,
        'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15,
        'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5,
        'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1,
        'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0,
        'z': 0.074
    }
    
    for shift in range(26):
        decrypted = caesar_cipher(text, shift, decode=True)
        score = 0
        letters = [c.lower() for c in decrypted if c.isalpha()]
        if letters:
            freq = Counter(letters)
            for letter, count in freq.items():
                if letter in english_freq:
                    observed = (count / len(letters)) * 100
                    score += (english_freq[letter] - observed) ** 2
        results.append((shift, decrypted, score))
    
    return sorted(results, key=lambda x: x[2])[:5]  # Top 5 most likely

def vigenere_cipher(text: str, key: str, mode: str = "encode") -> str:
    """Enhanced Vigenère with auto-key feature"""
    result = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            offset = ord('A')
            
            k = ord(key[key_index % key_length]) - offset
            if mode == "decode":
                k = -k
            
            new_char = chr((ord(char) - offset + k) % 26 + offset)
            if not is_upper:
                new_char = new_char.lower()
            
            result += new_char
            key_index += 1
        else:
            result += char
    
    return result

def autokey_vigenere(text: str, key: str, mode: str = "encode") -> str:
    """Vigenère cipher with autokey feature"""
    result = ""
    key = key.upper()
    key_stream = list(key)
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            offset = ord('A')
            
            k = ord(key_stream.pop(0)) - offset
            if mode == "decode":
                decrypted = chr((ord(char) - offset - k) % 26 + offset)
                key_stream.append(decrypted)
                result_char = decrypted
            else:
                encrypted = chr((ord(char) - offset + k) % 26 + offset)
                key_stream.append(char)  # Use original plaintext
                result_char = encrypted
            
            if not is_upper:
                result_char = result_char.lower()
            
            result += result_char
        else:
            result += char
    
    return result

def base64_encode(text: str) -> str:
    """Base64 encode with cyber formatting"""
    encoded_bytes = base64.b64encode(text.encode())
    return encoded_bytes.decode()

def base64_decode(text: str) -> str:
    """Base64 decode with multiple attempts"""
    try:
        decoded_bytes = base64.b64decode(text.encode())
        return decoded_bytes.decode()
    except:
        try:
            decoded_bytes = base64.urlsafe_b64decode(text.encode())
            return decoded_bytes.decode()
        except Exception as e:
            return f"[red]Decryption Failure: {str(e)}[/red]"

def atbash_cipher(text: str) -> str:
    """Atbash cipher (A↔Z, B↔Y, etc.)"""
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            result += chr(2 * offset + 25 - ord(char))
        else:
            result += char
    return result

def affine_cipher(text: str, a: int, b: int, decode: bool = False) -> str:
    """Affine cipher: E(x) = (ax + b) mod 26"""
    result = ""
    
    # Check if 'a' is coprime with 26
    if math.gcd(a, 26) != 1:
        return "[red]ERROR: 'a' must be coprime with 26[/red]"
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            x = ord(char) - offset
            
            if decode:
                # Find modular inverse of a
                a_inv = pow(a, -1, 26)  # Python 3.8+
                new_x = (a_inv * (x - b)) % 26
            else:
                new_x = (a * x + b) % 26
            
            result += chr(new_x + offset)
        else:
            result += char
    
    return result

def rail_fence_cipher(text: str, rails: int, decode: bool = False) -> str:
    """Rail fence cipher (zigzag pattern)"""
    if decode:
        result = [''] * len(text)
        idx = 0
        for rail in range(rails):
            pos = rail
            down = True
            while pos < len(text):
                if idx < len(text):
                    result[pos] = text[idx]
                    idx += 1
                if rail == 0 or rail == rails - 1:
                    pos += 2 * (rails - 1)
                else:
                    if down:
                        pos += 2 * (rails - rail - 1)
                    else:
                        pos += 2 * rail
                    down = not down
        return ''.join(result)
    else:
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        
        for char in text:
            fence[rail].append(char)
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
        
        return ''.join([''.join(rail) for rail in fence])

def xor_cipher(text: str, key: str) -> str:
    """XOR cipher with repeating key"""
    result = []
    key_bytes = key.encode()
    
    for i, char in enumerate(text):
        result_char = chr(ord(char) ^ key_bytes[i % len(key_bytes)])
        result.append(result_char)
    
    return ''.join(result)

def bacon_cipher(text: str, mode: str = "encode") -> str:
    """Bacon's cipher (5-bit binary representation)"""
    bacon_dict = {
        'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
        'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
        'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
        'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
        'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
        'Z': 'bbaab'
    }
    
    reverse_bacon = {v: k for k, v in bacon_dict.items()}
    
    if mode == "encode":
        result = []
        for char in text.upper():
            if char.isalpha():
                result.append(bacon_dict.get(char, char))
            elif char == ' ':
                result.append(' ')
        return ' '.join(result)
    else:
        result = []
        chunks = text.split()
        for chunk in chunks:
            if len(chunk) == 5:
                result.append(reverse_bacon.get(chunk.lower(), '?'))
            else:
                result.append(chunk)
        return ''.join(result)

def playfair_cipher(text: str, key: str, mode: str = "encode") -> str:
    """Playfair cipher implementation"""
    # Create Playfair square
    key = key.upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_square = []
    
    for char in key + alphabet:
        if char not in key_square and char.isalpha():
            key_square.append(char)
    
    # Prepare text
    text = text.upper().replace('J', 'I').replace(' ', '')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    
    result = []
    for pair in pairs:
        a, b = pair[0], pair[1]
        row_a = key_square.index(a) // 5
        col_a = key_square.index(a) % 5
        row_b = key_square.index(b) // 5
        col_b = key_square.index(b) % 5
        
        if row_a == row_b:
            # Same row
            if mode == "encode":
                result.append(key_square[row_a * 5 + (col_a + 1) % 5])
                result.append(key_square[row_b * 5 + (col_b + 1) % 5])
            else:
                result.append(key_square[row_a * 5 + (col_a - 1) % 5])
                result.append(key_square[row_b * 5 + (col_b - 1) % 5])
        elif col_a == col_b:
            # Same column
            if mode == "encode":
                result.append(key_square[((row_a + 1) % 5) * 5 + col_a])
                result.append(key_square[((row_b + 1) % 5) * 5 + col_b])
            else:
                result.append(key_square[((row_a - 1) % 5) * 5 + col_a])
                result.append(key_square[((row_b - 1) % 5) * 5 + col_b])
        else:
            # Rectangle
            result.append(key_square[row_a * 5 + col_b])
            result.append(key_square[row_b * 5 + col_a])
    
    return ''.join(result)

def morse_code(text: str, mode: str = "encode") -> str:
    """Morse code with timing and prosigns"""
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    
    reverse_morse = {v: k for k, v in morse_dict.items()}
    
    if mode == "encode":
        result = []
        for char in text.upper():
            result.append(morse_dict.get(char, char))
        return ' '.join(result)
    else:
        result = []
        words = text.split(' / ')
        for word in words:
            letters = word.split()
            decoded_word = ''.join(reverse_morse.get(letter, '') for letter in letters)
            result.append(decoded_word)
        return ' '.join(result)

def binary_conversion(text: str, mode: str = "encode") -> str:
    """Binary encoding/decoding"""
    if mode == "encode":
        return ' '.join(format(ord(c), '08b') for c in text)
    else:
        try:
            binary_chars = text.split()
            return ''.join(chr(int(b, 2)) for b in binary_chars)
        except:
            return "[red]Invalid binary format[/red]"

def hex_conversion(text: str, mode: str = "encode") -> str:
    """Hexadecimal encoding/decoding"""
    if mode == "encode":
        return text.encode().hex()
    else:
        try:
            return bytes.fromhex(text).decode()
        except:
            return "[red]Invalid hex format[/red]"

def rot13(text: str) -> str:
    """ROT13 cipher"""
    return codecs.encode(text, 'rot_13')

# ------------------------------
# CYBERPUNK VISUAL EFFECTS
# ------------------------------

def cyber_animation(text: str, color: str = "cyan") -> None:
    """Cyberpunk-style typing animation"""
    with console.status("[bold green]Initializing cryptographic protocols...") as status:
        for i, char in enumerate(text):
            console.print(f"[{color}]{char}[/{color}]", end="", style="bold")
            time.sleep(0.01)
        console.print()

def display_header():
    """Display cyberpunk header"""
    console.clear()
    console.print(CYBER_ASCII, style="bold cyan")
    console.print(Panel(
        f"[bold magenta]System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/bold magenta]\n"
        f"[bold green]Cipher Protocols Loaded: 14[/bold green]\n"
        f"[bold yellow]Neural Interface: ACTIVE[/bold yellow]",
        title="[bold]SYSTEM STATUS[/bold]",
        border_style="cyan",
        box=box.DOUBLE_EDGE
    ))
    console.print()

def create_cipher_table() -> Table:
    """Create cyberpunk cipher selection table"""
    table = Table(
        title="[bold magenta]CRYPTOGRAPHIC PROTOCOLS[/bold magenta]",
        show_header=True,
        header_style="bold cyan",
        box=box.HEAVY_EDGE,
        show_lines=True,
        title_style="bold yellow"
    )
    
    table.add_column("ID", style="bold green", width=8)
    table.add_column("Cipher Protocol", style="bold white", width=25)
    table.add_column("Type", style="bold blue", width=15)
    table.add_column("Status", style="bold yellow", width=12)
    
    ciphers = [
        ("1", "Caesar Cipher", "Substitution", "[green]ACTIVE[/green]"),
        ("2", "ROT13", "Substitution", "[green]ACTIVE[/green]"),
        ("3", "Vigenère Cipher", "Polyalphabetic", "[green]ACTIVE[/green]"),
        ("4", "Autokey Vigenère", "Polyalphabetic", "[cyan]ADVANCED[/cyan]"),
        ("5", "Base64", "Encoding", "[green]ACTIVE[/green]"),
        ("6", "Atbash Cipher", "Substitution", "[green]ACTIVE[/green]"),
        ("7", "Affine Cipher", "Mathematical", "[yellow]CRYPTO[/yellow]"),
        ("8", "Rail Fence", "Transposition", "[green]ACTIVE[/green]"),
        ("9", "XOR Cipher", "Bitwise", "[red]SECURE[/red]"),
        ("10", "Playfair Cipher", "Digraphic", "[yellow]CRYPTO[/yellow]"),
        ("11", "Bacon Cipher", "Binary", "[green]ACTIVE[/green]"),
        ("12", "Morse Code", "Signaling", "[green]ACTIVE[/green]"),
        ("13", "Binary", "Encoding", "[cyan]DIGITAL[/cyan]"),
        ("14", "Hexadecimal", "Encoding", "[cyan]DIGITAL[/cyan]"),
        ("B", "Caesar Brute Force", "Cryptanalysis", "[red]ATTACK[/red]"),
        ("C", "Cipher Information", "Help", "[blue]INFO[/blue]"),
        ("0", "System Shutdown", "Exit", "[red]EXIT[/red]")
    ]
    
    for cipher in ciphers:
        table.add_row(*cipher)
    
    return table

def show_cipher_info(cipher_name: str):
    """Display detailed information about a cipher"""
    info = {
        "Caesar Cipher": {
            "description": "Simple substitution cipher where each letter is shifted by a fixed number",
            "key_space": "25 (for English alphabet)",
            "security": "Very weak - easily broken by frequency analysis",
            "year": "100 BC",
            "use_case": "Educational purposes, simple obfuscation"
        },
        "Vigenère Cipher": {
            "description": "Polyalphabetic cipher using a keyword for multiple Caesar shifts",
            "key_space": "26^k where k is key length",
            "security": "Moderate - was considered unbreakable for centuries",
            "year": "1553",
            "use_case": "Historical secure communication"
        },
        "Playfair Cipher": {
            "description": "Digraphic substitution cipher using a 5x5 matrix",
            "key_space": "25! (practical keys are fewer)",
            "security": "Moderate - used in WWI and WWII",
            "year": "1854",
            "use_case": "Military communications"
        },
        "XOR Cipher": {
            "description": "Bitwise operation cipher, secure with one-time pad",
            "key_space": "Infinite with proper key",
            "security": "Unbreakable with true random one-time pad",
            "year": "1917",
            "use_case": "Modern cryptography, stream ciphers"
        }
    }
    
    if cipher_name in info:
        data = info[cipher_name]
        console.print(Panel(
            f"[bold cyan]Description:[/bold cyan] {data['description']}\n"
            f"[bold green]Key Space:[/bold green] {data['key_space']}\n"
            f"[bold yellow]Security Level:[/bold yellow] {data['security']}\n"
            f"[bold magenta]First Known Use:[/bold magenta] {data['year']}\n"
            f"[bold blue]Primary Use Case:[/bold blue] {data['use_case']}",
            title=f"[bold]CIPHER PROTOCOL: {cipher_name}[/bold]",
            border_style="cyan",
            box=box.ROUNDED
        ))

# ------------------------------
# MAIN INTERFACE
# ------------------------------

def main():
    """Main cyberpunk interface"""
    display_header()
    
    while True:
        table = create_cipher_table()
        console.print(table)
        console.print()
        
        choice = Prompt.ask(
            "[bold yellow]Select Protocol ID[/bold yellow]",
            choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                    "10", "11", "12", "13", "14", "B", "C"],
            default="0"
        )
        
        if choice == "0":
            cyber_animation("Initiating system shutdown... Goodbye!", "red")
            break
        
        elif choice == "C":
            cipher_name = Prompt.ask(
                "[bold cyan]Enter cipher name to learn about[/bold cyan]",
                choices=["Caesar Cipher", "Vigenère Cipher", "Playfair Cipher", "XOR Cipher"]
            )
            show_cipher_info(cipher_name)
            continue
        
        console.print()
        
        # Get input text with cyber animation
        text = Prompt.ask("[bold green]Enter transmission text[/bold green]")
        
        # Special case for brute force
        if choice == "B":
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task("[cyan]Brute forcing Caesar cipher...", total=26)
                results = caesar_bruteforce(text)
            
            console.print("\n[bold red]BRUTE FORCE RESULTS[/bold red]")
            console.print("[yellow]Most likely decryptions (sorted by frequency analysis):[/yellow]\n")
            
            for i, (shift, decrypted, score) in enumerate(results, 1):
                console.print(Panel(
                    f"[bold cyan]Shift:[/bold cyan] {shift}\n"
                    f"[bold green]Text:[/bold green] {decrypted}\n"
                    f"[bold yellow]Confidence Score:[/bold yellow] {score:.2f}",
                    title=f"[bold]Result #{i}[/bold]",
                    border_style="green" if i == 1 else "blue",
                    box=box.SIMPLE
                ))
            continue
        
        # Get mode for ciphers that support encode/decode
        if choice not in ["2", "6", "13", "14"]:  # ROT13, Atbash, Binary, Hex don't need mode
            mode = Prompt.ask(
                "[bold cyan]Select mode[/bold cyan]",
                choices=["encode", "decode"],
                default="encode"
            )
        
        # Process based on choice
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task("[cyan]Processing cryptographic protocol...", total=100)
            
            for i in range(100):
                progress.update(task, advance=1)
                time.sleep(0.01)
            
            if choice == "1":  # Caesar
                shift = IntPrompt.ask("[bold magenta]Enter shift value (0-25)[/bold magenta]", default=3)
                result = caesar_cipher(text, shift, mode == "decode")
            
            elif choice == "2":  # ROT13
                result = rot13(text)
            
            elif choice == "3":  # Vigenère
                key = Prompt.ask("[bold magenta]Enter encryption key[/bold magenta]")
                result = vigenere_cipher(text, key, mode)
            
            elif choice == "4":  # Autokey Vigenère
                key = Prompt.ask("[bold magenta]Enter initial key[/bold magenta]")
                result = autokey_vigenere(text, key, mode)
            
            elif choice == "5":  # Base64
                if mode == "encode":
                    result = base64_encode(text)
                else:
                    result = base64_decode(text)
            
            elif choice == "6":  # Atbash
                result = atbash_cipher(text)
            
            elif choice == "7":  # Affine
                a = IntPrompt.ask("[bold magenta]Enter 'a' value (must be coprime with 26)[/bold magenta]", default=5)
                b = IntPrompt.ask("[bold magenta]Enter 'b' value (0-25)[/bold magenta]", default=8)
                result = affine_cipher(text, a, b, mode == "decode")
            
            elif choice == "8":  # Rail Fence
                rails = IntPrompt.ask("[bold magenta]Enter number of rails[/bold magenta]", default=3)
                result = rail_fence_cipher(text, rails, mode == "decode")
            
            elif choice == "9":  # XOR
                key = Prompt.ask("[bold magenta]Enter XOR key[/bold magenta]")
                result = xor_cipher(text, key)
            
            elif choice == "10":  # Playfair
                key = Prompt.ask("[bold magenta]Enter Playfair key[/bold magenta]")
                result = playfair_cipher(text, key, mode)
            
            elif choice == "11":  # Bacon
                result = bacon_cipher(text, mode)
            
            elif choice == "12":  # Morse
                result = morse_code(text, mode)
            
            elif choice == "13":  # Binary
                result = binary_conversion(text, mode)
            
            elif choice == "14":  # Hexadecimal
                result = hex_conversion(text, mode)
        
        # Display result with cyberpunk flair
        console.print("\n" + "═" * 60, style="bold cyan")
        console.print(Panel(
            f"[bold green]INPUT:[/bold green] {text}\n"
            f"[bold yellow]PROTOCOL:[/bold yellow] {choice}\n"
            f"[bold magenta]MODE:[/bold magenta] {mode if 'mode' in locals() else 'N/A'}\n"
            f"[bold cyan]OUTPUT:[/bold cyan]\n{result}",
            title="[bold]CRYPTOGRAPHIC ANALYSIS COMPLETE[/bold]",
            border_style="green",
            box=box.DOUBLE,
            padding=(1, 2)
        ))
        
        # Save option
        if Prompt.ask("[bold yellow]Save to log file?[/bold yellow]", choices=["y", "n"], default="n") == "y":
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cipher_log_{timestamp}.txt"
            with open(filename, 'w') as f:
                f.write(f"Cipher Protocol: {choice}\n")
                f.write(f"Mode: {mode if 'mode' in locals() else 'N/A'}\n")
                f.write(f"Input: {text}\n")
                f.write(f"Output: {result}\n")
            console.print(f"[green]Log saved to {filename}[/green]")
        
        console.print("\n" + "─" * 60 + "\n", style="bold blue")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cyber_animation("\nEmergency shutdown initiated...", "red")
    except Exception as e:
        console.print(f"[bold red]SYSTEM ERROR: {str(e)}[/bold red]")
        console.print("[yellow]Please report this issue to the system administrator.[/yellow]")