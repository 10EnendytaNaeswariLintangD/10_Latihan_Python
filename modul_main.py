from kalkulasi_geometri import *
from analisis_angka import *

while True:
    print("\n------------------------------------------")
    print("      PROGRAM MATEMATIKA & LOGIKA        ")
    print("------------------------------------------")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("------------------------------------------")
    
    pilihan_menu = input("Pilih menu (1-7): ")
    
    if pilihan_menu == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Luas Persegi: {hitung_luas_persegi_v1(sisi)}")
        
    elif pilihan_menu == "2":
        sisi = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Keliling Persegi: {hitung_keliling_persegi_v1(sisi)}")
        
    elif pilihan_menu == "3":
        angka_in = int(input("Masukkan angka: "))
        if status_bilangan_prima(angka_in):
            print(f"Angka {angka_in} adalah Bilangan Prima.")
        else:
            print(f"Angka {angka_in} bukan Bilangan Prima.")
            
    elif pilihan_menu == "4":
        angka_in = int(input("Masukkan angka: "))
        print(f"Angka {angka_in} tergolong Bilangan {cek_ganjil_atau_genap(angka_in)}.")
            
    elif pilihan_menu == "5":
        r = float(input("Masukkan jari-jari: "))
        print(f"Hasil Luas Lingkaran: {hitung_luas_lingkaran_v1(r)}")

    elif pilihan_menu == "6":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga: {hitung_luas_segitiga_v1(a, t)}")
        
    elif pilihan_menu == "7":
        print("Program selesai, terima kasih!")
        break
    else:
        print("Pilihan salah, masukkan angka 1 sampai 7.")
