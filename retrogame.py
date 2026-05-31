import random
from colorama import init, Fore

init()

while True:
    print(Fore.CYAN + '''
    1. To Try Your Luck
    2. Exit (Dar gya !!!)
    ''')

    try:
        choice = int(input(Fore.GREEN + 'Bata bhai kya krne hai : '))
    except ValueError:
        print(Fore.RED + 'Please enter a valid number.')
        continue

    if choice == 1:
        computer_choice = random.randint(1, 10)
        try:
            user_value = int(input(Fore.CYAN + 'Enter number from 1 to 10 & win 2 x Money : '))
        except ValueError:
            print(Fore.RED + 'Please enter a valid number.')
            continue

        if 1 <= user_value <= 10:
            if computer_choice == user_value:
                print(Fore.MAGENTA + 'Congratulations You win ')
            else:
                print(Fore.RED + 'Better Luck Next time ')
        else:
            print(Fore.RED + 'Enter Correct value in range 1 to 10 ')
    elif choice == 2:
        print(Fore.CYAN + 'Bhai tu dar gya !!! ')
        break
    else:
        print(Fore.RED + 'Sahi Option select kr le ')