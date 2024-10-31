# Gaji pokok salesman
gaji_pokok = 5000000

# Input jumlah produk yang terjual dan harga satuan
banyak_produk = int(input("Masukkan banyak produk yang terjual: "))
harga_satuan = float(input("Masukkan harga satuan produk: "))

# Menghitung total omset penjualan
omset_penjualan = banyak_produk * harga_satuan

# Menghitung bonus
if banyak_produk > 100:
    bonus = 0.20 * omset_penjualan  # 20% bonus
else:
    bonus = 0.10 * omset_penjualan  # 10% bonus

# Menghitung total gaji
total_gaji = gaji_pokok + bonus

# Menampilkan hasil
print("Omset Penjualan: Rp", omset_penjualan)
print("Bonus: Rp", bonus)
print("Total Gaji: Rp", total_gaji)
