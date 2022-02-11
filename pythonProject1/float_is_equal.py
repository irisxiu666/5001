""" A function to compare the difference of two float
    numbers whether exceeds the threshold and test it."""


from math import fabs


def float_is_equal(num1, num2, threshold):
    """ Compare the difference of num1 and num2 whether exceeds
    the threshold.

    :param num1: float or int, any number can be input.
    :param num2: float or int, any number can be input.
    :param threshold: float, the minimum value of the difference
    between num1 and num2 if they are equal.
    :return: boolean, True if the difference of num1 and num2 doesn't
    exceed threshold, false otherwise.
    """
    if fabs(num1 - num2) <= threshold:
        return True
    else:
        return False


def test_float_is_equal(num1, num2, threshold, expected):
    """ test the function 'float_is_equal' and compare the actual
    output with the expected ones.

    :param num1: float or int, any number can be input.
    :param num2: float or int, any number can be input.
    :param threshold: float, the minimum value of the difference
    between num1 and num2 if they are equal.
    :param expected: boolean, expected output of the function.
    :return: None
    """
    actual = float_is_equal(num1, num2, threshold)
    if actual == expected:
        print('Test passed:', actual, 'is equal to', expected)
    else:
        print('Test failed:', actual, 'is not equal to', expected)


def main():
    # tests should include both equal float numbers
    # and not equal float numbers.
    test_float_is_equal(3.1415, 3.141592, 0.001, True)
    test_float_is_equal(6.67777, 6.67778, 0.0001, True)
    test_float_is_equal(1.414, 1.41429, 0.000001, False)
    test_float_is_equal(43.33333, 43.33, 0.0003, False)


if __name__ == '__main__':
    main()
