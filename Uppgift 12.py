def is_it_too_long(name, max_length):
    return len(name) > max_length


def main():
    #students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    try:
        max_length = int(input("Hur långt får namnet vara max? "))
    except ValueError:
        max_length = 5

    students = input("Skriv studenternas namn med komma imellan: ").split(",")

    for name in students:
        name = name.strip()
        if is_it_too_long(name, max_length):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()
