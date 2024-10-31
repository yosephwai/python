# Program Menggambar Segitiga Siku-siku

# Berikut adalah program Python yang menggambar segitiga siku-siku berdasarkan input bilangan bulat yang 
# dimasukkan oleh pengguna. Program ini akan memastikan bahwa input berada dalam rentang 1 hingga 100

# Program untuk menggambar segitiga siku-siku

# Meminta input dari pengguna
N = int(input("Masukkan bilangan bulat (1 ≤ N ≤ 100): "))

# Memastikan input berada dalam rentang yang valid
if 1 <= N <= 100:
    # Menggambar segitiga siku-siku
    for i in range(1, N + 1):  # Loop dari 1 hingga N
        print('*' * i)  # Mencetak i bintang
    print("Masukan tidak valid. Harap masukkan bilangan bulat antara 1 dan 100.")


# Penjelsan 

# Input: Program meminta pengguna untuk memasukkan sebuah bilangan bulat N.
# Validasi Input: Memastikan bahwa nilai N berada dalam rentang 1 hingga 100.
# Menggambar Segitiga:
    # Menggunakan loop for yang iterasi dari 1 hingga N.
    # Dalam setiap iterasi, mencetak i bintang (*), sehingga jumlah bintang meningkat setiap baris.
# Output: Program mencetak segitiga siku-siku sesuai dengan nilai yang dimasukkan.