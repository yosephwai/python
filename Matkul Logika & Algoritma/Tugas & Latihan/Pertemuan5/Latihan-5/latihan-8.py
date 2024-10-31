# Nested Loop (Loop Bersarang)

# Misalnya, kita ingin mencetak tabel perkalian dari 1 hingga 5 menggunakan nested while loop:

# Program untuk mencetak tabel perkalian

# Inisialisasi
i = 1

while i <= 5:  # Outer loop untuk angka 1 sampai 5
    j = 1
    while j <= 10:  # Inner loop untuk angka 1 sampai 10
        print(f"{i} x {j} = {i * j}")
        j += 1  # Increment j
    print()  # Mencetak baris kosong setelah satu tabel
    i += 1  # Increment i
