import random   # https://docs.python.org/3/library/random.html
from menus import welcome_menu
# import tutorial
from substitutions_pkg.handle_alpha import get_alpha, get_alpha_options
from substitutions_pkg.handle_numeric import get_numbers

welcome_menu()

alpha_component = get_alpha()
alpha_submission = alpha_component.copy()
numeric_component = get_numbers()

print("Now I'm going to make some replacements in the alphabetical string. Let me give you a few options to choose from...")

alpha_approval = False
while alpha_approval == False:
    alpha_options = get_alpha_options(alpha_component)
    print(f"\nWe started with {alpha_submission}.")
    for i, opt in enumerate(alpha_options):
        print(f"{i+1}. The alphabetic string {alpha_submission} could become {opt}")
    
    user_approval = input(f"\nWhich of the above would you like to use for your password?\nEnter 1, 2, 3, or 4. Or if would you rather send it through another series of randomized replacements hit enter: ")
    if user_approval == "1":
        alpha_component = alpha_options[0]
        alpha_approval = True
    elif user_approval == "2":
        alpha_component = alpha_options[1]
        alpha_approval = True
    elif user_approval == "3":
        alpha_component = alpha_options[2]
        alpha_approval = True
    elif user_approval == "4":
        alpha_component = alpha_options[4]
        alpha_approval = True
    else:
        alpha_component = alpha_submission
        continue
    





print("meanwhile back at main.py 💫")
