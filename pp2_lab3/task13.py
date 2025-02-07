import random
def a():
    print("Hello! What is your name?")
    a=input()
    print("Well,"+a+", I am thinking of a number between 1 and 20.")
    num=random.randint(1,20)
    popytka=0
    while True:
        print("Take a guess.")
        b=int(input())
        popytka+=1
        if b<num:
            print("Your guess is too low.")
        elif b>num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {a}! You guessed my number in {popytka} guesses!")

a()