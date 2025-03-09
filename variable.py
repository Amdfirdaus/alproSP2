#sebuah inputan yang disimpan didalam variable yag sudah ditentukan
namabarang = input('Nama Barang = ')
jumlahbarang =int(input('Jumlah Barang (Pcs) = '))
hargabarang = int(input ('harga barang (Rp) = '))

#proses sebuath data yang telah diinputkan
total = jumlahbarang * hargabarang

#output/hasil dari proses yang telah diinputkan
print("-"*40,"+" )
print(f'total yang harus dibayar = Rp{total:,.2f}')