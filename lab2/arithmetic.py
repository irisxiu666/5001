""" A arithmetic program to deal with '+,-,*,/' operators between
    two numbers and take invalid situations into consideration,
    such as invalid operators and divisors."""


def main():
    # Input two numbers and operators.
    number1 = float(input('Input first number: '))
    number2 = float(input('Input second number: '))
    input_operator = input('Input operator (+,-,*,/): ')
    # Assuming operators are "+,-,*,/" respectively
    # and print out the operation result.
    if input_operator == '+':
        print(number1, input_operator, number2, '=', number1 + number2)
    elif input_operator == '-':
        print(number1, input_operator, number2, '=', number1 - number2)
    elif input_operator == '*':
        print(number1, input_operator, number2, '=', number1 * number2)
    # When operator is '/', invalid situation that number2
    # is 0 is taken into consideration.
    elif input_operator == '/':
        if number2 != 0:
            print(number1, input_operator, number2, '=', number1 / number2)
        else:
            print(number1, input_operator, int(number2), '= NaN')
    # When operators are invalid, print
    # 'Invalid operator. Please use +,-,*,/.'.
    else:
        print('Invalid operator. Please use +,-,*,/.')


if __name__ == '__main__':
    main()
