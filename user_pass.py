while True:
    password = input("Пожалуйста, введите надежный пароль:")
    if not any(x.isupper() for x in password):
        print("В вашем пароле должен быть как минимум 1 заглавный регистр.")
    elif not any(x.isdigit() for x in password):
        print("У вас должна быть хотя бы 1 цифра")
    elif not any(x.islower() for x in password):
        print("В вашем пароле должна быть как минимум 1 строчная буква.")
    elif len(password) < 10:
        print("Пожалуйста, увеличьте длину вашего пароля, по крайней мере, до 10 символов.")
        print("Ваш пароль - это только " + str(len(password)) + " characters long")
    else:
        break
