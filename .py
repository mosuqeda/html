import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guest a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry your guest To low. ")
        elif guess > random_number:
            print("Sorry your guess To high. ")
            
    print(f"Congrats you guess the right number {random_number}")
    
guess(100)