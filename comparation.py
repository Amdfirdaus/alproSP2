def tentukan_tiket(usia):
    # Tentukan jenis tiket berdasarkan usia
    if usia < 3:
        tiket = "Gratis"
    elif usia >= 60:
        tiket = "Tiket Dewasa dengan Diskon"
    elif 3 <= usia <= 11:
        tiket = "Tiket Anak-Anak"
    else:
        tiket = "Tiket Dewasa"
        
    print("-"*20)
    print (f"Nama = {nama}")
    print(f"Usia = {usia} tahun")
    print(f"Jenis Tiket = {tiket}")

# Input usia pelanggan
nama = input("masukkan nama = ")
usia = int(input("Masukkan usia = "))

# Tentukan jenis tiket
tentukan_tiket(usia)
