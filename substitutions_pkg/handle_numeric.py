import random   # https://docs.python.org/3/library/random.html
import re
from substitutions_pkg.sub_dicts import words_subs_dict, alpha_subs_dict, allowed_symbols, commonly_prohibited_chars


def get_numbers():
    numbers_input = ""
    while numbers_input == "":
        print("Next, we'll get the numerical component.")
        numbers_input = input("Give me a a few numbers (2-5 digits in total) that we can use for your password: ")
        _list = numbers_input.split()
        if validate_numbers(_list) == 0:
            print("Let's try again!")
            continue
        if validate_numbers(_list) == 1:
            print("Looks good. Let me give you a few options to choose from for the alphabetical component.")
            nums_list = validate_numbers.split()
            print("alpha_list", nums_list)
            return nums_list


def validate_numbers(_list):
     # if user input fails validation return 0, else 1
     concat_nums = ''.join(_list)
     # if not all numbers
     if not re.match(r'\d{2,5}', concat_nums):
          print("Are those numbers? Let's try aagain for 2-5 digits in total.")
          return 0
     # if less than 2 or more than 5 digits
     if len(concat_nums) < 2:
          print("I need a bit more to work with to meet minimum character requirements for most logins.")
          return 0
     # if more than 5 words
     if len(concat_nums) > 5:
          print("That's probably too many chracters for most logins.")
          return 0
     # remove commonly prohibited characters
     for item in _list:
          for char in item:
               if char in commonly_prohibited_chars:
                    print(f"I found {char} which is prohibited by most logins, so I'm just going to remove it.")
                    new_word = item.replace(char, "")
                    idx = _list.index(item)
                    _list[idx] = item = new_word
     else:
          return 1


def handle_numbers(_list):
     pass





##########     DRIVER CODE     ##########
# test_1 = ["12", "25"]
# test_2 = ["2022"]
# test_3 = ["5", "5", "5"]
# test_4 = ["3", "5", "8"]
# test_5 = ["98118"]

# validate_numbers(test_1)
# validate_numbers(test_2)
# validate_numbers(test_3)
# validate_numbers(test_4)
# validate_numbers(test_5)

# test_6 = ["abcd"]
# test_7 = ["1234", "UnitB"]
# validate_numbers(test_6)
# validate_numbers(test_7)


# if __name__ == "__main__":
#     # This block runs only when the module is executed directly, not when imported
#     print("handle_numeric.py is running directly.")
#     get_numbers = get_numbers()
#     validate_numbers = validate_numbers()
#     handle_numbers = handle_numbers()