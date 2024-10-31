def ayam (n : int):
    while True:
        if n <= 1 :
            print("anak ayam turunlah 1, mati satu tinggal induknya")
            break
        else :
            print (f"anak ayam turunlah {n}, mati satu tinggal {n-1}")

            n -= 1
if __name__ == "__main__":
    while True :
        try:
            J_ayam = int (input("masukan jumlah ayam : "))
            ayam(J_ayam)
            exit
        except ValueError :
            print ("anda")

        

