#!/usr/bin/python3


logo = __import__("calc_art").logo


def add(num1, num2):
    """adds two integers"""
    return num1 + num2


def mul(num1, num2):
    """multiplies two integers"""
    return num1 * num2


def sub(num1, num2):
    """subtracts two integers"""
    return num1 - num2


def div(num1, num2):
    """divides two integers"""
    if num2 != 0:
        return num1 / num2
    return 0


operators = {'+': add, '-': sub, '*': mul, '/': div}


def start_calc():
    """start basic calculator"""
    stored = False
    storedValue = 0
    stop = False

    print(logo)
    while not stop:
        if not stored:
            num1 = input("Input first value: ")
        else:
            num1 = storedValue
        for i in operators:
            print(i)
        operator = input("Pick an operator: ")
        if operator not in operators:
            print("Invalid operator")
        else:
            num2 = input("Input second value: ")
            try:
                num1 = float(num1) if '.' in str(num1) else int(num1)
                num2 = float(num2) if '.' in str(num2) else int(num2)
            except ValueError:
                print("Please input a number...")
            else:
                result = operators[operator](num1, num2)
                print(f"{num1} {operator} {num2} = {result}")
                if input(f"Would you like to carry out another"
                         f" operation with {result}? (y/n)") == 'y':
                    stored = True
                    storedValue = result
                else:
                    stored = False
                    if input("Would you like to carry out"
                             " another calculation? (y/n)") == 'n':
                        stop = True


if __name__ == "__main__":
    start_calc()
