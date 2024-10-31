# Judul program
judul = "Toko Mainan Anak"
lebar = 40  # Tentukan lebar total
print(judul.center(lebar))
print("*" *lebar)

# Mengambil input dari pengguna
nama_pembeli = input("Masukkan nama pembeli: ")
kode_mainan = input("Masukkan kode mainan: ")
harga = float(input("Masukkan harga: "))
jumlah_beli = int(input("Masukkan jumlah beli: "))

# Menghitung total harga
total_harga = harga * jumlah_beli

# Menampilkan hasil
print("=" * lebar)
print("Nama Pembeli    :", nama_pembeli)
print("Kode Mainan     :", kode_mainan)
print("Harga Satuan    : Rp", harga)
print("Jumlah Beli     :", jumlah_beli)
print("Total Harga     : Rp", total_harga)

#Penjelasan:
#judul.center(lebar): Metode center() digunakan untuk mengatur teks agar berada di tengah dengan lebar yang ditentukan (dalam hal ini, 40 karakter).
#print("=" * lebar): Mencetak garis pemisah dengan panjang yang sama dengan lebar judul.
#Anda bisa menyesuaikan nilai lebar sesuai kebutuhan untuk memastikan teks terlihat di tengah