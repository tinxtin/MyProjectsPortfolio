def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw, s_numb = data.split("|")
            print("Username:", user, "| Password:", passw, "| Secret-number:", s_numb)

def add():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    while True:
        try:
            s_code = input("Enter secret code (4 digits): ")
            if len(s_code) != 4:
                print("Please enter 4 digits only!")
                continue
        except ValueError:
            print("Enter numbers only!")
            continue
        else:
            break

    with open("password.txt", 'a') as f:
        f.write(username + "|" + password + "|" + str(s_code) + "\n")

while True:
    mode = input("Would you like add or view existing password? Choose either (Add, view) or Q for quit: ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue

print("Goodbye!")