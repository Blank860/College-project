def login(users_file):
    print("Login to your account:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(users_file, 'r') as file:
        for line in file:
            role, stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                print("Login accepted.")
                return role
    print("Invalid username or password.")
    return None



# Create account
def create_account(users_file):
    print("Create a new account:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = input("Enter your role (admin/user): ").lower()

    if role not in ["admin", "user"]:
        print("Invalid role. Please enter 'admin' or 'user'.")
        return
    
    with open(users_file, 'a') as file:
        file.write(f"{role},{username},{password}\n")
    print("Account created successfully.")



