# passwd.py
from password_utils import read_user_passwords, write_user_passwords, encrypt_user_password

def change_password():
    usernames = [user[0] for user in read_user_passwords()]
    
    username = input("User: ").lower()
    
    if username not in usernames:
        print("User not found.")
        return

    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_current_password = encrypt_user_password(current_password)

    passwords = read_user_passwords()
    for i, user in enumerate(passwords):
        if user[0] == username and user[2] == encrypted_current_password:
            passwords[i] = (user[0], user[1], encrypt_user_password(new_password))
            write_user_passwords(passwords)
            print("Password changed.")
            return

    print("Invalid current password.")

if __name__ == "__main__":
    change_password()