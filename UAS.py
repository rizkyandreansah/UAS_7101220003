#Soal Nomor 5
# print ("\n======PROGRAM PENJUALAN BUKU======")
# hstuan = float (input("Harga Satuan Buku : "))
# jml = float (input("Jumlah Buku Yang Dibeli : "))
# disk = float(input("Diskon Buku : ")) 

# #Hitung Total Harga
# TotalHarga = hstuan * jml
# TotalHargaDisk = TotalHarga - (TotalHarga * (disk / 100))

# print ("\n======PROGRAM PENJUALAN BUKU======")
# print(f"{'Harga Satuan' :<20} {':'} {int(hstuan)} ")
# print(f"{'Jumlah Pembelian' :<20} {':'} {int(jml)} Buku " )
# print(f"{'Diskon ':<20} {':'} {int(disk)}%")
# print(f"{'Total Harga' :<20} {':'} {int(TotalHargaDisk)} ")

# #===========================================================================================

# #Soal A Nomor 3

# hnormal=int(input("Harga Normal Komputer : ")) 

# #Algoritma untuk menghitung besarnya uang muka dan cicilan setiap bulan
# hkredit = hnormal + (hnormal * 0.2 )
# umuka = hkredit * 0.3
# ucicil = (hkredit - umuka) / 12 

# print(f"Uang Muka :, {int(umuka)}")
# print(f"Uang Cicilan Perbulan , {int(ucicil)}")

# #=============================================================================================================
# #Soal A Nomor 4

# A = 3
# B = 9

# if A > B:
#     C = A * B
# else:
#     C = A + B

# D = C * C

# print(C)
# print(D)

#========================================================================================================
 
# Soal No 6
# def main():
#     print("\n======PROGRAM PERHITUNGAN GAJI KARYAWAN PT. XYZ======")
#     print("-----------------------------------------------------")
#     print("                    DATA  PEGAWAI                    ")
#     print("-----------------------------------------------------")

#     name = input(f"{'Nama':<20}{':':<3}")
#     Gol = input(f"{'Golongan':<20}{':':<3}")
#     jamKerja = int(input(f"{'Total Jam Kerja':<20}{':':<3}"))

#     if jamKerja < 200: lembur = 0
#     elif jamKerja > 200: lembur = jamKerja - 200
#     if Gol.upper() == 'A':
#         gaji = 1_200_000
#         uangTip = gaji * .1
#         lembur *= 5_000
#     elif Gol.upper() == 'B':
#         gaji = 1_600_000
#         uangTip = gaji * .15
#         lembur *= 7_500
#     elif Gol.upper() == 'C':
#         gaji = 2_000_000
#         uangTip = gaji * .2
#         lembur *= 10_000
#     total = gaji + uangTip + lembur
    
#     gaji = toCurrency(gaji)
#     uangTip = toCurrency(uangTip)
#     lembur = toCurrency(lembur)
#     total = toCurrency(total)

#     print("-----------------------------------------------------")
#     print("                  PERHITUNGAN  GAJI                  ")
#     print("-----------------------------------------------------")
#     print(f"{'Gaji Pokok':<20}{':':<3}Rp. {gaji}")
#     print(f"{'Tunjangan':<20}{':':<3}Rp. {uangTip}")
#     print(f"{'Lembur':<20}{':':<3}Rp. {lembur}")
#     print("-----------------------------------------------------")
#     print(f"{'Total':<20}{':':<3}Rp. {total}")
#     print("-----------------------------------------------------")

# def toCurrency(value):
#     return f"{value:,.2f}".replace('.', ' ').replace(',', '.').replace(' ', ',')

# if __name__ == "__main__": main()

#=========================================================================================================

#Soal C

data = []

for i in range(5):
    nim = input (f"Masukkan nim mahasiswa ke-{i+1}: ")
    nama = input (f"Masukkan nama mahasiswa ke-{i+1}: ")
    nilai = float(input(f"masukkan nilai mahasiswa ke-{i+1}: "))

    data.append((nim, nama, nilai))

print("=================== PROGRAM PENGOLAHAN DATA MATKUL ABK ==================")
print("\n=========================================================================")
print("| NO |   NIM         |   NAMA                  | NILAI     | KETERANGAN |")
print("=========================================================================")

Jumlah = 0
rataRata = 0 
nilaiTertinggi = 0
nilaiTerendah = 100
jumlahLulus = 0
jumlahGagal = 0

for i, (nim, nama, nilai) in enumerate(data):
    Jumlah += nilai
    if nilai > nilaiTertinggi:
        nilaiTertinggi = nilai
    if nilai < nilaiTerendah:
        nilaiTerendah = nilai

    keterangan = "LULUS" if nilai >= 56 else "GAGAL"
    if keterangan == "LULUS":
        jumlahLulus += 1
    else:
        jumlahGagal += 1
    print(f"|{i+1:2}  |   {nim:10}  |   {nama:20}  | {nilai:6.2f}    | {keterangan}      |")
    print("_"*73)

rata_rata = Jumlah / len(data)



print(f"Jumlah mahasiswa: {len(data)}")
print(f"Rata-rata nilai: {rata_rata:.2f}")
print(f"Mahasiswa dengan nilai tertinggi: {nilaiTertinggi}")
print(f"Mahasiswa dengan nilai terendah: {nilaiTerendah}")
print(f"Jumlah mahasiswa yang lulus: {jumlahLulus}")
print(f"Jumlah mahasiswa yang gagal: {jumlahGagal}")