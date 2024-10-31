merek = input ("merek baju P/A/S :")
if merek == 'P' :
    print("merek Polo")
    ukuran = input ("ukuran L/M/S :")
    if ukuran == 'L' :
        print('harga = 300000')
    if ukuran == 'M' :
        print('harga = 225000')
    else :
        print('harga = 175000')
elif merek == 'A':
    print('merek alisan')
    ukuran = input("ukuran M/L/S :")
    if ukuran == 'L':
        print("harga = 275000")
    elif ukuran == "M":
        print('harga = 200000')
    else :
        print ("merek EtYess")
        ukuran = input('ukuran L/M/S :')
        if ukuran== 'L':
            print("harga = 250000")
        elif ukuran == 'M':
            print("harga = 175000")
        else :
            print('harga = 1250000')


    




