""" A program that is able to convert a number between 1 and 4999 (inclusive)
    to a roman numeral with variables, arithmetic operators, and functions."""


def main():
    # Input the number
    number = roman_num = int(input('Enter number:'))
    # The quotient gotten from 'number // 1000' is the number of 'M'
    # in the roman numeral system.
    num1 = number // 1000
    roman_num1 = 'M' * num1
    number = number - num1 * 1000
    # The quotient gotten from 'number // 500' is
    # the number of 'D' in the roman numeral system.
    num2 = number // 500
    roman_num2 = roman_num1 + 'D' * num2
    number = number - num2 * 500
    # The quotient gotten from 'number // 100' is
    # the number of 'C' in the roman numeral system.
    num3 = number // 100
    roman_num3 = roman_num2 + 'C' * num3
    number = number - num3 * 100
    # The quotient gotten from 'number // 50' is the number of 'L'
    # in the roman numeral system.
    num4 = number // 50
    roman_num4 = roman_num3 + 'L' * num4
    number = number - num4 * 50
    # The similar reason that 'num5','num6','nums7' is the number of
    # 'X','V' and 'I' in the roman numeral system.
    num5 = number // 10
    roman_num5 = roman_num4 + 'X' * num5
    number = number - 10 * num5
    num6 = number // 5
    roman_num6 = roman_num5 + 'V' * num6
    number = number - num6 * 5
    num7 = number // 1
    roman_num7 = roman_num6 + 'I' * num7
    # Print the final string using '+' to connect the
    # number of 'M','D','C','L','X','V',I'.
    print(roman_num, 'is', roman_num7)


if __name__ == '__main__':
    main()
