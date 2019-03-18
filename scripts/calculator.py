while True:
    try:

        equation = eval(input("Enter an equation: "))
        print(equation)
    except:
        print("Invalid Input!")
