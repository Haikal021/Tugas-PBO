print("SELAMAT DATANG DI BRI")
p=int(input("MASUKKAN PIN ANDA: "))
m = 25000
if(p == 1234):
    print("1 Tarik Tunai")
    print("2 Cek Saldo")
    print("3 Tranfer")
    c = int(input("Silahkan pilih Transaksi: "))
    if (c == 1):
        w=int(input("Masukkan Jumlah Penarikan: "))
        if (w < m and w%100 == 0):
            print("Silahkan Ambil Jumlah Anda:", w)
        else:
            print("Uang tidak cukup")

    elif(c==2): 
        print("Saldo Anda : ",m)

    elif (c == 3):
        a = int(input("Masukkan No Rek Tujuan: "))
        z = int(input("Masukkan Jumlah Transfer: "))

        if z > m:
            print("Saldo tidak cukup")
        else:
            print(f"{z} ditransfer ke {a}")

    else:
        print("Pilihan Salah")
else:
    print("Pin Anda Salah")