from jupyterlab.semver import valid

def clean_up():
    with open("text_to_clean.txt") as my_file:
        contents = my_file.readlines()
        cleaned = []
        valid_characters = [" ","."]
        for i, line in enumerate(contents):
            string = ""
            for char in line:
                if char in valid_characters or char.isalpha():
                    string += char
            cleaned.append(string)
    with open("student_names.txt", "w") as student_db:
        for student in cleaned:
            student_db.write(student+"\n")
    return cleaned

def build_id():
    id_list = []
    with open("student_names.txt") as student_db:
        for line in student_db:
            line = line.strip()
            name_parts = line.lower().split(" ")
            sid = ""
            if len(name_parts) == 3:
                for part in name_parts:
                    sid += part[0]
            else:
                sid += name_parts[0][0] + "x" + name_parts[1][0]
            id_list.append(sid)
    return id_list

def validate_password(password):
    illegal_password = []
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    elif len(password) > 12:
        illegal_password.append("TOO LONG")

    for char in password:
        if not char.isalpha() and not char.isdigit() and char != "_":
            illegal_password.append("WRONG CHARACTERS")
            break

    has_lower = False
    has_upper = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True

    if not has_lower or not has_upper:
        illegal_password.append("NOT MIXED CASE")

    if password[0].isdigit():
        illegal_password.append("LEADING DIGIT")

    most_common_passes = []
    with open("password.txt") as passwords:
        for line in passwords:
            line = line.strip()
            most_common_passes.append(line)
    if password in most_common_passes:
        illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")
    return illegal_password

def create_unique(id_list):
    unique_id = []
    for stu_id in id_list:
        sid_count = id_list.count(stu_id)
        if sid_count > 1:
            for n in range(sid_count):
                code = f"000{n}"
                stud_id = stu_id + code
                if stud_id not in unique_id:
                    unique_id.append(stud_id)
        else:
            unique_id.append(stu_id + "0000")
    with open("unique_ids.txt", "w") as db, open("create_emails.txt", "w") as emails:
        for sid in unique_id:
            db.write(sid+"\n")
            emails.write(sid+"@student.bham.ac.uk"+"\n")
    return unique_id

def create_short_address():
    split_addrs = []
    with open("addresses.txt", "r") as addresses:
        for line in addresses:
            line = line.strip().split(",")
            split_addrs.append(line[0] + "," + line[3])
    return split_addrs

def validate_pcode(split_addrs):
    post_codes = []
    for i, address in enumerate(split_addrs):
        single_add = [i, True, True, True, True]
        pcode = address.split(",")[1][1:]
        print(pcode)
        if len(pcode) != 6:
            pcode = "00000"
            single_add[1] = False
        if not pcode[0].isupper():
            single_add[2] = False
        if not pcode[1:4].isdigit():
            single_add[3] = False
        if not pcode[-2::].isupper():
            single_add[4] = False
        post_codes.append(single_add)
    return post_codes


def ids_addrs(short_addr):
    id_add = {}
    with open("unique_ids.txt") as db:
        for i, line in enumerate(db):
            line = line.strip()
            id_add[line] = short_addr[i]
    return id_add


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


