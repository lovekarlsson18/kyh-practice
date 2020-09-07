import random


def main():

    mobiltelefonen = ["en dator", "en bil", "en tvättmaskin", "ett par google glasses"]
    coronaviruset = ["zombieviruset", "magsjuka", "löss", "scenskräck"]
    sverige = ["Narnia", "Midgård", "Norge", "Finland"]
    markku_tervahauta = ["Peter Forsberg", "Kattla", "Darth Vader", "Markoolio"]
    en_app = ["Ett dokument", "Ett hologram", "En stenmålning", "Ett datorspel"]

    print(f"""{en_app[random.randint(0,3)]} som kan laddas ned till {mobiltelefonen[random.randint(0, 3)]} ska varna finländare som kommit nära någon som smittats med {coronaviruset[random.randint(0, 3)]}.
– Jag tycker att ni i {sverige[random.randint(0, 3)]} borde överväga att göra något liknande, säger {markku_tervahauta[random.randint(0, 3)]}, generaldirektör för
Finska institutet för hälsa och välfärd, THL.""")


if __name__ == '__main__':
    main()
