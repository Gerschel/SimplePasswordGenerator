#!usr/local/bin/python3
from os import urandom
from os import getcwd
from hashlib import sha256
from sys import argv

def generate():
    code = str(int.from_bytes(urandom(32), 'little'))
    code = sha256(code.encode()).hexdigest()
    code = [chr((int(code[x:x+2], 16)%94)+33) for x in range(0,64,2)]
    return "".join(code)

def filter_ask(password):
    filter_chars = input("What are the characters you need to filter out? ")
    return filter_out(password, filter_chars)

def filter_out(string_to_filter, filter_chars):
    for _character in filter_chars:
        string_to_filter = string_to_filter.replace(_character, "")
    return string_to_filter

def generate_filter(included_chars):
    alphabet = "".join([chr(character) for character in range(33, 127)])
    return filter_out(alphabet, included_chars)

def filter_out_unspecified(password, inclusive_string):
    filter_chars = generate_filter(inclusive_string)
    return filter_out(password, filter_chars)

if __name__ == "__main__":
    instruction = argv[1]
    print(argv)
    if instruction.lower()[0] == "f":
        password = filter_out(generate() + generate(), argv[2])
    elif instruction.lower()[0] == "i":
        password = filter_out_unspecified(generate() + generate(), argv[2])
    else:
        password = filter_ask(generate() + generate())
    print(password)
