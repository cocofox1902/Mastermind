#!/usr/bin/python3
import random
import os
from colorama import Fore

def clear():
    os.system("clear")

def print_mastermind_board(user_try, code_to_guess, the_hint):
    print("    |", end="")
    [print("\t" + x[:3], end="") for x in user_try]
    print()
    for i in reversed(range(len(code_to_guess))):
        print("-----------------------------------------")
        print(the_hint[i][0], the_hint[i][1], "|")
        print(the_hint[i][2], the_hint[i][3], end=" |")
        [print("\t" + x[:3], end="") for x in code_to_guess[i]]
        print()
    print("-----------------------------------------")

def create_code():
    random.shuffle(colors)
    user_try = colors[:4]
    print("The code is: ", user_try)
    result_2 = input("is it good ? (y/n)\n")
    while result_2 == "y":
        random.shuffle(colors)
        user_try = colors[:4]
        print("The code is: ", user_try)
        result_2 = input("is it good ? (y/n)\n")
    return (user_try)

if __name__ == '__main__':
    colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "MAGENTA"]
    colors_value = {1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE", 5:"BLACK", 6:"MAGENTA"}
    random.shuffle(colors)
    user_try = colors[:4]
    chances = 8
    pswd = ['UNK', 'UNK', 'UNK', 'UNK']
    code_to_guess = [['-', '-', '-', '-'] for x in range(chances)]
    the_hint = [['-', '-', '-', '-'] for x in range(chances)]
    clear()
    print("-----------------------------------------")
    print("Menu")
    print("-----------------------------------------")
    result = input("Do you want to create the code? (y/n)\n")
    if result == "y":
        user_try = create_code()
    elif result == "n":
        pass
    else:
        print("error")
        exit()
    turn = 0
    while turn < chances:
        print("Enter code using numbers.")
        print("1 - ", Fore.RED + "RED", Fore.RESET + ", 2 - ", Fore.GREEN + "GREEN", Fore.RESET + ", 3 - ", Fore.YELLOW + "YELLOW", Fore.RESET + ", 4 - ", Fore.BLUE + "BLUE", Fore.RESET + ", 5 - ", Fore.BLACK +"BLACK", Fore.RESET + ", 6 - ", Fore.MAGENTA + "MAGENTA", Fore.RESET)
        print("Example: RED GREEN BLACK MAGENTA ---> 1 2 5 6")
        print("-----------------------------------------")
        print_mastermind_board(pswd, code_to_guess, the_hint)
        try:
            code = list(map(int, input("Enter your choice (put space between numbers) = ").split()))
        except ValueError:
            clear()
            print("-----------------------------------------")
            print("Wrong choice")
            print("-----------------------------------------")
            continue
        if len(code) != 4:
            clear()
            print("-----------------------------------------")
            print("Wrong choice")
            print("-----------------------------------------")
            continue
        flag = 0
        for x in code:
            if x > 6 or x < 1:
                flag = 1
        if flag == 1:
            clear()
            print("-----------------------------------------")
            print("Wrong choice")
            print("-----------------------------------------")
            continue
        for i in range(4):
            code_to_guess[turn][i] = colors_value[code[i]]
        dummy_user_try = [x for x in user_try]
        pos = 0
        for x in code:
            if colors_value[x] in dummy_user_try:
                if code.index(x) == user_try.index(colors_value[x]):
                    the_hint[turn][pos] = 'R'
                else:
                    the_hint[turn][pos] = 'W'
                pos += 1
                dummy_user_try.remove(colors_value[x])
        random.shuffle(the_hint[turn])
        if code_to_guess[turn] == user_try:
            clear()
            print_mastermind_board(user_try, code_to_guess, the_hint)
            print("-----------------------------------------")
            print("-----------------------------------------")
            print("-----------------------------------------")
            print("WIN")
            print("-----------------------------------------")
            print("-----------------------------------------")
            print("-----------------------------------------")
            break
        turn += 1
        clear()

if turn == chances:
    clear()
    print_mastermind_board(user_try, code_to_guess, the_hint)
    print("-----------------------------------------")
    print("LOSE")
    print("-----------------------------------------")
