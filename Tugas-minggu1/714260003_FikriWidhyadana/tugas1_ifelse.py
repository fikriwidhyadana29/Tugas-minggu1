# ======
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama : Fikri Widhyadana
# Nim : 714260003
# Kelas : 1A 4 TI
# ======

print("="*45)
print("  PROGRAM PENILAIAN MAHASISWA")
print("="*45)

nilai_input = input("Masukkan nilai akhir (0-100):")

nilai = float(nilai_input)

if nilai < 0 or nilai >100:
    print("\n[ERROR]Input tidak valid!Nilai harus diantara 0-100.")
else:

    if nilai >=85:
        huruf = "A"
        status = "Lulus"
    elif nilai >=70:
        huruf = "B"
        status = "Lulus"
    elif nilai >=60:
        huruf = "C"
        status =  "Lulus"
    elif nilai >=50:
        huruf = "D"
        status = "Tidak Lulus"
    else:
        huruf = "E"
        status = "Tidak Lulus"

    print("-"*45)
    print(f"Nilai Angka : {nilai}")
    print(f"Huruf Mutu : {huruf}")
    print(f"Status : {status}")
    print("-"*45)

print("Terima kasih telah menggunakan program ini.") 
print("="*45)