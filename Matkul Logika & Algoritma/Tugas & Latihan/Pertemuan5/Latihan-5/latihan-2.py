# Program untuk menampilkan deret bilangan genap

# Input dari pengguna
n = int(input('Masukkan Nilai N: '))

# Inisialisasi variabel
x = 2

# Menggunakan while untuk menampilkan deret bilangan genap
while x <= n:
    print(x, end=" ")
    x += 2  # Menambah x sebanyak 2 untuk mendapatkan bilangan genap berikutnya
