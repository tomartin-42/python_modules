import random
import argparse
import signal

msg_init = "This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n"


parser = argparse.ArgumentParser(description = msg_init)
args = parser.parse_args()

def init_guess():
    print(msg_init)
    global num
    num = random.randint(0, 99)

def handler(signum, frame):
    if signum == signal.SIGINT:
        print('Goodbye!')
    exit(0)

def game():
    trys = 1
    while True:
        data = input("What's your guess between 1 and 99\n")
        if data == '':
            pass
        elif data == 'exit':
            print('Goodbye!')
            break
        elif any(not i.isdigit() for i in data):
            print('That\'s not a numbre.')
        elif data == str(num):
            if trys == 1:
                if num == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print(f'You won in {trys} attempts!')
            break
        elif int(data) < num:
            print('Too low!')
            trys += 1
        elif int(data) > num:
            print('Too high!')
            trys += 1

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    init_guess()
    try:
        game()
    except EOFError:
        print('Goodbye!')
        exit(0)
