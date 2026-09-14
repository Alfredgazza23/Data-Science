import sys

def main():
    if len(sys.argv) != 4:
        raise Exception("Usage: python caesar.py <encode|decode> <text> <shift>")

    mode = sys.argv[1]
    text = sys.argv[2]

    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer")

    if not is_latin(text):
        raise Exception("The script does not support your language yet.")

    if mode == "encode":
        print(caesar(text, shift, encode=True))
    elif mode == "decode":
        print(caesar(text, shift, encode=False))
    else:
        raise Exception("Mode must be 'encode' or 'decode'")

def is_latin(text):
    for char in text:
        if char.isalpha() and not char.isascii():
            return False
    return True

def shift_char(char, shift, encode=True):
    if not char.isalpha():
        return char

    base = ord('A') if char.isupper() else ord('a')
    offset = shift if encode else -shift
    return chr((ord(char) - base + offset) % 26 + base)

def caesar(text, shift, encode=True):
    return ''.join(shift_char(char, shift, encode) for char in text)

if __name__ == "__main__":
    main()
