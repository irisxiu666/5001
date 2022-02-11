''' A program to judge whether an integer value between 1
    and 5 (inclusive) is the same number with a text word.'''


def main():
    num = int(input('Enter integer value: '))
    word = input('Enter word: ')
    if num == 1 and word == 'one':
        print(num, 'and', word, 'are the same number')
    elif num == 2 and word == 'two':
        print(num, 'and', word, 'are the same number')
    elif num == 3 and word == 'three':
        print(num, 'and', word, 'are the same number')
    elif num == 4 and word == 'four':
        print(num, 'and', word, 'are the same number')
    elif num == 5 and word == 'five':
        print(num, 'and', word, 'are the same number')
    else:
        print(num, 'and', word, 'are Not the same number')


if __name__ == '__main__':
    main()
