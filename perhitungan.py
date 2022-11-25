# Nama  : Haikal
# NIM   : D0221376
# Kelas : Informatika H


def luas_lingkaran(r):
    return 3.14*(r * r)

def luas_segitiga(alas, tinggi):
    return 1/2 * alas * tinggi

def luas_persegi(sisi):
    return sisi * sisi

print('''1. Lingkaran
2. Segitiga
3. Persegi''')

a = int(input("Masukkan luas bangun datar yang akan dicari : "))
if a == 1:
    r = float(input("Masukkan jari - jari : "))
    hasil = luas_lingkaran(r)
    print("Luas lingkaran adalah = " , hasil ," cm"  )

elif a == 2:
    alas = float(input("Masukkan alas segitiga : "))
    tinggi = float(input("Masukkan tinggi segitiga : "))
    hasil = luas_segitiga(alas, tinggi)
    print("Luas segitiga adalah = " , hasil ," cm" )

elif a == 3:
    sisi = float(input("Masukkan sisi persegi: "))
    hasil = luas_persegi(sisi)
    print("Luas persegi adalah : " , hasil ," cm" )

else :
    print( a , "Tidak ada")
