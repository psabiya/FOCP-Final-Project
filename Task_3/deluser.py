# deluser.py
from password_utils import read_user_passwords, write_user_passwords

def delete_user():
    usernames = [user[0] for user in read_user_passwords()]
    
    username_to_delete = input("Enter username: ").lower()
    
    passwords = read_user_passwords()
    updated_passwords = [user for user in passwords if user[0] != username_to_delete]

    if len(passwords) == len(updated_passwords):
        print("User not found.")
        return

    write_user_passwords(updated_passwords)
    print("User Deleted.")

if __name__ == "__main__":
    delete_user()
