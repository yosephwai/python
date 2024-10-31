# Perinta Break pada Python

# Program untuk mencetak angka dari 0 hingga 6 dan keluar dengan break

bil = 6
for i in range(0, 10):
    print(i)
    if i == bil:  # Menggunakan '==' untuk membandingkan
        break  # Keluar dari loop jika i sama dengan bil

# Catatan: Looping akan terus berjalan sampai dipaksa keluar oleh instruksi break.


# Penjelasan 

# Inisialisasi Variabel:
# diatur ke 6. Ini adalah nilai yang akan memicu perintah break.

# Looping dengan for:
# Menggunakan for i in range(0, 10): Loop ini akan iterasi dari 0 hingga 9.

# Mencetak Angka:
# print(i): Setiap angka dari 0 hingga 9 akan dicetak.

# Kondisi break:
# if i == bil: Memeriksa apakah nilai i sama dengan bil.
# Jika kondisi ini terpenuhi, perintah break akan menghentikan loop.