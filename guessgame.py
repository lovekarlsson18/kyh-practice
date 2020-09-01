import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1-100. Gissa vilket?")
gissning = 0

def mainloop(gissning):
    while True:
        text = input("Din gissning: ")
        as_number = int(text)

        if as_number == n:
            gissning += 1
            print("Rätt!")
            print("Du hade totalt: " + str(gissning) + " " "gissningar")
            break

        if as_number < n:
            print("Fel! Mitt nummer är högre... Testa igen!")
            gissning += 1
            print("Antal gissningar: " + str(gissning))

        if as_number > n:
            print("Fel! Mitt nummer är lägre... Testa igen!")
            gissning += 1
            print("Antal gissningar: " + str(gissning))

mainloop(gissning)
