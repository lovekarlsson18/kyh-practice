import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1-100. Gissa vilket?")
gissning = 0


def ask_number():
    text = input("Din gissning: ")
    as_number = int(text)
    return as_number


def mainloop(gissning):
    while True:
        as_number = ask_number()

        if as_number == n:
            gissning += 1
            print("Rätt!")
            # print("Du hade totalt: " + str(gissning) + " " "gissningar")
            return gissning

        if as_number < n:
            print("Fel! Mitt nummer är högre... Testa igen!")
            gissning += 1
            print("Antal gissningar: " + str(gissning))

        if as_number > n:
            print("Fel! Mitt nummer är lägre... Testa igen!")
            gissning += 1
            print("Antal gissningar: " + str(gissning))


antal_gissningar = mainloop(gissning)
print("Du hade totalt: " + str(antal_gissningar) + " " "gissningar")
