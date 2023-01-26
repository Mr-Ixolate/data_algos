import re

def decompress(short:str) -> str:
    letters = re.split('\d+', short)[1::]
    digits = re.split('[a-z]', short)[:-1:]

    long_str=""
    for digit,letter in zip(digits,letters):
        long_str += int(digit)*letter

    return long_str

        
    

test = "3a2b5c"

print(decompress(test))