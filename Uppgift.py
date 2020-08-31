"""
Detta är ett ett "hängagubben" spel. Man får först fylla i sitt namn.
Sen kommer det en förklaring på vad spelet går ut
på. Man får reda på att det är en mening och att det finns chans att få hjälp om man behöver det.
Man har 10 chanser att svara fel.
Om man klarar utmaningen så får man reda på hur många gissningar man klarade utmaningen
på. Ifall man inte klarar utmaningen får man frågan om man vill försöka igen eller inte.
"""


def start():
    print("-------------------------------------------------")
    name = input("Write your name : ")
    print("Hello", name, ",", "Can you beat the challenge?")

    description = """
                This is a \"Hangman game\". 
                Can you guess the sentence in limited amount of guesses?
                
                If you need help, type "help".
                
                """
    print(description)


def main():
    start()
    game()


def game():
    sentence = "tabs over spaces"
    right_guesses = ["Right letters:"]
    wrong_guesses = ["Wrong letters:"]
    turns = 10
    guesses = 0
    while turns > 0:
        guess = input("What's your guess? ")

        if guess.lower() == "help":
            print("There are three words in the sentence. It's also two a\'s and two e\'s")
            turns += 1

        if guess.lower() not in sentence:
            turns -= 1
            guesses += 1
            print("Wrong guess, try again", "you have", turns, "chances left")
            wrong_guesses.append(guess)
            print(right_guesses)
            print(wrong_guesses)

        if guess.lower() in sentence:
            guesses += 1
            print(guess, "is in sentence")
            right_guesses.append(guess)
            print(right_guesses)
            print(wrong_guesses)

        if guess.lower() == sentence:
            print("You won! You finished the challenge in:", guesses, "guesses.")
            print("That was all the words. Good Job!")
            break

        if turns == 0:
            print("You lose")
            again = (input("Would you like to try again? (y/n)"))

            if again.lower() == "y":
                main()

            else:
                print("Better luck next time")
                quit()


if __name__ == '__main__':
    main()
