import random   # https://docs.python.org/3/library/random.html
from menus_main import welcome_menu
# import tutorial
from substitutions_pkg.handle_alpha import get_alpha, get_alpha_approval
from substitutions_pkg.handle_numeric import get_numbers
from substitutions_pkg.handle_extras import handle_short_entries, get_pwroot_approval

welcome_menu()

alpha_component = get_alpha()
alpha_submission = alpha_component.copy()   # preserve original submission
numeric_component = get_numbers()

alpha_component = get_alpha_approval(alpha_submission, alpha_component)

alpha_component, numeric_component = handle_short_entries(alpha_component, numeric_component)

pwroot = get_pwroot_approval(alpha_component, numeric_component)




    



print("meanwhile back at main.py 💫")
# print("alpha_component", alpha_component)
# print("numeric_component", numeric_component)
print("pwroot", pwroot)



'''
WORK STILL TO DO:
    - Split alpha_component if one string
    - Split numeric_component if one string > 3 (offer splits for 2)
    - Let user choose first/second/penultimate/last, character/letter/consonant/vowel, y-interpretation, number-interpretation
    
    # TODO: def set_variables():
    # TODO: def choose_variable():
    # TODO: def place_variable():

'''