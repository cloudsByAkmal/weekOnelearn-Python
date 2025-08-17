# tugas day one 1

# hitung luas dan keliling
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

luas = p * l
keliling = 2 * (p + l)

print(f"Luas persegi dengan panjang {p}, dan lebar {l} = {luas}")
print(f"Keliling persegi dengan panjang {p}, dan lebar {l} = {keliling}")

# konversi waktu
secInput = int(input("Masukkan detik: "))

hour = secInput // 3600
modSec = secInput % 3600
minute = modSec // 60
second = modSec % 60

print(f"{hour:02d}:{minute:02d}:{second:02d}")

# BMI calculator
berat = float(input("Berat badan(kg): "))
tinggi = float(input("Tinggi badan(cm): "))

# conversi cm to m
tinggi  = tinggi / 100

#  hitung BMI
bmi = berat / (tinggi ** 2)
bmi = round(bmi, 2)

if bmi < 18.5 : 
    kategori = "Underweight"
elif 18.5 <= bmi <= 24.9 :
    kategori = "Normal"
elif 24.9 <= bmi <= 29.9 :
    kategori = "Overweight"
else :
    kategori = "Obese"
print(f"berat badan: {berat}, dan tinggi: {tinggi}")
print(f"Boddy mass index: {bmi}, kategori {kategori}")

# split bill
totalTagihan = float(input("total tagihan: "))
jumlahOrang = int(input("jumlah orang: "))

totalTagihan = round(totalTagihan, 2)
splitBill = totalTagihan / jumlahOrang
splitBill = round(splitBill, 2)

print(f"nominal per orang adalah: {splitBill}")
