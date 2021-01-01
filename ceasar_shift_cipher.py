from collections import deque


def shifter(paramater, shift):
    shifted = deque(paramater)
    shifted.rotate(shift)
    return shifted


def var_init(shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "[]{}()+-*/:;<>,.?!_@#"
    s_letters = shifter(letters, shift) + shifter(letters.upper(), shift)
    s_numbers = shifter(numbers, shift)
    s_symbols = shifter(symbols, shift)
    dicts = dict(zip(letters+letters.upper()+numbers+symbols,
                     s_letters+s_numbers+s_symbols))
    return dicts


def encoder(texts, dicts):
    line = ""
    keys = dicts.keys()
    for text in texts:
        if text not in keys:
            line += text
        else:
            line += dicts[text]
    return line


def text_coder(texts, shift):
    dicts = var_init(int(shift))
    code = encoder(texts, dicts)
    return code


def textfile_coder():
    file_in = input("Enter filename:\n")
    shift = input("Enter the number of places you want to shift:\n")
    dicts = var_init(int(shift))
    coded = []
    with open(file_in, "r", encoding='utf-8', errors='replace') as filename:
        texts = filename.read().splitlines()
        for text in texts:
            code = encoder(text, dicts)
            coded.append(code)
    with open(file_in, "w", encoding='utf-8', errors='replace') as filename:
        for code in coded:
            filename.write(code + "\n")
