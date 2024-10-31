# Program untuk menjumlahkan bilangan dari 1 sampai 10

jum = 0  # Inisialisasi variabel untuk menyimpan jumlah

for i in range(10):  # Loop dari 0 hingga 9
    i += 1  # Tambah 1 agar i mulai dari 1 sampai 10
    print(i, end=' ')  # Mencetak nilai i di satu baris
    jum += i  # Menjumlahkan i ke dalam jum

print()  # Mencetak baris baru setelah loop
print("Jumlah Bilangan 1 - 10 adalah:", jum)  # Mencetak jumlah


# Penjelasn :

# Inisialisasi: jum = 0 digunakan untuk menyimpan total jumlah bilangan.
# Looping: for i in range(10) akan mengulangi proses sebanyak 10 kali (0 hingga 9).
    # i += 1 digunakan untuk mengubah nilai i sehingga mulai dari 1 hingga 10.
# Mencetak: print(i, end=' ') mencetak setiap nilai i pada satu baris dengan spasi di antara angka.
# Menjumlahkan: jum += i menambahkan nilai i ke total jum.
# Output: Setelah loop selesai, mencetak jumlah total bilangan.
