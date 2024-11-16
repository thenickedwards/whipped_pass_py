import random   # https://docs.python.org/3/library/random.html
from sub_dicts import words_subs_dict, alpha_subs_dict, numeric_subs_dict, allowed_symbols, commonly_prohibited_chars

'''
The first input from the user that will be used to create the base password will be a few words or a phrase. If the phrase is close to a sentence, the program will attempt to reduce the characters with simple replacements (e.g. 4 = for, u = you, etc) or take the first letter of each word to create an acronym or an initialism.
'''

def validate_words(_list):
    print(_list)
    # if user input fails validation return 0, else 1
    # if only one word and less than 5 characters
    if len(_list) == 1 and len(_list[0]) < 5:
        print("I need a bit more to work with to meet minimum character requirements for most logins.")
        return 0
    # if more than 5 words
    if len(_list) > 4:
        print("That's probably too many chracters for most logins.")
        return 0
    # remove commonly prohibited characters
    for word in _list:
        for char in word:
            if char in commonly_prohibited_chars:
                print(f"I found {char} which is prohibited by most logins, so I'm just going to remove it.")
                new_word = word.replace(char, "")
                idx = _list.index(word)
                _list[idx] = word = new_word
                print(_list)
    else:
        return 1

def handle_words(_list):
    print(_list)
    for i in _list:
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
test_5 = ["you're", "awesome"]

# handle_words(test_1)
# handle_words(test_2)
# handle_words(test_3)
# handle_words(test_4)
# handle_words(test_5)

test_6 = ["abc"]
test_7 = ["a", "b", "c", "d", "e", "f"]
test_8 = ["test", "r~m[]ve"]

# validate_words(test_4)
# validate_words(test_5)
# validate_words(test_6)
# validate_words(test_7)
# validate_words(test_8)
