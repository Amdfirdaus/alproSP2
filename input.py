#inputan text
nama_makanan =input ("masukkan nama makanan = ")
#inputan angka/harga (bilangan bulat)
jumlah = int(input("masukkan jumlah  = "))
#inputan angka (bilangan desimal)
harga = float(input("masuk kan harga = "))

total = jumlah * harga

print("Nama Makanan =",nama_makanan)
print(f"total yang harus dibayar = {total:,.3f}")


