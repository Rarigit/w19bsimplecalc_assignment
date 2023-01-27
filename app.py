import Calculations.addition as addition
import Calculations.subtraction as subtraction
import Calculations.multiplication as multiplication
import Calculations.division as division



print("This is the simple Calculator. Select from the following options:")
print("1.) Add two numbers")
print("2.) Subtract two numbers")
print("3.) Multiply two numbers")
print("4.) Divide two numbers")


is_valid = False

while not is_valid:
    choice0 = (input("Please enter your selection:"))
    # choice1 = (input("Enter first number:"))
    # choice2 = (input("Enter first number:"))
    try:
        choice0 = int(choice0)
        # choice1 = int(choice1)
        # choice2 = int(choice2)
        is_valid = True
    except ValueError:
        print("WTF. GIMME A NUMBER SER!!!")

is_valid = False

while not is_valid:
    choice1 = (input("Enter first number:"))
    # choice1 = (input("Enter first number:"))
    # choice2 = (input("Enter first number:"))
    try:
        choice1 = int(choice1)
        # choice1 = int(choice1)
        # choice2 = int(choice2)
        is_valid = True
    except ValueError:
        print("WTF. GIMME A NUMBER SER!!!")

is_valid = False

while not is_valid:
    choice2 = (input("Enter second number:"))
    # choice1 = (input("Enter first number:"))
    # choice2 = (input("Enter first number:"))
    try:
        choice2 = int(choice2)
        # choice1 = int(choice1)
        # choice2 = int(choice2)
        is_valid = True
    except ValueError:
        print("WTF. GIMME A NUMBER SER!!!")


if choice0 == 1:
    result = addition.addition(choice1, choice2)
elif choice0 == 2: 
    result = subtraction.subtraction((choice1), (choice2))
elif choice0 == 3:
    result = multiplication.multiplication((choice1), (choice2))
elif choice0 == 4:
    result = division.division((choice1), (choice2))
else:
    print("Input Specified Options Only (1-4)!")


