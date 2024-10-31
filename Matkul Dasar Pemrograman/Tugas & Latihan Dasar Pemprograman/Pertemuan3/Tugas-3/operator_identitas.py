# Mendefinisikan dua variabel dengan objek yang sama
a = [1, 2, 3]
b = a  # b adalah referensi yang sama dengan a

# Menggunakan operator 'is'
if a is b:
    print("a dan b adalah identik (referensi yang sama).")

# Menggunakan operator 'is not'
c = [1, 2, 3]  # c adalah objek baru, meskipun nilai sama
if a is not c:
    print("a dan c tidak identik (referensi yang berbeda).")

# Contoh dengan tipe data non-mutable
x = 1000
y = 1000

# Memeriksa identitas
if x is y:
    print("x dan y adalah identik (referensi yang sama).")
else:
    print("x dan y tidak identik (referensi yang berbeda).")

#Dalam contoh ini:

#is digunakan untuk memeriksa apakah dua variabel merujuk ke objek yang sama di memori. 
  #Dalam kasus a dan b, keduanya merujuk ke daftar yang sama, jadi hasilnya adalah true.
#is not digunakan untuk memeriksa apakah dua variabel tidak merujuk ke objek yang sama. 
  #a dan c memiliki nilai yang sama tetapi merupakan objek yang berbeda di memori.
#Pada variabel x dan y, meskipun keduanya memiliki nilai yang sama (1000), Python bisa membuat 
  #dua objek terpisah untuk angka besar, sehingga hasilnya mungkin false tergantung pada implementasi Python.