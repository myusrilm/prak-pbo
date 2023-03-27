import random

class Robot:
    jumlah_turn = 0
    alive = True
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = int(health)
        self.damage = int(damage)

    def lakukan_aksi(self, other):
        if self.nama == "Antares":
            if self.jumlah_turn % 3 == 0:
                self.damage *= 1.5
                self.terima_aksi(other, self.damage)
                self.damage /= 1.5
            else:
                self.terima_aksi(other, self.damage)
        elif self.nama == "Alphasetia":
            if self.jumlah_turn % 2 == 0:
                self.health += 4000
                self.terima_aksi(other, self.damage)
                print("Alphasetia mendapatkan health tambahan sebesar 4000")
            else:
                self.terima_aksi(other, self.damage)
        elif self.nama == "Lecalicus":
            if self.jumlah_turn % 4 == 0:
                self.damage *= 2
                self.health += 7000
                self.terima_aksi(other, self.damage)
                self.damage /= 2
                print("Lecalicus mendapatkan health tambahan sebesar 7000")
            else:
                self.terima_aksi(other, self.damage)

    def terima_aksi(self, other, damage):
        if damage > other.health:
            other.health = 0
            other.alive = False
            print(f"{other.nama} menerima damage sebesar {int(damage)}")
            print(f"{other.nama} telah mati!")
        else:
            other.health -= damage
            print(f"{other.nama} menerima damage sebesar {int(damage)}")

class Antares(Robot):
    def __init__(self):
        Robot.__init__(self, "Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        Robot.__init__(self, "Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        Robot.__init__(self, "Lecalicus", 45000, 5500)

loop = True
print("Selamat datang di pertandingan robot Yamako")

n = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
while loop:
    if n == 1:
        Mine = Antares()
        break
    elif n == 2:
        Mine = Alphasetia()
        break
    elif n == 3:
        Mine = Lecalicus()
        break
    else :
        print("Pilihan tidak tersedia!")
        n = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))

o = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
while loop:
    if o == 1:
        Enemy = Antares()
        break
    elif o == 2:
        Enemy = Alphasetia()
        break
    elif o == 3:
        Enemy = Lecalicus()
        break
    else:
        print("Pilihan tidak tersedia!")
        o = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
print()

while Mine.alive and Enemy.alive:
    Robot.jumlah_turn += 1
    print(f"Turn saat ini: {Robot.jumlah_turn}")
    print(f"Robotmu ({Mine.nama} - {int(Mine.health)} HP), robot lawan ({Enemy.nama} - {int(Enemy.health)} HP)")
    My_turn = int(input(f"Pilih tangan robotmu ({Mine.nama}) : "))
    while loop:
        if My_turn > 0 and My_turn < 4:
            break
        else:
            print("Pilihan tidak tersedia!")
            My_turn = int(input(f"Pilih tangan robotmu ({Mine.nama}) : "))
    Enemy_turn = random.randint(1, 3)
    print(f"Robot lawan ({Enemy.nama}) memilih : {Enemy_turn}")

    if My_turn == 1:
        if Enemy_turn == 1:
            print("Seri!")
        elif Enemy_turn == 2:
            Enemy.lakukan_aksi(Mine)
        elif Enemy_turn ==3:
            Mine.lakukan_aksi(Enemy)
    elif My_turn == 2:
        if Enemy_turn == 1:
            Mine.lakukan_aksi(Enemy)
        elif Enemy_turn == 2:
            print("Seri!")
        elif Enemy_turn ==3:
            Enemy.lakukan_aksi(Mine)
    elif My_turn == 3:
        if Enemy_turn == 1:
            Enemy.lakukan_aksi(Mine)
        elif Enemy_turn == 2:
            Mine.lakukan_aksi(Enemy)
        elif Enemy_turn ==3:
            print("Seri!")
    print()

print("Pertandingan berakhir!")
