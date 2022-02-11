""" Functions to compare two or four numbers to find
the largest one and test them."""


def biggest(num1, num2):
    """compare two numbers and return the larger one.

    :param num1: float or integer, one of the numbers to be compared.
    :param num2: float or integer, the other of the number to be compared.
    :return: float or integer, the larger one of num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2


def biggest_of_four(num3, num4, num5, num6):
    """ quote the function above to find the largest number among four numbers.

    :param num3: float or integer, one of the numbers to be compared.
    :param num4: float or integer, another number to be compared.
    :param num5: float or integer, the third number to be compared.
    :param num6: float or integer, the fourth number to be compared.
    :return: float or integer, the largest one among four numbers.
    """
    return biggest(biggest(num3, num4), biggest(num5, num6))


def test_biggest(num1, num2, expected):
    """ A function to test 'biggest' above.

    :param num1: float or int, a number to be compared.
    :param num2: float or int, the second number to be compared.
    :param expected: float or int, expected the larger number
    between num1 and num2.
    :return: None
    """
    actual = biggest(num1, num2)
    if actual == expected:
        print('Test passed: the biggest number is ', actual)
    else:
        print('Test failed: the biggest number is ', expected, 'not', actual)


def test_biggest_of_four(num3, num4, num5, num6, expected):
    """ A function to test 'biggest_of_four' above.

    :param num3: float or int, a random number to be compared.
    :param num4: float or int, a random number to be compared.
    :param num5: float or int, a random number to be compared.
    :param num6: float or int, a random number to be compared.
    :param expected: float or int, expected output of the function.
    :return: None
    """
    actual = biggest_of_four(num3, num4, num5, num6)
    if actual == expected:
        print('Test passed: the biggest number is ', actual)
    else:
        print('Test failed: the biggest number is ', expected, 'not', actual)


def main():
    # tests should include different situations,
    # and every number could be possibly the largest one.
    test_biggest(34, 98, 98)
    test_biggest(101, 25, 101)
    test_biggest(66, 66, 66)
    test_biggest_of_four(12, 45, 32, 88, 88)
    test_biggest_of_four(67, 22, 43, 27, 67)
    test_biggest_of_four(19, 520, 432, 123, 520)
    test_biggest_of_four(77, 521, 4500, 68, 4500)


if __name__ == '__main__':
    main()
