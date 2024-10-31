# Input gaji pokok dan total jam kerja
gaji_pokok = float(input("Masukkan gaji pokok: Rp "))
jam_kerja = float(input("Masukkan total jam kerja: "))

# Menghitung tunjangan
tunjangan = 0.20 * gaji_pokok

# Menghitung lembur
lembur = 0
if jam_kerja > 200:
    kelebihan_jam = jam_kerja - 200
    lembur = kelebihan_jam * 20000  # Uang lembur per jam kelebihan

# Menghitung gaji sebelum pajak
gaji_sebelum_pajak = gaji_pokok + tunjangan + lembur

# Menghitung pajak
pajak = 0.10 * gaji_sebelum_pajak

# Menghitung gaji setelah pajak
gaji_setelah_pajak = gaji_sebelum_pajak - pajak

# Menampilkan hasil
print("\n--- Rincian Gaji ---")
print("Gaji Pokok: Rp", gaji_pokok)
print("Tunjangan (20%): Rp", tunjangan)
print("Lembur: Rp", lembur)
print("Gaji Sebelum Pajak: Rp", gaji_sebelum_pajak)
print("Pajak (10%): Rp", pajak)
print("Gaji Setelah Pajak: Rp", gaji_setelah_pajak)
