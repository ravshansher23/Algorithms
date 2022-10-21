import hashlib
import json


def password():

    try:
        with open('data.json') as f:
            data = json.load(f)
        user = input('Enter your Login')
        salt = user
        if data[user]:
            user_password = input('Enter your password')
            hash_pass = hashlib.sha256(user_password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            if hash_pass == data[user]:
                print(f"OK")
            else:
                print(f"Не верно введен пароль")
    except Exception:
        data = {}
        user = input('Enter your Login')
        salt = user
        user_password = input('Enter your password')
        hash_pass = hashlib.sha256(user_password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        user_password2 = input('Enter your password again')
        hash_pass2 = hashlib.sha256(user_password2.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        if hash_pass == hash_pass2:
            print(f"Пароль введен верно")
            data[user] = hash_pass
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
        else:
            print(f"Не верно введен пароль")


password()