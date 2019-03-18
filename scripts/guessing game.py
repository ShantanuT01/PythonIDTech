import random

#generates secret number
number = random.randint(1,100)
answer = None
while(answer != number):
    #checks to avoid bad user input
    try:
        answer = int(input("Guess a number: \n"))
        if(answer > number):
            print("Too high")
        elif(answer < number):
            print("Too low")
        else:
            print("Correct")
    except:
        print("Invalid Input! Type a number!")
