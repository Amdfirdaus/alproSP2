nama = input("Masukan nama : ")
tinggi_badan = float(input("Masukkan tinggi badan : "))
berat_badan = float (input("masukkan berat badan : "))

if tinggi_badan >= 165 :
    
    if berat_badan >= 60:
        print("anda lulus seleksi polisi ")
    else:
        print("anda tidak lulus seleksi polisi ")
else:
    print("anda tidak lulus seleksi polisi")