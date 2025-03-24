berat_badan = float(input("Masukkan berat badan : "))
tinggi_badan = float(input("Masukkan tinggi badan : "))
tensi = float(input("Masukkan tensi darah : "))

if berat_badan >= 60:
    print(f"anda lalus test berat badan dengan berat {berat_badan}")
elif tinggi_badan >= 165 :
    print (f"anda lulus test tinggi badan dengan tinggi {tinggi_badan}")
elif tensi >= 80:
    print (f"anda lulus tensi darah{tensi}")
else:
    print("anda tidak lulus seleksi polisi")