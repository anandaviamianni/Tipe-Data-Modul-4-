# Jody merupakan seorang Software Developer, ia sedang membuat sebuah program yang dapat 
# mengkonversi urutan bulan menjadi nama bulan secara berurutan. Dimana jika pengguna program 
# konversi tersebut menginputkan nomor maka akan mencetak nama bulannya.

print("PROGRAM KONVERENSI BULAN")
nama_bulan = ("Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember")
urutan_bulan = int(input("Bulan ke :"))

if urutan_bulan >= 1 and urutan_bulan <=12:
    print(nama_bulan[urutan_bulan-1])
else:
    print("Gak ada")
