# Program Lirik Lagu "Anak Ayam"
# Meminta input bilangan bulat dari pengguna
n = int(input("Masukkan bilangan bulat (1 ≤ N ≤ 100): "))

# Memastikan input berada dalam rentang yang valid
if 1 <= n <= 100:
    print("Tek kotek kotek kotek, anak ayam turun berkotek")
    
    # Menguraikan lirik sesuai dengan nilai N
    for i in range(n, 0, -1):
        if i == 1:
            print(f"anak ayam turunlah {i} mati satu tinggallah induknya")
        else:
            print(f"anak ayam turunlah {i} mati satu tinggallah {i - 1}")
else:
    print("Masukan tidak valid. Harap masukkan bilangan bulat antara 1 dan 100.")


# Penjelesan 
# Input Bilangan Bulat: Program meminta pengguna untuk memasukkan bilangan bulat N.
# Validasi Input: Memastikan bahwa N berada dalam rentang 1 hingga 100.
# Mencetak Lirik:
    # Mencetak baris awal lagu: "Tek kotek kotek kotek, anak ayam turun berkotek".
    # Menggunakan loop for untuk menghitung mundur dari N hingga 1:
        #Jika i adalah 1, mencetak lirik "anak ayam turunlah 1 mati satu tinggallah induknya".
        # Untuk nilai lainnya, mencetak lirik "anak ayam turunlah {i} mati satu tinggallah {i - 1}".
