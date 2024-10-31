# Mendefinisikan dua variabel
a = 60  # Dalam biner: 0011 1100
b = 13  # Dalam biner: 0000 1101

# Operator AND bitwise
and_result = a & b  # Hasil: 0000 1100 (12 dalam desimal)
print("Hasil AND bitwise:", and_result)

# Operator OR bitwise
or_result = a | b  # Hasil: 0011 1101 (61 dalam desimal)
print("Hasil OR bitwise:", or_result)

# Operator XOR bitwise
xor_result = a ^ b  # Hasil: 0011 0001 (49 dalam desimal)
print("Hasil XOR bitwise:", xor_result)

# Operator NOT bitwise
not_result = ~a  # Hasil: 1100 0011 (dalam desimal: -61)
print("Hasil NOT bitwise:", not_result)

# Operator shift left
left_shift_result = a << 2  # Hasil: 1111 0000 (240 dalam desimal)
print("Hasil Shift Left:", left_shift_result)

# Operator shift right
right_shift_result = a >> 2  # Hasil: 0000 1111 (15 dalam desimal)
print("Hasil Shift Right:", right_shift_result)


#Dalam contoh ini:

#AND (&): Menghasilkan bit 1 hanya jika kedua bit adalah 1.
#R (|): Menghasilkan bit 1 jika salah satu atau kedua bit adalah 1.
#XOR (^): Menghasilkan bit 1 jika satu bit adalah 1 dan yang lainnya adalah 0.
#NOT (~): Mengubah semua bit, mengubah 0 menjadi 1 dan sebaliknya.
#Shift Left (<<): Menggeser semua bit ke kiri, menambahkan 0 di sisi kanan.
#Shift Right (>>): Menggeser semua bit ke kanan