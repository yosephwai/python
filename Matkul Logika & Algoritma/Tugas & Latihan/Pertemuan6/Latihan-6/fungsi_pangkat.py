def pangkat_10(n):
    if n == 0:
        return 1  # Dasar rekursi: 10^0 = 1
    else:
        return 10 * pangkat_10(n - 1)  # Rekurens: 10^n = 10 * 10^(n-1)

# Contoh penggunaan
n = 3
hasil = pangkat_10(n)
print(f"10^{n} = {hasil}")




# Fungsi Pangkat secara Rekursif
def pangkat(x, y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x, y - 1)

# Input dari pengguna
x = int(input("Masukkan Nilai X: "))
y = int(input("Masukkan Nilai Y: "))

# Menampilkan hasil
print("%d dipangkatkan %d = %d" % (x, y, pangkat(x, y)))
