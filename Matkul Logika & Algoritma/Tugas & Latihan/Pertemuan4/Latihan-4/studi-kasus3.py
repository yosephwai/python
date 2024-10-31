# Input lama pemakaian
lama_pemakaian = float(input("Masukkan lama pemakaian (dalam jam): "))

# Menghitung biaya
if lama_pemakaian <= 3:
    biaya = lama_pemakaian * 6000
else:
    biaya_3_jam = 3 * 6000
    sisa_jam = lama_pemakaian - 3
    biaya_sisa_jam = sisa_jam * 5000
    total_biaya = biaya_3_jam + biaya_sisa_jam

# Menampilkan total biaya
print("Total Biaya: Rp", total_biaya)

 +-------------------------+
 |          Start          |
 +-------------------------+
            |
            v
 +-------------------------+
 | Input lama pemakaian    |
 +-------------------------+
            |
            v
 +-------------------------+
 |  Lama pemakaian ≤ 3?    |
 +----------+--------------+
            | Yes           | No
            v              |
 +-----------------+       +-----------------------+
 |  Biaya = lama   |       | Biaya_3_jam = 3 * 6000 |
 |  pemakaian *    |       +-----------------------+
 |  6000           |       | sisa_jam = lama pemakaian - 3 |
 +-----------------+       | Biaya_sisa_jam = sisa_jam * 5000 |
            |              +-----------------------+
            |                     |
            v                     v
 +-----------------+       +-----------------------+
 |  Tampilkan      |       | Total_Biaya = Biaya_3_jam + Biaya_sisa_jam |
 |  Total Biaya    |       +-----------------------+
 +-----------------+                     |
            |                           v
            |                     +------------------+
            |                     |  Tampilkan Total  |
            |                     |  Biaya            |
            |                     +------------------+
            v
 +-------------------------+
 |          End            |
 +-------------------------+
