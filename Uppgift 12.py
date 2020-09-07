def is_it_too_long(name):
    return len(name) > 5


def main():
    #students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    students = input("Skriv studenternas namn med komma imellan: ").split(",")
    for name in students:
        if is_it_too_long(name):
            print(f"{name} är för långt!")


if __name__ == '__main__':
    main()