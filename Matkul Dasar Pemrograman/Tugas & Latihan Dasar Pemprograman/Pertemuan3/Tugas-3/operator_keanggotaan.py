# Mendefinisikan daftar
buah = ['apel', 'jeruk', 'pisang', 'mangga']

# Menggunakan operator 'in'
if 'jeruk' in buah:
    print("Jeruk ada dalam daftar buah.")

# Menggunakan operator 'not in'
if 'anggur' not in buah:
    print("Anggur tidak ada dalam daftar buah.")

# Contoh dengan string
kalimat = "Belajar Python sangat menyenangkan!"

# Memeriksa apakah substring ada dalam string
if 'Python' in kalimat:
    print("Kata 'Python' ada dalam kalimat.")

# Memeriksa apakah substring tidak ada
if 'Java' not in kalimat:
    print("Kata 'Java' tidak ada dalam kalimat.")


#Dalam contoh ini:

#Operator in digunakan untuk memeriksa apakah elemen tertentu ada dalam sebuah daftar. 
  #Misalnya, kita memeriksa apakah "jeruk" ada dalam daftar buah.
#Operator not in digunakan untuk memeriksa apakah elemen tidak ada dalam daftar. 
  #Dalam contoh ini, kita memeriksa apakah "anggur" tidak ada dalam daftar buah.
#Kita juga menggunakan operator keanggotaan dengan string untuk memeriksa keberadaan substring.


# Mendefinisikan set
warna = {'merah', 'biru', 'hijau'}

# Menggunakan operator 'in' untuk set
if 'biru' in warna:
    print("Biru ada dalam set warna.")

# Menggunakan operator 'not in' untuk set
if 'kuning' not in warna:
    print("Kuning tidak ada dalam set warna.")

# Contoh dengan dictionary
data_mahasiswa = {
    '001': 'Alice',
    '002': 'Bob',
    '003': 'Charlie'
}

# Memeriksa apakah kunci ada dalam dictionary
if '002' in data_mahasiswa:
    print("Mahasiswa dengan ID 002 adalah:", data_mahasiswa['002'])

# Memeriksa apakah kunci tidak ada
if '004' not in data_mahasiswa:
    print("Mahasiswa dengan ID 004 tidak ditemukan.")

#Dalam contoh ini:

#Kita menggunakan operator in untuk memeriksa apakah elemen "biru" ada dalam set warna.
#Kita juga menggunakan not in untuk memeriksa apakah "kuning" tidak ada dalam set.
#Pada bagian dictionary, kita memeriksa apakah kunci "002" ada dalam data_mahasiswa, dan 
  #jika ada, kita mencetak nama mahasiswa yang sesuai.
#Terakhir, kita memeriksa apakah kunci "004" tidak ada dalam dictionary.