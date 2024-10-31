# Fungsi Fibonacci secara Rekursif
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input dari pengguna
x = int(input("Masukkan Batas Deret Bilangan Fibonacci: "))

# Menampilkan deret Fibonacci
print("Deret Fibonacci:")
for i in range(x):
    print(fibonacci(i), end=' ')

