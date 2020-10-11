# Dalam sebuah kelompok mentoring Alpro terdapat 10 mahasiswa, 
# Shahnaz selaku asisten dalam kelompok tersebut ingin membuat sebuah program yang dapat 
# menyimpan nama-nama anggota kelompok mentoring 
# dalam sebuah struktur data list. Bantulah Shahnaz untuk membuat program tersebut!

print("\t PROGRAM DATA MAHASISWA MENTORING ALPRO")

nama_mahasiswa_alpro = []
for i in range(10):
    nama_mahasiswa_alpro.append(input("Masukkan Nama Mahasiswa ke-"+str(i+1)+" :"))

print("-"*50)
print("\nDaftar mahasiswa Alpro :",nama_mahasiswa_alpro)