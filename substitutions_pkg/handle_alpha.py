import random   # https://docs.python.org/3/library/random.html
from sub_dicts import words_subs_dict, alpha_subs_dict, numeric_subs_dict, allowed_symbols, commonly_prohibited_chars

'''
The first input from the user that will be used to create the base password will be a few words or a phrase. If the phrase is close to a sentence, the program will attempt to reduce the characters with simple replacements (e.g. 4 = for, u = you, etc) or take the first letter of each word to create an acronym or an initialism.
'''

def validate_words(_list):
    # if only one word and less than 5 characters
    print(_list)
    if len(_list) == 1 and len(_list[0]) < 5:
        return 0
    # if more than 5 words
    if len(_list) > 5:
        return 0
    else:
        return 1

def handle_words(_list):
    print(_list)
    for i in _list:
        # commonly prohibited sub
        if i in commonly_prohibited_chars:
            pass
        # if already a symbol skip
        if i in allowed_symbols or i in allowed_symbols:
            continue
        # commmon word replacements
        if i in words_subs_dict:
            idx = _list.index(i)
            _list[idx] = random.choice(words_subs_dict[i])
            continue
        # randomize a 1-3 replacements in each word
        subs = random.randint(1, 3)
        for s in range(1, subs):
            letter_to_replace = random.choice(i)
            key = letter_to_replace.lower()
            possible_replacement = random.choice(alpha_subs_dict[key])
            new_word = i.replace(letter_to_replace, possible_replacement)        
            idx = _list.index(i)
            _list[idx] = i = new_word
            continue
    print("_list", _list)
    return _list
        
        


##########     DRIVER CODE     ##########
test_1 = ["brush", "teeth"]
test_2 = ["Bert", "Ernie"]
test_3 = ["travel", "to", "France"]
test_4 = ["win", "a", "million"]
test_5 = ["quit", "dayjob"]
test_6 = ["abc"]
test_7 = ["a", "b", "c", "d", "e", "f"]

# handle_words(test_1)
# handle_words(test_2)
# handle_words(test_3)
# handle_words(test_4)
handle_words(test_5)

# validate_words(test_1)
# validate_words(test_2)
# validate_words(test_3)
# validate_words(test_4)
# validate_words(test_5)
# validate_words(test_6)
