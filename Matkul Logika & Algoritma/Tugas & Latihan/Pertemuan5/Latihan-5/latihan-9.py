# Program Menggunakan Nested While

# lengkap tentang program untuk mencetak bilangan prima antara 1 hingga 50 menggunakan nested while loop.

# Program untuk mencetak bilangan prima antara 1 sampai 50

i = 2  # Inisialisasi bilangan yang akan diperiksa
while i <= 50:  # Loop untuk setiap bilangan dari 2 hingga 50
    j = 2  # Inisialisasi untuk pengecekan faktor
    while j <= (i ** 0.5):  # Hanya perlu memeriksa hingga akar kuadrat dari i
        if (i % j) == 0:  # Jika i habis dibagi j
            break  # Keluar dari inner loop jika ditemukan faktor
        j += 1  # Increment j
    if j > (i ** 0.5):  # Jika tidak ada faktor ditemukan
        print(i, "adalah Bilangan Prima")  # Mencetak bilangan prima
    i += 1  # Increment i

print("Terima Kasih")

# Inisialisasi:
    # i diatur ke 2, karena 1 bukan bilangan prima.

# Outer Loop (while i <= 50):
    #Loop ini akan iterasi dari 2 hingga 50.

# Inner Loop (while j <= (i ** 0.5)):
    # Loop ini digunakan untuk memeriksa apakah i memiliki faktor selain 1 dan i sendiri.
    # Memeriksa hingga akar kuadrat dari i cukup untuk menentukan apakah i adalah bilangan prima.

# Pemeriksaan Faktor:
    # Jika i habis dibagi j (if (i % j) == 0), maka i bukan bilangan prima, dan program keluar dari inner loop dengan break.
    # Jika tidak ada faktor yang ditemukan setelah memeriksa semua j, maka i dianggap bilangan prima.

# Increment:
    # Setelah memeriksa semua bilangan hingga 50, i ditambahkan 1 untuk melanjutkan ke bilangan berikutnya.

# Output:
    # Program mencetak bilangan prima yang ditemukan dan mengucapkan terima kasih setelah selesai.