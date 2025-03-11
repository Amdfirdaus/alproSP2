#mencari luas persegi dengan rumus s x s
#fungsi dari casting agar operator dapat berjalan,jika operator perkalian atau dipangkatkan 2 fungsi akan error atu tidak berjalan
sisi = float(input("masukkan panjang sisi persegi = "))
luas = sisi **2
print (f"luas perseginya dengan sisi {sisi} adalah = {luas} ")

#jika operator penjumlah angka hanya digabungkan bukan di jumlahkan
#contoh:
print("penjulahan")
print("-"*30)
angka1 = int(input("masukkan angka 1 = "))
angka2 = int(input("masukkan angka 2 = "))

total = angka1 + angka2

print(f"hasil penjumlahan = {total}")
