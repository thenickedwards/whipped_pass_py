import random   # https://docs.python.org/3/library/random.html
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from .sub_dicts import words_subs_dict, alpha_subs_dict, numeric_subs_dict, allowed_symbols, commonly_prohibited_chars

from menus_main import typing_print


def handle_short_entries(alpha_component, numeric_component):
    # alpha will be 8 - 12 characters after validation
    if len(alpha_component) == 1:
        print("Since we've only got one word, I'll randomize a split in the letters for enhanced security.")
        # print("alpha_component pre-split: ", alpha_component)
        one_word = alpha_component[0]
        # randomize split
        split_index = random.randint(1, len(one_word) - 2)
        # print("split_index", split_index)
        first_part = one_word[:split_index]
        second_part = one_word[split_index:]
        alpha_component = [first_part, second_part]
        typing_print(f"We'll go with '{alpha_component[0]}' and '{alpha_component[1]}'.", split="letter")
    # nums will be 2 - 5 digits after validation
    if len(numeric_component) == 1:
        print("Since we've only got one number, I'll randomize a split in the number for enhanced security.")
        # print("numeric_component pre-split: ", numeric_component)
        one_num = numeric_component[0]
        # randomize split
        split_index = random.randint(1, len(one_num) - 1)
        # print("split_index", split_index)
        first_part = one_num[:split_index]
        second_part = one_num[split_index:]
        numeric_component = [first_part, second_part]
        typing_print(f"We'll go with '{numeric_component[0]}' and '{numeric_component[1]}'.", split="letter")
    return alpha_component, numeric_component


def get_pwroot_approval(alpha_component, numeric_component):
    print("To make your password even more secure, let's insert the numbers in and alphabetical component. I'll give you a few options to choose from...\n")
    
    pwroot_options = []
    # Generate all possible valid insertions of numeric_component into alpha_component
    def get_pwroot_options(alpha, numerics, current, alpha_index, numeric_index):
        # If all numeric components placed, add alpha
        if numeric_index == len(numerics):
            pwroot_options.append(current + alpha[alpha_index:])
            return
        
        # Try insert of current numeric value at various positions in the alpha list
        for i in range(alpha_index, len(alpha) + 1):
            # Add the next numeric component into the combination
            get_pwroot_options(alpha, numerics, current + alpha[alpha_index:i] + [numerics[numeric_index]], i, numeric_index + 1)
    
    while True:
        get_pwroot_options(alpha_component, numeric_component, [], 0, 0)
        for i, opt in enumerate(pwroot_options):
            print(f"{i+1}. The password root could become {opt}")
        # after gerenerating options, allow user to choose
        user_approval = input(f"\nWhich of the above would you like to use for the root of your password?\nEnter 1 and {len(pwroot_options)}: ")
        try:
            user_approval = int(user_approval)
        except:
            print("Please enter a valid number.\n")
            continue
        if int(user_approval) >0 and int(user_approval) <= len(pwroot_options):
            pwroot = pwroot_options[int(user_approval)-1]
            return pwroot
        else:
            print("Let's try again!\n")
            continue







##########     DRIVER CODE     ##########
# test_1a = ["firebend"]
# test_1b = ["86"]
# test_2a = ["appreciation"]
# test_2b = ["1974"]
# test_3a = ["driftwoods"]
# test_3b = ["333"]
# test_4a = ["harnonizing"]
# test_4b = ["12345"]
# test_5a = ["adventure"]
# test_5b = ["1212"]

# handle_short_entries(test_1a, test_1b)
# handle_short_entries(test_2a, test_2b)
# handle_short_entries(test_3a, test_3b)
# # handle_short_entries(test_4a, test_4b)
# # handle_short_entries(test_5a, test_5b)