def clean_up():
    pass


def build_id():
    pass


def validate_password(password):
    pass


def create_unique(id_list):
    pass


def create_short_address():
    pass


def validate_pcode(split_addrs):
    pass


def ids_addrs(short_addr):
    pass


def main():
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up()
        elif choice == '2':
            id_list = build_id()
        elif choice == '3':
            validate_password("1abcDE%")
        elif choice == '4':
            create_unique(id_list)
        elif choice == '5':
            short_addr = create_short_address()
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()
