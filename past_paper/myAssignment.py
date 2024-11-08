import string
'''
My solution for the practice paper question.
The starting template can be found in assignment_start.py
If you find any mistakes in this file/anything that can be improved please update it!
'''

def clean_up():
    cleaned = ""
    with open("text_to_clean.txt", "r") as f:
        original_text = f.read()
    acceptable_characters = "." + string.whitespace + string.ascii_letters
    # OR just = " " + "\n" + "." + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" if we aren't allowed to import string for whatever reason
    for letter in original_text:
        if letter in acceptable_characters:
            cleaned += letter
    with open("student_names.txt", "w") as f:
        f.write(cleaned)
        f.close()
    return cleaned


def build_id():
    id_list = []
    with open("student_names.txt", "r") as f:
        name_list = f.readlines()
    for name in name_list:
        id = ""
        name = name.strip().split()
        if len(name) == 3:
            for part in name:
                id += part[0].lower()
        else:
            id = name[0][0].lower() + "x" + name[1][0].lower()
        id_list.append(id)
    return id_list


def validate_password(password):
    illegal_password_list = []
    # Check Length
    if len(password) < 8:
        illegal_password_list.append("TOO SHORT")
    elif len(password) > 12:
        illegal_password_list.append("TOO LONG")
    # Check character type
    legal_characters = string.digits + string.ascii_letters + "_"
    for letter in password:
        if letter not in legal_characters:
            illegal_password_list.append("WRONG CHARACTERS")
        break
    # Check leading digit
    if password[0] in string.digits:
        illegal_password_list.append("LEADING DIGIT")
    # Check mixed case
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    uc_count = 0
    lc_count = 0
    for letter in password:
        if letter in lc:
            lc_count += 1
        if letter in uc:
            uc_count += 1
    if uc_count == 0 or lc_count == 0:
        illegal_password_list.append("NOT MIXED CASE")
    # Check if common password
    with open("password.txt", "r") as f:
        common_passwords = f.readlines()
        for common_password in common_passwords:
            if common_password.strip() == password:
                illegal_password_list.append("CANNOT MAKE USE OF THIS PASSWORD")
            break
    print([reason for reason in illegal_password_list])


def create_unique(id_list):
    unique_list = []
    for id in id_list:
        counter = "0000"
        same_id = [id for entry in unique_list if entry.startswith(id)]
        if len(same_id) > 0:
            incr = len(same_id)
            new_counter = f"000{incr}"
            id = id + new_counter
        else:
            id = id + counter
        unique_list.append(id)
    with open("unique_ids.txt", "w") as f:
        for id in unique_list:
            f.write(id + "\n")
    with open("create_emails.txt", "w") as ef:
        for id in unique_list:
            ef.write(id + "@student.bham.ac.uk" + "\n")
def create_short_address():
    split_addrs = []
    with open("addresses.txt", "r") as f:
        addresses = f.readlines()
    for address in addresses:
        info = address.split(',')
        address1 = info[0]
        postcode = info[3].strip()
        split_addrs.append([address1, postcode])
    return split_addrs

def validate_pcode(split_addrs):
    validate_pcode = []
    postcodes = [entry[1] for entry in split_addrs]
    print(postcodes)
    for i, postcode in enumerate(postcodes):
        li = [i]
        # Verify Length
        if len(postcode) != 6:
            invalid = '$$$$$$'
            postcodes[i] = invalid
            li.append(False)
        else:
            li.append(True)
        # Verify first character
        uc = string.ascii_uppercase
        if postcode[0] not in uc:
            li.append(False)
        else:
            li.append(True)
        # Verify 2,3,4
        nums = '0123456789'
        for n in postcode[1:4]:
            if n not in nums:
                li.append(False)
                break
            else:
                li.append(True)
                break
        # Verify final 2 characters
        if postcode[-2:] not in uc:
            li.append(False)
        else:
            li.append(True)
        validate_pcode.append(li)
    return validate_pcode


def ids_addrs(short_addr):
    combo = {}
    with open("unique_ids.txt", "r") as f:
        unique_ids = f.readlines()
    for i, id in enumerate(unique_ids):
        combo[id.strip()] = short_addr[i]
    return combo


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
