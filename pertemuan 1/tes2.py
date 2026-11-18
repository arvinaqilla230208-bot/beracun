total_penjualan = 0
jumlah_transaksi = 0
tertinggi = 0

n = int(input("Masukkan jumlah transaksi penjualan: "))

for i in range(1, n + 1):
    nilai = float(input(f"Masukkan nilai penjualan transaksi ke-{i}: "))
    
    jumlah_transaksi += 1
    total_penjualan += nilai
    
    if nilai > tertinggi:
        tertinggi = nilai

print("\n--- Hasil Rekapitulasi Penjualan ---")
if jumlah_transaksi > 0:
    rata_rata = total_penjualan / jumlah_transaksi
    print(f"Jumlah transaksi    : {jumlah_transaksi}")
    print(f"Total penjualan     : Rp{total_penjualan:,.0f}".replace(",", "."))
    print(f"Rata-rata penjualan : Rp{rata_rata:,.0f}".replace(",", "."))
    print(f"Penjualan tertinggi : Rp{tertinggi:,.0f}".replace(",", "."))
else:
    print("Tidak ada transaksi yang diproses.")