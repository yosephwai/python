#diketahui
berat_telur = 5
harga_telur = 26_000
harga_angkos = 3_500
uang_ibu = 200_000

#ditanya 

total_harga_telur = harga_telur * berat_telur
total_ongkos = harga_angkos * 2
total_pengeluaran_ibu = total_harga_telur + total_ongkos
sisa_uang_ibu = uang_ibu - total_pengeluaran_ibu

#dijawab 

print(f'''
        berat telur {berat_telur} kg
        harga telur Rp.{harga_telur} kg
        transport pulang dan pergi dengan tarif Rp.{total_ongkos}
        uang ibu Rp.{uang_ibu}

        sisa uang ibu {sisa_uang_ibu}
        ''')

#Algotima :

    # 1. Memulai Program
    # 2. Mendefenisikan variabel yang diperlukan, termasuk uang, harga dan berat telur 
    # 3. Menghitung total harga telur berdasarkan harga per kilogram dan berat yang dibeli
    # 4. Menghitung total ongkos transportasi untuk perjalanan pulang pergi
    # 5. Menghitung total pengeluaran ibu yang merupakan jumlah dari total harga telur dan total ongkos
    # 6. Menghitung sisa uang ibu setelah pengeluaran 
    # 7. Menampilkan informasi yang relatif kepada pengguna, termasuk berat telur, harga per kilogram,
    #    ongkos trasportasi, uang ibu dan sisa uang  
    # 8. mengakhiri Program
    