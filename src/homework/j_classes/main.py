from class_a import Die

def main():
    die = Die()

    while True:
        print("1. Roll the die")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            die.roll()
            die.__str__()
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()
