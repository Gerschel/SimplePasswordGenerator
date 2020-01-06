#!usr/local/bin/python3
from os import urandom
from os import getcwd
from hashlib import sha256

def generate():
    code = str(int.from_bytes(urandom(32), 'little'))
    code = sha256(code.encode()).hexdigest()
    code = [chr((int(code[x:x+2], 16)%94)+33) for x in range(0,64,2)]
    return "".join(code)

def filter_out(password):
    filter_chars = input("What are the characters you need to filter out? ")
    for _character in filter_chars:
        password = password.replace(_character, "")
    return password


password = generate()
password += generate()
password = filter_out(password)
print(getcwd())
print(password)
