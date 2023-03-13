class Mobil:
    roda = 4                              # globat atribut

    def __init__(self, warna, model):
        self.warna = warna                  # atribut public
        self.model = model              
        self._mileage = 0                   # atribut protected
        self.__engine_status = False        # atribut private

    def start_engine(self):                 # fungsi menyalakan mobil
        self.__engine_status = True      
        print("Mesin Hidup")

    def stop_engine(self):                  # fungsi mematikan mobil
        self.__engine_status = False
        print("Mesin Mati")

    def _update_mileage(self, jarak):    # fungsi menambah odometer
        self._mileage += jarak

    def drive(self, jarak):              # fungsi untuk menjalankan mobil
        if self.__engine_status:
            self._update_mileage(jarak)
            print(f"{self.warna} {self.model} Mengendarai dengan {jarak} km")
        else:
            print("Tolong Hidupkan Mesinnya Terlebih Dahulu")

    def get_mileage(self):                  # fungsi untuk menampilkan odometer   
        return self._mileage

    def _reset_mileage(self):               # fungsi untuk mereset odometer
        self._mileage = 0


Mobil1 = Mobil("Putih", "BMW")
print(f"warna: {Mobil1.warna}") 
print(f"Model: {Mobil1.model}")
print(f"roda: {Mobil1.roda}")

Mobil1.start_engine()
Mobil1.drive(50)
Mobil1.warna = "Biru"
print(f"Warna Baru: {Mobil1.warna}")
print(f"Mileage: {Mobil1.get_mileage()} km")
Mobil1._reset_mileage()
