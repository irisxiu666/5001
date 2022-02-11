""" A program to decide whether buying a new stock and buying how much
    when we know the range of stock rating."""


def main():
    # Input the rating of the stock.
    rating = float(input('Input rating: '))
    # When the rating is over 100, the system prints 'Buy a lot'.
    if rating > 100:
        print('Buy a lot')
    # When the rating is above 76 and no higher than 100,
    # the system prints 'Buy a little'.
    elif 100 >= rating > 76:
        print('Buy a little')
    # When the rating is between 50 and 76, the output is 'Stay'.
    elif 50 <= rating <= 76:
        print('Stay')
    # When the rating is lower than 50 but above 25, the output is 'Sell'.
    elif 25 < rating < 50:
        print('Sell')
    # When the rating is 25 or less than 25, the output is 'Sell! Sell! Sell!'.
    else:
        print('Sell! Sell! Sell!')


if __name__ == '__main__':
    main()
