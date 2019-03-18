import random
num = None
def diceRoll(low, high):
    low = None
    high = None
    try:
        while((low != None) and (high != None)
        low =input("Enter lowest value:"))
        high = int(input("Enter lowest value:"))
    except:
        print("Invalid input!")
    try:
        num = random.randint(l,high)
    except:
        print("Check values")
        continue
diceRoll()
            
              
