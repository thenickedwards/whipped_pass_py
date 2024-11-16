import random   # https://docs.python.org/3/library/random.html
import re
from sub_dicts import words_subs_dict, alpha_subs_dict, numeric_subs_dict, allowed_symbols, commonly_prohibited_chars


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