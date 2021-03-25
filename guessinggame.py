import random
import time
guess=0
number = random.randint(1,10)
tries=0

name = input("HOWDY! May i know your name? ")
print(f"hello {name}.")

question = input("Are you ready to guess? [Y/N] ")
if question.lower() =='n':
    print("Oh! Okay. Bye")
    exit()
if question.lower == 'y':
    print("I'm thinking of a number between 1 & 10")
    time.sleep(1)

while not(guess == number):
    guess = int(input("what's your guess? "))
    time.sleep(1)
    tries=tries+1
    if guess==number:
        print("Brilliant!")
        time.sleep(1)
        print(f"Congrats. Your guess was correct, the number was indeed {guess}")
        time.sleep(1)
        print(f"It has taken you {tries}")
    elif guess < number:
        time.sleep(1)
        print("Guess higher")
    elif guess > number:
        time.sleep(1)
        print("Guess lower")

