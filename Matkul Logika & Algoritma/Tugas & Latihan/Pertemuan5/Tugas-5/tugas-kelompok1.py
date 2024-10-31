# Meminta input bilangan bulat dari pengguna
n = int(input("Masukkan bilangan bulat (1 ≤ N ≤ 100): "))

# Memastikan input berada dalam rentang yang valid
if 1 <= n <= 100:
    # Meminta input karakter dari pengguna
    karakter = input("Masukkan karakter: ")

    # Menggambar pola segitiga sama kaki
    for i in range(n):  # Loop untuk setiap baris
        # Mencetak spasi sebelum karakter untuk membuat segitiga
        print(' ' * (n - i - 1), end='')  # Spasi di depan
        print(karakter * (2 * i + 1))  # Mencetak karakter
else:
    print("Masukan tidak valid. Harap masukkan bilangan bulat antara 1 dan 100.")


# Penjelasan 

# Input Bilangan Bulat: Program meminta pengguna untuk memasukkan sebuah bilangan bulat N.
# Validasi Input: Memastikan bahwa N berada dalam rentang 1 hingga 100.
# Input Karakter: Program meminta pengguna untuk memasukkan sebuah karakter.
# Menggambar Pola Segitiga:
    # Loop untuk Baris: for i in range(n) mengulangi proses untuk setiap baris segitiga.
    # Mencetak Spasi: print(' ' * (n - i - 1), end='') mencetak spasi di depan karakter agar membentuk segitiga yang simetris.
    # Mencetak Karakter: print(karakter * (2 * i + 1)) mencetak karakter dengan jumlah yang sesuai untuk membentuk segitiga.
# Output: Program akan mencetak pola segitiga dengan karakter yang dimasukkan.
