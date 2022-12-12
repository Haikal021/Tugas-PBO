class Kubus():
    def __init__(self, sisi):
        self.sisi = sisi

    def volume (self):
        v_k = self.sisi**3
        print("volume kubus adalah : " , v_k)

    def luas (self):
        l_k = 6 * self.sisi**2
        print("luas kubus adalah : " , l_k)

class Balok():
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume (self):
        v_b = self.panjang * self.lebar * self.tinggi
        print("vplume balok adalah : " , v_b)

    def luas (self):
        l_b = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang)
        print("luas balok adalah : ", l_b)

class Bola():
    def __init__(self, jari):
        self.jari = jari

    def volume (self):
        v_b = 4/3 * 22/7 * self.jari**3
        print("volume bola adalah : " , round(v_b,2))

    def luas (self):
        l_b = 4 * 22/7 * self.jari**2
        print("luas bola adalah : ", round(l_b,2))

while True:
    print()
    print("""Bangun Ruang yang akan di hitung
1. Balok
2. Kubus
3. Bola
4. Berhenti""")
    pilihan = input("=> ")

    if pilihan == '1':
        p = float(input("masukkan panjang: "))
        l = float(input("masukkan lebar: "))
        t = float(input("masukkan tinggi: "))
        balok = Balok(p,l,t)
        print()
        balok.volume()
        balok.luas()
    elif pilihan == '2':
        s = float(input("Masukkan Sisi: "))
        kubus = Kubus (s)
        print()
        kubus.volume()
        kubus.luas()
    elif pilihan == '3':
        j = float(input("masukkan jari: "))
        bola = Bola (j)
        print()
        bola.volume()
        bola.luas()
    elif pilihan == '4':
        break
    else :
        print("input salah")
