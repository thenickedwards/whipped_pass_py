import random   # https://docs.python.org/3/library/random.html
from menus import welcome_menu
# import tutorial
from substitutions_pkg.handle_alpha import get_alpha, get_alpha_options, get_alpha_approval
from substitutions_pkg.handle_numeric import get_numbers

welcome_menu()

alpha_component = get_alpha()
alpha_submission = alpha_component.copy()
numeric_component = get_numbers()

print("Now I'm going to make some replacements in the alphabetical string. Let me give you a few options to choose from...")

alpha_component = get_alpha_approval(alpha_submission, alpha_component)

    




print("alpha_component", alpha_component)
print("meanwhile back at main.py 💫")
