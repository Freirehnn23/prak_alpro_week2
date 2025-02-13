pajak = 14/100
beli_baju = 10/100
beli_atk = 1/100
sedekah = 25/100

gaji_perjam = int(input("Masukan gaji perjam yang diinginkan: "))
jumlah_jam_kerja = int(input("Masukan total jam kerja dalam satu minggu: "))

print("=======================================")
total_pendapatan_kotor = (gaji_perjam * jumlah_jam_kerja) * 5
setelah_pajak = total_pendapatan_kotor -  (total_pendapatan_kotor * pajak)
pakaian_aksesoris = setelah_pajak * beli_baju
untuk_atk = setelah_pajak * beli_atk
sisa_uang_sementara = setelah_pajak - pakaian_aksesoris - untuk_atk
untuk_sedekah = sisa_uang_sementara * sedekah
diterima_yatim = untuk_sedekah * 30/100
diterima_duafa = untuk_sedekah * 70/100

print("Pendapatan Budi sebelum bayar pajak", total_pendapatan_kotor)
print("Pendapatan Budi setelah bayar pajak adalah: ", (setelah_pajak))
print("Budget budi untuk membeli pakaian dan aksesoris adalah: ", (pakaian_aksesoris))
print("Budget budi untuk membeli ATK adalah:", (untuk_atk))
print("Budget budi untuk sedekah adalah:", (untuk_sedekah))
print("Sedekah yang diterima yatim adalah:", (diterima_yatim))
print("Sedekah yang diterima duafa adalah:", (diterima_duafa))




