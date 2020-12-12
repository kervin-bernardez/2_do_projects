from collections import deque


def shift_list(paramater, shift):
    # use deque datatype and rotate list
    shifted = deque(paramater)
    shifted.rotate(shift)
    return shifted


def var(shift):
    # var init
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "[]{}()+-*/:;<>,.?!_@#"
    # make shifted list
    s_letters = shift_list(letters, shift) + shift_list(letters.upper(), shift)
    s_numbers = shift_list(numbers, shift)
    s_symbols = shift_list(symbols, shift)
    # make shifted dictionary
    dicts = dict(zip(letters+letters.upper()+numbers+symbols,
                     s_letters+s_numbers+s_symbols))
    return dicts


def encode(texts, dicts):
    # replace words
    ntext = []
    keys = dicts.keys()
    for text in texts:
        if text not in keys:
            ntext.append(text)
        else:
            ntext.append(dicts[text])
    return "".join(ntext)


def main():
    # enter inputs
    input_file = input("Enter filename:\n")
    shift = int(input("Enter the number of places you want to shift:\n"))
    dicts = var(shift)
    coded = []
    # open file
    with open(input_file, "r", encoding='utf-8', errors='replace') as filename:
        texts = filename.read().splitlines()
        for text in texts:
            code = encode(text, dicts)
            coded.append(code)
    # write file
    with open(input_file, "w", encoding='utf-8', errors='replace') as filename:
        for code in coded:
            filename.write(code + "\n")
