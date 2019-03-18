while True:
    try:
        x = input("Enter an equation:")
        print(eval(x))
    except:
        print("Invalid Input!")
    
