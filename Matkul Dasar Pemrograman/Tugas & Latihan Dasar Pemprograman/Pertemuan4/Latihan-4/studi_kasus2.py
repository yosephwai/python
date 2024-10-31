# Data Biaya Kuliah
biaya_kuliah = {
    "TI": 1500000,  # Teknik Informatika
    "SI": 2400000,  # Sistem Informasi
    "DKV": 1600000, # Desain Komunikasi Visual
    "SIA": 2000000, # Sistem Informasi Akuntansi
}

# Input Data Calon Mahasiswa
nis = input("Input NIS: ")
nama = input("Input Nama: ")
jurusan = input("Input Jurusan [TI/SI/DKV]: ")

# Proses
if jurusan in biaya_kuliah:
    biaya = biaya_kuliah[jurusan]
else:
    print("Jurusan tidak valid.")
    exit()

# Cetak Hasil
print("------------------------------------")
print("           DATA CALON MAHASISWA")
print("------------------------------------")
print("NIS: " + nis)
print("Nama: " + nama)
print("Jurusan: " + jurusan)
print("Biaya Kuliah: Rp " + str(biaya))
print("------------------------------------")
