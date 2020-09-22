def main():
    user_input = input("Skriv en mening: ").lower().replace(" ", "")
    print(user_input)
    #print(len(user_input))
    reversed_user_input = user_input[::-1]
    print(reversed_user_input)
    if user_input == reversed_user_input:
        print("Ditt ord är en palindrom")
    else:
        print("Ditt ord är inte en palindrom")


if __name__ == '__main__':
    main()
