# variabel dan type data
nama = "Muhammad Akmal Firmansyah" 
age = 19
haight = 165.9
isStudent = True
print(nama, age, haight, isStudent)
print(type(nama), type(age), type(haight), type(isStudent))

# operator
a, b = 2, 4
print(a+b, a-b, a*b, b/a, b//a, a%b, b**a)

# input and casting
nama = str(input("Masukkan nama kamu: "))
age = int(input("Masukkan tanggal lahir kamu: "))
print(nama)
print(age)
print(f"nama kamu adalah {nama}, dan umur kamu adalah: {age}")

# percabangan
umur = 12
if umur < 13 :
    kategori = "anak anak"
elif umur > 13 and umur < 18:
    kategori  = "remaja"
elif umur > 18 and  umur < 40: 
    kategori = "dewasa"
else:
    kategori = "jokowi"

print(f"jika umur kamu {umur}, kategori kamu adalah {kategori}")


