# Inisialisasi counter dan akumulator
jumlah_mhs = 0
total_nilai = 0

# Input nilai pertama
nilai = float(input("Masukkan nilai mahasiswa (-1 untuk berhenti): "))

# Perulangan while dengan sentinel -1
while nilai != -1:
    jumlah_mhs += 1
    total_nilai += nilai
    nilai = float(input("Masukkan nilai mahasiswa (-1 untuk berhenti): "))

# Perhitungan dan output hasil
print("\n--- Hasil Pengolahan Nilai ---")
if jumlah_mhs > 0:
    rata_rata = total_nilai / jumlah_mhs
    print("Jumlah mahasiswa : {jumlah_mhs}")
    print("Total nilai      : {total_nilai:g}")
    print("Rata-rata nilai  : {rata_rata:.2f}")
else:
    print("Tidak ada data nilai mahasiswa yang dimasukkan.")