import random


def game():
    correct_answers = 0
    i = int(input("Hur många uppgifter vill du lösa?"))
    for i in range(i):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(f"{a}+{b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1

        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

    print(f"Du fick {correct_answers} av {i} rätt.")


if __name__ == '__main__':
    game()
