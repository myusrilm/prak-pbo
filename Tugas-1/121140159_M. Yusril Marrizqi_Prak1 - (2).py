username = "informatika"
password = "12345678"

for i in range(3):
    uname = input("Username anda : ")
    passw = input("Password anda : ")

    if uname == username and passw == password:
        print("Login berhasil!")
        exit()
    elif uname != username or passw != password:
        print("Username atau password salah, coba lagi!")
    elif i == 2 and (uname != username or passw != password):
        print("Akun diblokir!") 
    print()
