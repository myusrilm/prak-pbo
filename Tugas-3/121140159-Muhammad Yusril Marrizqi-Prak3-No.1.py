class Akun:
    listpel = 0

    def __init__(self, nomor, nama, saldo):
        self.__nomor = nomor
        self.__nama = nama
        self.__saldo = saldo
        Akun.listpel += 1

    def lihat_saldo():
        print(f"{Akun1.__nama} memiliki saldo Rp {Akun1.__saldo}")

    def tarik_tunai():
        while True:
            tarik = int(input("Masukan jumlah nominal yang ingin ditarik : "))

            if tarik > Akun1.__saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                Akun1.__saldo -= tarik
                print("Saldo berhasil ditarik!")
                break
    
    def transfer():
        transfer = int(input("Masukan nominal yang ingin ditransfer : "))
        tujuan = int(input("Masukan no rekening tujuan : "))
        
        if tujuan == Akun2.__nomor:
            Akun2.__saldo += transfer
            Akun1.__saldo -= transfer
            print(f"Transfer Rp.{transfer} ke {Akun2.__nama} sukses!")
        elif tujuan == Akun3.__nomor:
            Akun3.__saldo += transfer
            Akun1.__saldo -= transfer
            print(f"Transfer Rp.{transfer} ke {Akun3.__nama} sukses!")
        else:
            print("No rekening tujuan tidak dikenal!")

    def lihat_menu():
        print("Selamat datang di Bank Jago")
        print(f"Halo {Akun1.__nama}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        n = int(input("Masukan nomor input : "))

        print()
        if n == 1:
            Akun.lihat_saldo()
        elif n == 2:
            Akun.tarik_tunai()
        elif n == 3:
           Akun.transfer()
        elif n == 4:
            exit(0)
 
        print()
        print()
        Akun.lihat_menu()

Akun1 = Akun(1234, "Muhammad Yusril Marrizqi", 5000000000)
Akun2 = Akun(2345, "Ukraina", 6666666666)
Akun3 = Akun(3456, "Elon Musk", 9999999999)

Akun.lihat_menu()
