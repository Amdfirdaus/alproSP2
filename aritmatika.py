
jumlahhari=int(input("masukkan jumlah hari = "))
upahperhari = 20000
persentasibonus = 20

# Operator Perkalian: menghitung total pendapatan
pendapatan = upahperhari * jumlahhari
print(f"Gaji anda sebesar = Rp{pendapatan:,.2f}")

# Operator pembagian,perkalian,penjumlahan : menghitung gaji dengan bonus
gajidanbonus = (persentasibonus / 100 * pendapatan)+ pendapatan
print(f"Gaji dengan bonus = Rp{gajidanbonus:,.2f}")

# Operator Pembagian: menghitung rata-rata gaji per hari setelah bonus
rata_rata_perhari = gajidanbonus / jumlahhari
print(f"Rata-rata gaji per hari setelah bonus = Rp{rata_rata_perhari:,.2f}")

#operator floor division : hasil pembagian yang dibulatkan, tidak akan berfungsi jika pembagian sudah bulat
rata_rata_perhari = gajidanbonus // jumlahhari
print(f"Rata-rata gaji yang dibulatkan = Rp{rata_rata_perhari:,.2f}")

# Operator Modulus: menghitung sisa dari pembagian gaji dengan jumlah hari kerja
sisa_gaji = gajidanbonus % jumlahhari
print(f"Sisa gaji setelah dibagi dengan jumlah hari = Rp{sisa_gaji:,.2f}")

# Operator Eksponen: menghitung gaji dengan bonus dipangkatkan 2 kali
gaji_kuadrat = gajidanbonus ** 2
print(f"Gaji dengan bonus dipangkatkan 2 = Rp{gaji_kuadrat:,.2f}")
