from abc import ABC, abstractmethod
from datetime import date

tahun_sekarang = date.today().year

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
    
    @abstractmethod
    def TransferSaldo(self, other):
        pass
    
    @abstractmethod
    def SukuBunga(self):
        pass

class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def TransferSaldo(self, other):
        if (tahun_sekarang - self.tahun_daftar) >= 3:
            if other > 100000:
                print(f"Transfer sejumlah Rp.{other} bebas biaya admin")
                self.saldo -= other
        else:
            if other > 100000:
                print(f"Transfer sejumlah Rp.{other} dikenakan admin sebesar Rp.2000")
                self.saldo -= (other + 2000)
            else:
                print(f"Transfer sejumlah Rp.{other} bebasa biaya admin")
                self.saldo -= other

    def SukuBunga(self):
        if(tahun_sekarang - self.tahun_daftar) >= 3 and self.saldo >= 1000000000:
            print(f"Bunga bulanan sebesar Rp.{self.saldo / 100}")
        else:
            if self.saldo >= 1000000000:
                print(f"Bunga bulanan sebesar Rp.{self.saldo / 200}")
            else:
                print(f"Bunga bulanan sebesar Rp.{self.saldo / 300}")
    
class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def TransferSaldo(self, other):
        if (tahun_sekarang - self.tahun_daftar) >= 3:
            if other > 100000:
                print(f"Transfer sejumlah Rp.{other} dikenakan biaya admin sebesar Rp.2000")
                self.saldo -= (other + 2000)
        else:
            if other > 100000:
                print(f"Transfer sejumlah Rp.{other} dikenakan biaa admin sebesar Rp.5000")
                self.saldo -= (other + 5000)
            else:
                print(f"Transfer sejumlah Rp.{other} bebas biaya admin")
                self.saldo -= other
    
    def SukuBunga(self):
        if(tahun_sekarang - self.tahun_daftar) >= 3 and self.saldo >= 10000000:
            print(f"Bunga bulanan sebesar Rp.{self.saldo / 100}")
        else:
            if self.saldo >= 10000000:
                print(f"Bunga bulanan sebesar Rp.{self.saldo / 200}")
            else:
                print(f"Bunga bulanan sebesar Rp.{self.saldo / 300}")

Yusril=AkunGold("Yusril Marrizqi", 2015, 1000000000)
Yusril.lihat_saldo()
Yusril.lihat_suku_bunga()
Yusril.transfer_saldo(10000000)
Yusril.lihat_saldo()
Yusril.lihat_suku_bunga()

Gabriel=AkunSilver("Gabriel Fico", 2015, 100000000)
Gabriel.lihat_saldo()
Gabriel.lihat_suku_bunga()
Gabriel.transfer_saldo(10000000)
Gabriel.lihat_saldo()
Gabriel.lihat_suku_bunga()
