# Buatlah sebuah program yang dapat menampung data mahasiswa berdasarkan NIM yang didalamnya terdapat nama, 
# kelas, dan nilai Perilaku Organisasi. Tetapi dari data mahasiswa tersebut Amel belum memiliki nilai Perilaku Organisasi. 
# Tambahlah nilai Perilaku Organisasi serta ubahlah nilai Perilaku Organisasi milik Farid dari 75,70 menjadi 81,97

("\t\t PROGRAM DATA MAHASISWA\n")

data_mahasiswa = {
    "1202190008" :{
        "Nama": "Ananda",
        "Kelas": "SI-43-02",
        "Nilai_PO" : 80.85
    },
    "120218008" : {
        "Nama" : "Viamianni",
        "Kelas" : "SI-43-01",
    }
}

print("Data sebelum diubah")
print("-"*15)
for key,value in data_mahasiswa.items():
    print("NIM :",key)
    for key2 in value:
        print(key2, ":",value[key2])
    print()

data_mahasiswa["1202190008"]["Nilai_PO"] = 91.21
data_mahasiswa["120218008"]["Nilai_PO"] = 81.97

print("Data setelah diubah")
print("-"*15)
for key,value in data_mahasiswa.items():
    print("NIM :",key)
    for key2 in value:
        print(key2, ":",value[key2])
    print()

data_mahasiswa.clear()
print("\nMenghapus semua anggota  dengan clear :")
print("\nIsi data setelah dihapus dengan clear :",data_mahasiswa)