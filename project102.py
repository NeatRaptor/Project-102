def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def rem(x, y):
    return x % y


number1 = int(input("\nEnter first number: "))
number2 = int(input("Enter second number: "))
print()
print("Select Operation: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Remainder")
choice = input("\nEnter choice 1/2/3/4/5: ")

if choice == "1":
    print("\nSum is " + str(add(number1, number2)))
elif choice == "2":
    print("\nDifference is " + str(sub(number1, number2)))
elif choice == "3":
    print("\nProduct is " + str(mul(number1, number2)))
elif choice == "4":
    print("\nQuotient is " + str(div(number1, number2)))
elif choice == "5":
    print("\nRemainder is " + str(rem(number1, number2)))
else:
    print("Invalid input")
