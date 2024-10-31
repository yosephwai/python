# Gaji Pokok
gaji_pokok = 300000

# Input Data Karyawan
print("Program Menghitung Gaji Karyawan")
nama_karyawan = input("Nama Karyawan: ")
golongan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Jumlah Jam Kerja: "))

# Hitung Tunjangan Jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid.")

# Hitung Tunjangan Pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid.")

# Hitung Honor Lembur
lembur = 0
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500

# Total Gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Cetak Hasil
print("\nKaryawan yang bernama:", nama_karyawan)
print("Honor yang diterima:")
print("Tunjangan Jabatan: Rp", tunjangan_jabatan)
print("Tunjangan Pendidikan: Rp", tunjangan_pendidikan)
print("Honor Lembur: Rp", lembur)
print("_______+")
print("Total Gaji: Rp", total_gaji)
