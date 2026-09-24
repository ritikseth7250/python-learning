import random
secret_number=random.randint(1,10)
Guess_number=int(input("Guess the number: "))
if Guess_number == secret_number:
    print("You gussed the number ")
else:
    print("Wrong guess") 
