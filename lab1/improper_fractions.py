def main(number):
    """ Return None
    Define the function that convert a floating point number to
    an improper fraction over 100.

    y: input of the floating number.
    """
    print(str(float(number)) + ' is ' + str(int(float(number) * 100)) + '/100')


if __name__ == '__main__':
    # Input a floating point number.
    input_number = input('Enter a floating point number:')
    # Call function.
    main(input_number)
