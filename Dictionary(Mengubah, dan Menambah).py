dict1 = {
    "nama":"Gani",
    "usia" : 35
}
print("Isi dict1 :")
print("Key nama :",dict1["nama"])
print("Key usia :",dict1["usia"])

#Mengupdate nilai
dict1["usia"] = 36
print("\nMengupdate usia :",
    "\nIsi key usia setelah diupdate :",dict1["usia"])

#Menambah anggota
dict1["alamat"] = "Medan"
print("\nMenambah anggota/key baru :",
    "\nIsi dict1 setelah ditambah anggota/key baru : ")
print(dict1)