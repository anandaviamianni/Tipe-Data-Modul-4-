list1 = ["apel","jeruk","nanas"]
print("Isi lis1 sebelum ditambah dengan metode append :", list1)
list1.append("durian")
print("Isi list1 setelah ditambah dengan metode append :",list1)
print("-+"*45,"\n")

list2 = ["salak","mangga","anggur"]
print("Isi list2 sebelum ditambah dengan metode insert :", list2)
list2.insert(2,"manggis")
print("Isi list2 setelah ditambah dengan metode insert :", list2)
print("+-"*45,"\n")

list3 = ["nangka", "pisang", "kelapa"]
print("Isi list3 sebelum ditambah dengan metode extend :", list3)
list3.extend(list2)
print("Menggabungkan isi list3 dengan list2 :",list3)

list4 = ["buah","sayur","bunga"]
