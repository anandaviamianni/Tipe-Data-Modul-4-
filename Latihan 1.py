print("\t\tPROGRAM KONVERENSI HARI")
hari = ("Minggu","Senin","Selasa","Rabu","Kamis","Jumat","Sabtu")
urutan_hari = int(input("Hari ke? :"))

if urutan_hari >= 1 and urutan_hari <=12:
    print("Hari ke-",urutan_hari,"adalah hari:",hari[urutan_hari])
else:
    print("Gak ada")