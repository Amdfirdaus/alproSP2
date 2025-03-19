# Harga awal barang
harga_barang = 100000
diskon1 = 0.10
diskon2 = 0.05
pajak = 0.12

harga_barang -= harga_barang * diskon1
print(f"Harga setelah diskon pertama: {harga_barang:,.2f}")

harga_barang -= harga_barang * diskon2
print(f"Harga setelah diskon kedua: {harga_barang:,.2f}")

harga_barang += harga_barang * pajak
print(f"Harga setelah pajak: {harga_barang:,.2f}")

harga_barang //= 1 
print(f"Harga akhir setelah pembulatan: {harga_barang:,.2f}")

harga_barang %= 1
print(f"Sisa harga setelah pembulatan: {harga_barang:,.2f}")