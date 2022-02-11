''' A function to simulate a bank machine and its process to withdraw money.
    amount_money: the requested money to withdraw.
    count: the amount money of different denominations.'''


def atm(amount_money):
    amount_money = float(input('Input request: '))
    # round amount_money to 2nd digit
    amount_money = round(amount_money, 2)
    # convert amount_money to cents
    amount_money = int(amount_money * 100)
    # calculate the amount of money in fifty value.
    count = amount_money // 5000
    if count == 1:
        print(count, "fifty")
    elif count > 1:
        print(count, "fifties")
    amount_money %= 5000
    # calculate the amount of money in twenty value.
    count = amount_money // 2000
    if count == 1:
        print(count, "twenty")
    elif count > 1:
        print(count, "twenties")
    amount_money %= 2000
    # calculate the amount of money in ten value.
    count = amount_money // 1000
    if count == 1:
        print(count, "ten")
    elif count > 1:
        print(count, "tens")
    amount_money %= 1000
    # calculate the amount of money in five value.
    count = amount_money // 500
    if count == 1:
        print(count, "five")
    elif count > 1:
        print(count, "fives")
    amount_money %= 500
    # calculate the amount of money in toony value.
    count = amount_money // 200
    if count == 1:
        print(count, "toony")
    elif count > 1:
        print(count, "toonies")
    amount_money %= 200
    # calculate the amount of money in loony value.
    count = amount_money // 100
    if count == 1:
        print(count, "loony")
    elif count > 1:
        print(count, "loonies")
    amount_money %= 100
    # calculate the amount of money in quarter value.
    count = amount_money // 25
    if count == 1:
        print(count, "quarter")
    elif count > 1:
        print(count, "quarters")
    amount_money %= 25
    # calculate the amount of money in dime value.
    count = amount_money // 10
    if count == 1:
        print(count, "dime")
    elif count > 1:
        print(count, "dimes")
    amount_money %= 10
    # calculate the amount of money in nickel value.
    count = amount_money // 5
    amount_money %= 5
    if amount_money >= 3:
        count += 1
    if count == 1:
        print(count, "nickel")
    elif count > 1:
        print(count, "nickels")


def test_atm(amount_money, expected):
    actual = str(atm(amount_money))
    if actual == expected:
        print('Test passed:', actual, 'is equal to', expected)
    else:
        print('Test failed:', actual, 'is not equal to',expected)


def main():
    test_atm(98.22, '1 fifty 2 twenties 1 five 1 toony 1 loony 2 dimes')


if __name__ == "__main__":
    main()
