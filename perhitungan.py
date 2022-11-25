# Nama  : Haikal
# NIM   : D0221376
# Kelas : Informatika H


from abc import ABC, abstractmethod


from math import pi

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

class Lingkaran(BangunDatar):
    def __init__(self, jari = 0):
        self.jari = jari

    def luas(self):
        return pi * (self.jari**2)

class Persegi(BangunDatar):
    def __init__(self, sisi = 0):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Segitiga(BangunDatar):
    def __init__(self, alas = 0, tinggi = 0):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    
lingkaran = Lingkaran()
segitiga = Segitiga()
persegi = Persegi()
luas = 0

while True:
    print()
    print("""1. Hitung Luas Segitiga
2. Hitung Luas Persegi
3. Hitung Luas Lingkaran
4. Berhenti""")
    pilihan = int(input("=> "))

    if pilihan == 1:
        segitiga.alas = float(input("Masukkan Alas: "))
        segitiga.tinggi = float(input("Masukkan Tinggi: "))
        luas = segitiga.luas()
    elif pilihan == 2:
        persegi.sisi = float(input("Masukkan Sisi: "))
        luas = persegi.luas()
    elif pilihan == 3:
        lingkaran.jari = float(input("Masukkan Jari-jari: "))
        luas = lingkaran.luas()
    elif pilihan == 4:
        break
    else:
        print("Periksa Kembali Inputan!")
    
    print("Luas: ", luas)

print("Selamat Tinggal")
