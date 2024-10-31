# Mendefinisikan variabel
a = 10
b = 5

# Menggunakan operator logika AND
if a > b and b > 0:
    print("a lebih besar dari b dan b positif.")

# Menggunakan operator logika OR
if a < 0 or b < 0:
    print("Salah satu nilai adalah negatif.")
else:
    print("Kedua nilai adalah positif.")

# Menggunakan operator logika NOT
if not (a < b):
    print("a tidak kurang dari b.")

#Dalam contoh ini:

#AND: Pernyataan a > b and b > 0 akan benar hanya jika kedua kondisi terpenuhi.
#OR: Pernyataan a < 0 or b < 0 akan benar jika salah satu dari kedua kondisi terpenuhi.
#NOT: Pernyataan not (a < b) akan benar jika kondisi di dalam tanda kurung salah


# Mendefinisikan variabel
umur = 20
status_pekerjaan = "mahasiswa"

# Menggunakan operator logika AND
if umur >= 18 and status_pekerjaan == "mahasiswa":
    print("Anda adalah mahasiswa dewasa.")

# Menggunakan operator logika OR
if umur < 18 or status_pekerjaan == "pengangguran":
    print("Anda masih muda atau tidak memiliki pekerjaan tetap.")

# Menggunakan operator logika NOT
if not (status_pekerjaan == "mahasiswa"):
    print("Anda bukan mahasiswa.")
else:
    print("Anda adalah mahasiswa.")


#Dalam contoh ini:

#AND: Pernyataan umur >= 18 and status_pekerjaan == "mahasiswa" mengecek apakah umur minimal 18 tahun 
# dan status pekerjaan adalah mahasiswa. Jika keduanya benar, maka pesan akan ditampilkan.

#OR: Pernyataan umur < 18 or status_pekerjaan == "pengangguran" akan menghasilkan true jika salah satu 
# dari kondisi terpenuhi, yaitu jika umur kurang dari 18 atau status pekerjaan adalah pengangguran.

#NOT: Pernyataan not (status_pekerjaan == "mahasiswa") mengecek apakah status pekerjaan bukan mahasiswa. 
# Jika benar, maka pesan akan ditampilkan. Jika tidak, maka akan menampilkan pesan bahwa orang 
# tersebut adalah mahasiswa

