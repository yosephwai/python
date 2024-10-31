# Program menentukan bilangan prima

# Input bilangan
bilangan = int(input("Masukkan Bilangan: "))

# Bilangan prima harus lebih besar dari 1
if bilangan > 1:
    for i in range(2, bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "bukan bilangan prima")
            print(i, "kali", bilangan // i, "=", bilangan)
            break
    else:
        print(bilangan, "adalah bilangan prima")
else:
    print(bilangan, "bukan bilangan prima")

# Penjelsan

# nput Bilangan: Program meminta pengguna untuk memasukkan sebuah bilangan.
# Pengecekan Bilangan:
# Program memeriksa apakah bilangan lebih besar dari 1. Jika tidak, maka bilangan tersebut bukan bilangan prima.
# Looping untuk Mencari Pembagi:
# Menggunakan for loop dari 2 hingga bilangan - 1.
# Jika bilangan habis dibagi dengan i (artinya bilangan % i sama dengan 0), maka bilangan tersebut bukan bilangan prima. Program mencetak informasi tentang pembagi dan keluar dari loop.
# Pesan Bilangan Prima:
# Jika tidak ditemukan pembagi (loop tidak terputus), program mencetak bahwa bilangan tersebut adalah bilangan prima.