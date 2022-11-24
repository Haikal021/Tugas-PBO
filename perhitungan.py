# Nama  : Haikal
# NIM   : D0221376
# Kelas : Informatika H

from bangundatar import *

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()

luas = 0
while True:
    print()
    print("""1. Hitung Luas persegi
2. Hitung Luas Lingkaran
3. Hitung Luas Segitiga
4. Berhenti""")
    pilihan = int(input("=> "))

    if pilihan == 1:
        persegi.sisi = float(input("Masukkan Sisi: "))
        luas = persegi.luas()
        
    elif pilihan == 2:
        lingkaran.jari = float(input("Masukkan Jari-jari: "))
        luas = lingkaran.luas()
        
    elif pilihan == 3:
        segitiga.alas = float(input("Masukkan Alas: "))
        segitiga.tinggi = float(input("Masukkan Tinggi: "))
        luas = segitiga.luas()
    elif pilihan == 4:
        break
    else:
        print("Periksa Kembali !")
    
    print("Luas: ", luas)

print("Selamat Tinggal")