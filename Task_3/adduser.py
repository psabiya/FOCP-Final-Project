# adduser.py
from password_utils import read_user_passwords, write_user_passwords, encrypt_user_password
encrypt_user_password
def add_new_user():
    existing_usernames = {user[0].lower() for user in read_user_passwords()}
    
    new_username = input("Enter new username: ").lower()
    
    if new_username in existing_usernames:
        print("Error: Cannot add. Username already exists.")
        return

    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    encrypted_password = encrypt_user_password(password)
    
    passwords = read_user_passwords()
    new_user = (new_username, real_name, encrypted_password)
    passwords.append(new_user)
    
    write_user_passwords(passwords)
    print(f"User '{new_username}' Created.")

if __name__ == "__main__":
    add_new_user()

