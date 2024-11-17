import random   # https://docs.python.org/3/library/random.html
from menus import welcome_menu
# import tutorial
from substitutions_pkg.handle_alpha import get_alpha, alpha_options, handle_words
from substitutions_pkg.handle_numeric import get_numbers

welcome_menu()

alpha_component = get_alpha()
numeric_component = get_numbers()

print("Now I'm going to make some replacements in the alphabetical string. Let me give you a few options to choose from...")

alpha_opts = alpha_options(alpha_component)

option_1 = handle_words(alpha_component)
option_2 = handle_words(alpha_component)
option_3 = handle_words(alpha_component)
option_4 = handle_words(alpha_component)

# alpha_opts = [option_1, option_2, option_3, option_4]

# print(alpha_opts)







print("meanwhile back at main.py 💫")
