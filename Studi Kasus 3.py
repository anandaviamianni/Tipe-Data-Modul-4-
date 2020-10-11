# Seorang pedagang buah bernama Ifen selalu kesusahan ketika mengecek stok buah yang ada di tokonya, 
# akhirnya Ifen pun meminta tolong kepada Anda untuk membuatkan sebuah program untuk mengecek stok barang di tokonya.  

print("PROGRAM CEK STOK BUAH")
stok_buah = ("Pisang","Apel","Nanas","Mangga","Semangka","Salak")
print("Stok buah yang tersedia: ")
for buah in stok_buah:
    print(buah,end =" ")

cari = input("\nCari buah apa? :")
if cari in stok_buah:
    print("Buah",cari,"Tersedia")
else:
    print("Buah",cari,"Tidak Tersedia")