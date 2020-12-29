from collections import deque


def shift_list(paramater, shift):
    # returns shifted list
    shifted = deque(paramater)
    shifted.rotate(shift)
    return shifted


def var(shift):
    # var init
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "[]{}()+-*/:;<>,.?!_@#"
    # var shift
    s_letters = shift_list(letters, shift) + shift_list(letters.upper(), shift)
    s_numbers = shift_list(numbers, shift)
    s_symbols = shift_list(symbols, shift)
    # returns dictionary {"var init": "var shift"}
    dicts = dict(zip(letters+letters.upper()+numbers+symbols,
                     s_letters+s_numbers+s_symbols))
    return dicts


def encode(texts, dicts):
    # returns replaced words
    line = ""
    keys = dicts.keys()
    for text in texts:
        if text not in keys:
            line += text
        else:
            line += dicts[text]
    return line


def text_coder(texts, shift):
    dicts = var(int(shift))
    code = encode(texts, dicts)
    return code


def textfile_coder():
    # enter inputs
    file_in = input("Enter filename:\n")
    shift = input("Enter the number of places you want to shift:\n")
    dicts = var(int(shift))
    coded = []
    # open file
    with open(file_in, "r", encoding='utf-8', errors='replace') as filename:
        texts = filename.read().splitlines()
        for text in texts:
            code = encode(text, dicts)
            coded.append(code)
    # write file
    with open(file_in, "w", encoding='utf-8', errors='replace') as filename:
        for code in coded:
            filename.write(code + "\n")
