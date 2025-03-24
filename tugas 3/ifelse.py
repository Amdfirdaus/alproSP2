nama = input("masukkan nama : ")
kekuatan_nafas = float(input("masukkan lama menyelam (dtk) : "))
print("-"*50)

if kekuatan_nafas >= 60 :
    print (f"{nama} LAYAK mengikuti seleksi berikutnya")
else :
    print(f"{nama} TIDAK LAYAK  menuju seleksi berikutnya")