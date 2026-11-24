# =========================================================
# PROYEK INDIVIDU ELEMEN 5: ASISTEN ANALISIS DATA IPK
# SMK TELKOM MALANG - KELAS X RPL 3
# Nama Siswa: Neila Putri Nafisya
# =========================================================

# 1. Menyimpan dataset dalam List
dataset_IPS = [3.20, 3.12, 3.95, 3.76, 3.82]

# 2. Menghitung total dan rata-rata dengan Loop
variable = 0

for n in dataset_IPS:
    variable = variable + n

rata_rata = variable / len(dataset_IPS)

# 3. Output dan Kesimpulan Otomatis dengan If-Else
print("Total Nilai IPS :", round(variable, 2))
print("Rata-rata IPK   :", round(rata_rata, 2))

if rata_rata >= 3.90:
    print("Predikat: Summa Cumlaude")
elif rata_rata >= 3.70:
    print("Predikat: Magna Cumlaude")
elif rata_rata >= 3.50:
    print("Predikat: Cumlaude")
else:
    print("Predikat: Non Cumlaude")