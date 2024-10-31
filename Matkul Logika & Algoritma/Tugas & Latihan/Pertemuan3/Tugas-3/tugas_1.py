kelereng_aldi = int(input("masukan kelereng Aldi : ")) 
kelereng_budi = (kelereng_aldi - 15)
kelereng_anto = 2 * (kelereng_aldi + kelereng_budi)
kelereng_agung = (kelereng_aldi + kelereng_budi + kelereng_anto) - 5
jumlah = kelereng_budi + kelereng_anto + kelereng_agung

print(f'kelereng budi adalah    : {kelereng_budi}')
print(f'kelereng antoh adalah   : {kelereng_anto}')
print(f'kelereng agung adalah   : {kelereng_agung}')

print(f'jumlah kelereng semuanya adalah : {jumlah}')