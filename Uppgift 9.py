import random




def game(antal, max_tal):
    correct_answers = 0

    for i in range(antal):
        a = random.randint(1, max_tal)
        b = random.randint(1, max_tal)

        while True:
            answer = input(f"{a}+{b}")
            try:
                number = int(answer)
                break
            except ValueError:
                print("Det måste vara en siffra, försök igen")
        if number == a + b:
            print("Rätt!")
            correct_answers += 1

        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

    print(f"Du fick {correct_answers} av {antal} rätt.")


if __name__ == '__main__':
    try:
        antal = int(input("Hur många uppgifter vill du lösa?"))
        max_tal = int(input("Hur stort ska det största talet vara?"))
    except ValueError:
        print("Du skrev en bokstav. Då blir det 3 ")
        antal = 3
        max_tal = 10
    game(antal, max_tal)
