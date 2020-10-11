pangkat = {1:1, 2:4, 3:9, 4:16, 5:25, "6":36 }
print("Isi pangkat :",pangkat)
# Menghapus anggota tertentu
print("\nenghapus key 3 dengan pop() dan mengembalikan valuenya :", pangkat.pop(3))

# Menghapus anggota secara acak
print("\nMenghapus anggota secara acak dengan popitem() :",pangkat.popitem())
print("Isi pangkat setelah dihapus secara acak :",pangkat)

#Menghapus semua anggota
pangkat.clear()
print("\nMenghapus semua anggota pangkat dengan clear :")
print("\nIsi pangkat setelah dihapus dengan clear :",pangkat)