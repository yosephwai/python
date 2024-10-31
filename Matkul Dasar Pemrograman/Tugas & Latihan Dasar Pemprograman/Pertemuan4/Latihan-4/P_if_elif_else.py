# pernyataan if....elif....else

# disini kita menguji apakah sebuah bilangan adalah bilangan positif, nol, atau negatif 
# dan menampilkan hasilnya ke layar

bilangan = 5.5

# Coba juga ganti bilangan menjadi
# bilangan = 0
# bilangna = -5.5

if bilangan > 0 :
    print("bilangan positif")
elif bilangan == 0:
    print ("nol")
else :
    print("bilangna negatif")


kode_baju = input("masukan kode baju [SP/AD] : ")
ukuran = input("masukan ukura baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s" :
        harga = 450_000
    elif ukuran == "M" or ukuran == "m" :
        harga = 500_000
    else :
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "ADIDAS"
    if ukuran == "s" or ukuran == "S" :
        harga = 650_000
    elif ukuran == "M" or ukuran == "m" :
        harga = 700_000
    else :
        harga = 0
else :
    merk = "anda salah input kode merek"
    harga = 0

print ("-"*40)
print ("merek baju : "+str(merk))
print ("harga baju : Rp.", harga )
