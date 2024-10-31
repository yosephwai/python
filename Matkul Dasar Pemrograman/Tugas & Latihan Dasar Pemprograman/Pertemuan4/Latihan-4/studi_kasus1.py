# Input
pembeli = input("Masukan Nama Pembeli: ")
no_hp = input("Masukan  No. Handphone: ")
jurusan = input("Masukan Jurusan [SBY/BL/LMP]: ")
jumlah = int(input("Masukkan Jumlah Beli: "))  # Input Jumlah Beli

# Proses
if jurusan == "SBY":
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    namajurusan = "Bali"
    harga = 350000
else:
    namajurusan = "Lampung"
    harga = 500000

# Proses potongan
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0

total = (jumlah * harga) - potongan

# Cetak Hasil
print("------------------------------------")
print(" PENJUALAN TIKET BUS")
print("zzz")
print("------------------------------------")
print("Nama Pembeli: " + str(pembeli))
print("No. Handphone: " + str(no_hp))
print("Kode Jurusan yang dipilih: " + str(jurusan))
print("Nama Kota Tujuan: " + str(namajurusan))
print("Harga per Tiket: ", harga)
print("Jumlah Beli: ", jumlah)
print("------------------------------------")
print("Potongan yang didapat: ", potongan)
print("Total Bayar: ", total)

ubay = int(input("Masukkan Uang Bayar: "))
uangkembali = ubay - total
print("Uang Kembali: ", uangkembali)
