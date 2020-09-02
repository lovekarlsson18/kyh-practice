import calc


def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 - multiply numbers")
    print("4 - divide numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))
    if answer == "1":
        result = calc.add(a, b)

    if answer == "2":
        result = calc.subtract(a, b)

    if answer == "3":
        result = calc.multiply(a, b)

    if answer == "4":
        result = calc.divide(a, b)

    print("Result = " + str(result))


if __name__ == '__main__':
    run()
