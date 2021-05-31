# REKURSIF 
# Untung Mangkunegara 71200619

# Aku ingin membuat program untuk menghitung faktorial. Programnya nanti akan meminta input user untuk mengisikan angka faktorial yang akan dihitung.
# Angka positif = program jalan
# Angka negatif = programnya tidak jalan dan memberikan output gagal

def faktorial(angka):
    if angka==1:
        return angka
    else:
        return angka*faktorial(angka-1)

# Input User
angka=int(input("Masukkan angka: "))

if angka < 0:
    print("Angka faktorial tidak bisa negatif")
elif angka == 0:
    print("Faktorial dari 0 adalah 1")
else:
    print("Faktorial dari ",angka ,"adalah",faktorial(angka))