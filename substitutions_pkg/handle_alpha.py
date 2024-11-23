# to run file directly use module flag
# python -m substitutions_pkg.handle_alpha
import random   # https://docs.python.org/3/library/random.html
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .sub_dicts import words_subs_dict, alpha_subs_dict, numeric_subs_dict, allowed_symbols, commonly_prohibited_chars



def get_alpha():
    while True:
        print("We'll start with the alphabetical component.")
        print("Don't worry about adding symbols (or numbers just yet), I can do that for you. Though, if there's a symbol you want to make sure is part of the alphabetical component feel free to include it and I'll try to preserve them. You will have a chance to add numbers momentarily.")
        alpha_submission = input("Give me a couple of words that we can use for your password: ")
        _list = alpha_submission.split()
        if validate_words(_list) == 0:
            print("Let's try again!\n")
            continue
        if validate_words(_list) == 1:
            print("Looks good. Let me give you a few options to choose from for the alphabetical component.")
            alpha_list = alpha_submission.split()
            print("alpha_list", alpha_list)
            return alpha_list


def validate_words(_list):
    # if user input fails validation return 0, else 1
    # remove commonly prohibited characters
    for word in _list:
        for char in word:
            if char in commonly_prohibited_chars:
                print(f"I found the character '{char}' which is prohibited by most logins, so I'm just going to remove it.")
                new_word = word.replace(char, "")
                idx = _list.index(word)
                _list[idx] = word = new_word
                print(_list)
    # if less than 8 characters
    if len(''.join(_list)) < 8:
        print("I need at least 8 characters to work with to meet minimum character requirements for most logins.")
        return 0
    # if more than 12 characters
    if len(''.join(_list)) > 12:
        print("That's probably too many characters for most logins. Please enter a few words that are 8 - 12 characters.")
        return 0
    else:
        return 1


def handle_words(_list):
    # print("_list out side i loop", _list)
    for i in _list:
        # commmon word replacements
        if i in words_subs_dict:
            idx = _list.index(i)
            common_replacement = random.choice(words_subs_dict[i])
            _list[idx] = common_replacement
            continue
        # if already a symbol or number skip
        if i in allowed_symbols or i in numeric_subs_dict:
            continue
        # randomize a 1-3 replacements in each word
        subs = random.randint(1, 3)
        for s in range(subs):
            letter_to_replace = random.choice(i)
            # if already a symbol or number skip
            if letter_to_replace in allowed_symbols or letter_to_replace in numeric_subs_dict:
                continue
            key = letter_to_replace.lower()
            possible_replacement = random.choice(alpha_subs_dict[key])
            new_word = i.replace(letter_to_replace, possible_replacement, 1)
            # print(f"I'm replacing {letter_to_replace} with {possible_replacement}.\nSo now {i} will be {new_word}")
            idx = _list.index(i)
            _list[idx] = i = new_word
            continue
    # print("_list finished the loop", _list)
    return _list

def get_alpha_options(_list):
    options = [handle_words(_list.copy()) for i in range(4)]
    # print("options", options)
    return options


##########     DRIVER CODE     ##########
test_1 = ["brush", "teeth"]
test_2 = ["Bert", "Ernie"]
test_3 = ["travel", "to", "France"]
test_4 = ["win", "a", "million"]
test_5 = ["you're", "awesome"]

# handle_words(test_1)
# handle_words(test_2)
# handle_words(test_3)
# handle_words(test_4)
# handle_words(test_5)

# test_6 = ["abc"]
# test_7 = ["a", "b", "c", "d", "e", "f"]
# test_8 = ["test", "r~m[]ve"]

# validate_words(test_4)
# validate_words(test_5)
# validate_words(test_6)
# validate_words(test_7)
# validate_words(test_8)

# get_alpha_options(test_1)





