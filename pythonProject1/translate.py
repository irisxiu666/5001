""" A function that translate an English day to a Frensh day and test it."""


def translate(english_days):
    """ translate the name of a day in a week from English to French.

    :param english_days: string, a day in a week in English.
    :return: string, the French name for the day.
    """
    french_days = ''
    if english_days == 'Monday':
        french_days = 'lundi'
    elif english_days == 'Tuesday':
        french_days = 'mardi'
    elif english_days == 'Wednesday':
        french_days = 'mercredi'
    elif english_days == 'Thursday':
        french_days = 'jeudi'
    elif english_days == 'Friday':
        french_days = 'vendredi'
    elif english_days == 'Saturday':
        french_days = 'samedi'
    elif english_days == 'Sunday':
        french_days = 'dimanche'
    else:
        raise Exception("Days in wrong form!")
    return french_days


def text_english_to_french(english_days, expected):
    """ test the function of 'translate' and compare the
    actual output whether matches the expected.

    :param english_days: string, a day in English.
    :param expected: string, expected output of the function,which
    is French name of the english_days.
    :return: None
    """
    actual = translate(english_days)
    if actual == expected:
        print('Test passed:', english_days, 'translates to French is', actual)
    else:
        print('Test failed:', english_days, 'should be', expected,
              'in French not the', actual)


def main():
    # tests should include seven different days.
    text_english_to_french('Monday', 'lundi')
    text_english_to_french('Tuesday', 'mardi')
    text_english_to_french('Wednesday', 'mercredi')
    text_english_to_french('Thursday', 'jeudi')
    text_english_to_french('Friday', 'vendredi')
    text_english_to_french('Saturday', 'samedi')
    text_english_to_french('Sunday', 'dimanche')


if __name__ == '__main__':
    main()
