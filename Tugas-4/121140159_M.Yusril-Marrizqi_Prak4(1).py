class Komputer:
    def __init__(self, merk, jenis, harga):
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

    def __str__(self):
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class Processor(Komputer):
    def __init__(self, merk, jenis, harga, core, speed):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "Processor"
        self.jumlah_core = core
        self.kecepatan_processor = speed

class RAM(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "RAM"
        self.capacity = capacity

class HDD(Komputer):
    def __init__(self, merk, jenis, harga, capacity, rpm):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "SATA"
        self.capacity = capacity
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "VGA"
        self.capacity = capacity

class PSU(Komputer):
    def __init__(self, merk, jenis, harga, daya):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "PSU"
        self.daya = daya
    
P1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
P2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
RAM1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
RAM2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
HDD1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
HDD2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
VGA1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
VGA2 = VGA('Asus', '1060Ti', 250000, '8GB')
PSU1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
PSU2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

Rakit = [[P1, RAM1, HDD1, VGA1, PSU1], [P2, RAM2, HDD2, VGA2, PSU2]]

x = 1
for i in Rakit:
    print(f"Komputer {x}")
    for j in i:
        print(j)
    x += 1
    print()
