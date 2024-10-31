def triangle (n, symbol, current = 1):
    # Basic case : jika baris saat ini lebih besar dari n, hentikan rekursi
    if current > n :
        return
    
    # cetak baris dengan spasi dan symbol
    print(' ' * (n - current) + f'{symbol} ' * current)

    # Panggil fungsi rekurisif untuk mencetak baris berikutnya
    triangle (n, symbol, current + 1)

if __name__ == "__main__":

    while True :
        symbol = input ("masukan simbol :")
        try :
            hight = int(input("masukan tinggi bangunan : "))
            triangle (hight,symbol)
            exit()
        except ValueError :
            print("anda hanya bisa memasukan type data integer")