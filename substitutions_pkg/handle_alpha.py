import random   # https://docs.python.org/3/library/random.html
# from sub_dicts import words_subs_dict, alpha_subs_dict, allowed_symbols, commonly_prohibited_chars
from substitutions_pkg.sub_dicts import words_subs_dict, alpha_subs_dict, allowed_symbols, commonly_prohibited_chars


def get_alpha():
    alpha_input = ""
    while alpha_input == "":
        print("We'll start with the alphabetical component.")
        print("Don't worry about adding symbols (or numbers), I can do that for you. Though, if there's a symbol you want to make sure are part of the alphabetical component feel free to include and I'll try to preserve them. You will have a chance to add numbers momentarily.")
        alpha_input = input("Give me a couple of words that we can use for your password: ")
        _list = alpha_input.split()
        if validate_words(_list) == 0:
            print("Let's try again!")
            continue
        if validate_words(_list) == 1:
            print("Looks good. Let me give you a few options to choose from for the alphabetical component.")
            alpha_list = alpha_input.split()
            print("alpha_list", alpha_list)
            return alpha_list
            



def validate_words(_list):
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
    return _list
        
        


##########     DRIVER CODE     ##########
# test_1 = ["brush", "teeth"]
# test_2 = ["Bert", "Ernie"]
# test_3 = ["travel", "to", "France"]
# test_4 = ["win", "a", "million"]
# test_5 = ["you're", "awesome"]

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

get_alpha()




# if __name__ == "__main__":
#     # This block runs only when the module is executed directly, not when imported
#     print("handle_alpha.py is running directly.")
#     get_alpha = get_alpha()
#     validate_words = validate_words()
#     handle_words = handle_words()
