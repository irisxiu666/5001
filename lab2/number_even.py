""" A program to judge whether an integer is odd or even."""


def main():
    # Input the number with integer type.
    number = int(input('Input number: '))
    # Assuming the reminder of the number dividing by 2 is 0,
    # the number is even and print it out.
    if number % 2 == 0:
        print(number, 'is even')
    # Assuming the reminder of the number dividing by 2 isn't 0,
    # the number is odd and print it out.
    else:
        print(number, 'is odd')


if __name__ == '__main__':
    main()
