import random
import sys
import argparse

msg_init = "This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n"


parser = argparse.ArgumentParser(description = msg_init)
args = parser.parse_args()

def init_guess():
    print(msg_init)
    global num
    num = random.randint(0, 99)

def game():
    trys = 0
    while True:
        data = input("What's your guess between 1 and 99\n")
        if data == 'exit':
            break
        elif any(not i.isdigit() for i in data):
            print('That\'s not a numbre.')
        elif data == str(num):
            print(f'You won in {trys} attempts!')
            break
        elif int(data) < num:
            print('Too low!')
            trys += 1
        elif int(data) > num:
            print('Too high!')
            trys += 1

if __name__ == '__main__':
    init_guess()
    game()
