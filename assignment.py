text = "Selamat Datang Di Villa Kami"
print(f"{text:^50}")  # 30 adalah panjang total string
print("-"*50)
# Harga tarif per orang
hargatarifperorang = 20000

# Diskon untuk wisata 2%
diskon_persen = 0.02  # Diskon 2%

# Pajak untuk tempat wisata 5%
pajak_wisata = 0.05  # Pajak 5%

# Jumlah orang
jumlah_orang = 8

# Menghitung total harga tarif untuk 8 orang menggunakan operator perkalian (*)
total_harga = hargatarifperorang * jumlah_orang
print(f"Total harga tarif untuk {jumlah_orang} orang = Rp{total_harga:,.2f}")

# Menghitung diskon menggunakan operator perkalian dan pengurangan (-)
diskon = total_harga * diskon_persen
total_setelah_diskon = total_harga - diskon
print(f"Total harga setelah diskon = Rp{total_setelah_diskon:,.2f}")

# Menghitung pajak menggunakan operator perkalian (*)
pajak = total_setelah_diskon * pajak_wisata
total_setelah_pajak = total_setelah_diskon + pajak
print(f"Total harga setelah pajak = Rp{total_setelah_pajak:,.2f}")

# Menghitung harga per orang menggunakan operator pembagian (/)
harga_per_orang_akhir = total_setelah_pajak / jumlah_orang
print(f"Harga tarif per orang setelah diskon dan pajak = Rp{harga_per_orang_akhir:,.2f}")

# Menggunakan operator modulus (%) untuk mencari sisa pembagian harga total dengan 1 hari
sisa = total_setelah_pajak % 1
print(f"Sisa pembagian total harga 1 hari = {sisa:.2f}")

# Menggunakan operator floor division (//) untuk membagi total dengan 1 hari dibulatkan
hasil_bagi = total_setelah_pajak // 1
print(f"Hasil pembagian total harga setelah pajak dibagi 1 = Rp{hasil_bagi:,.2f}")

# Menggunakan operator eksponen (**) untuk menghitung pangkat
pangkat_harga = total_setelah_pajak ** 2
print(f"Total harga setelah pajak dipangkatkan 2 = Rp{pangkat_harga:,.2f}")
