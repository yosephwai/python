# Perinta Continue
# fungsi continue akan melakukan pengulangan dari awal lagi

# Program untuk meminta pengguna memasukkan bilangan di bawah 50

bil = 0
pilihan = 'y'

while pilihan != 'n':
    bil = int(input("Masukkan bilangan di bawah 50: "))
    
    if bil > 50:
        print("Bilangan melebihi angka 50, silakan diulangi.")
        continue  # Kembali ke awal loop untuk meminta input lagi
    
    print("Pangkat dua dari bilangan ini adalah:", bil * bil)
    pilihan = input("Apakah Anda ingin mengulang kembali (y/n)? ")

    # penjelsan 

# Inisialisasi:
    # bil diatur ke 0 dan pilihan diatur ke 'y' untuk memulai loop.

# Looping dengan while:
    # while pilihan != 'n': Loop ini akan terus berjalan sampai pengguna memasukkan 'n'.

# Input Bilangan:
    # Program meminta pengguna untuk memasukkan bilangan di bawah 50.

# Kondisi if:
    # Jika bilangan yang dimasukkan lebih dari 50, program akan mencetak pesan dan menggunakan continue untuk kembali 
    # ke awal loop tanpa mengeksekusi sisa kode dalam loop.

# Menghitung dan Mencetak:
    # Jika bilangan valid (di bawah 50), program akan mencetak pangkat dua dari bilangan tersebut.

# Menanyakan Ulang:
    # Program menanyakan kepada pengguna apakah ingin mengulang input (y/n)
