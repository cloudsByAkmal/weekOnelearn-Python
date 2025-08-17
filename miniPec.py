# penilaian nilai mahasiswa (CLI)

print(" ===== Sistem Penilaian Sederhana ===== ")
nama = str(input("Nama: "))
npm = int(input("Npm: "))

nilaiTugas = float(input("Nilai Tugas: "))
nilaiUts = float(input("Nilai UTS: "))
nilaiUas = float(input("Nilai UAS: "))

nilaiAkhir = (0.3*nilaiTugas) + (0.3*nilaiUts) + (0.4*nilaiUas)

if nilaiAkhir >= 85:
    grade = 'A'
elif nilaiAkhir >= 70 and nilaiAkhir < 85:
    grade = 'B'
elif nilaiAkhir >= 55 and nilaiAkhir < 70:
    grade = 'C'
else :
    grade = 'D'

status = "LULUS" if grade in ("A","B","C") else "Tidak Lulus"

print("\n--- Rapor ---")
print(f"Nama : {nama}")
print(f"NIM  : {npm}")
print(f"Tugas: {nilaiTugas:.2f}, UTS: {nilaiUts:.2f}, UAS: {nilaiUas:.2f}")
print(f"Nilai Akhir: {nilaiAkhir:.2f}")
print(f"Grade: {grade} -> {status}")