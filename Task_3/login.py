# login.py
from password_utils import read_user_passwords, encrypt_user_password

def login():
    usernames = [user[0] for user in read_user_passwords()]
    
    username = input("User: ").lower()
    
    if username not in usernames:
        print("Access denied.")
        return

    password = input("Password: ")
    encrypted_password = encrypt_user_password(password)
    user_found=False
    for user in read_user_passwords():
        if user[0] == username and user[2] == encrypted_password:
            user_found=True
    if user_found:
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    login()



