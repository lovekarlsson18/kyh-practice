from pathlib import Path

p = Path("TODO.txt")


homepage = """
1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet"""

print(homepage)

todo_list = []
todo_list.append(p.read_text())


def user_input():
    user_answer = input("Vad vill du göra? ")
    while True:
        if user_answer == "1":
            print(p.read_text())

        if user_answer == "2":
            p.read_text()
            user_input2 = input("Vad vill du lägga till? ")
            todo_list.append(user_input2)
            p.write_text(f"{todo_list}")

        if user_answer == "3":
            print(p.read_text())
            user_input3 = input("Vad vill du ta bort? ")
            todo_list.remove(user_input3)
            p.write_text(f"{todo_list}")

        if user_answer == "4":
            quit()


        user_input()

user_input()