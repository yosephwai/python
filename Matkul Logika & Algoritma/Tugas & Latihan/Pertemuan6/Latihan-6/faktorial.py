# Fungsi Faktorial secara Rekursif
def faktorial(n):
    if n == 0:
        return 1  # Dasar rekursi: 0! = 1
    else:
        return n * faktorial(n - 1)  # Rekurens: N! = N * (N-1)!

# Input dari pengguna
n = int(input("Masukkan nilai N: "))

# Menampilkan hasil
print("FAKT(%d) = %d" %  (n, faktorial(n)))

