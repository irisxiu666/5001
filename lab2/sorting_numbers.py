""" A program to sort three numbers input by a user."""


def main():
    # Input three numbers.
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    num3 = float(input('Input third number: '))
    # Compare the size of three numbers, and there are six situations in total.
    # Print these three numbers in oder from smallest to largest.
    if num1 < num2 < num3:
        print(str(num1) + ', ' + str(num2) + ', ' + str(num3))
    if num2 < num1 < num3:
        print(str(num2) + ', ' + str(num1) + ', ' + str(num3))
    if num2 < num3 < num1:
        print(str(num2) + ', ' + str(num3) + ', ' + str(num1))
    if num1 < num3 < num2:
        print(str(num1) + ', ' + str(num3) + ', ' + str(num2))
    if num3 < num1 < num2:
        print(str(num3) + ', ' + str(num1) + ', ' + str(num2))
    if num3 < num2 < num1:
        print(str(num3) + ', ' + str(num2) + ', ' + str(num1))


if __name__ == '__main__':
    main()
