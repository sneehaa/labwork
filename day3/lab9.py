print("Please enter your username and password")
count=0
while count < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username=="admin" and password=="123":
        print('Logged in Successfully!')
        break
    else:
        print("Invalid credentials. Try again.")
        count += 1
else:
    print("Attempt finished!")