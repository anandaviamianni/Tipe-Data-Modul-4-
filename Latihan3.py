print("PROGRAM CEK STOK BUAH")
stok_buah = {"Jeruk","Apel","Naga","Mangga","Pisang"}
print("Stok buah : ")
for buah in stok_buah:
    print(buah,end =" ")

cari = input("\nCari buah apa? :")
if cari in stok_buah:
    print("Buah",cari,"tersedia")
    beli = input("Mau Beli? [y/n] :")
    if beli == "y":
        print(cari,"berhasil dibeli")
        stok_buah.discard(cari)
        print("Stok buah: ",stok_buah)
    elif beli == "n":
        print("Stok buah: ",stok_buah)
else:
    print("Buah yang dicari tidak ada")

