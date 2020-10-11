daftar_lab = {
    "DASPRO" :{
        "praktikum": "ALgoritma dan Pemrograman",
        "semester": 2,
    },
    "ERP" : {
        "praktikum" : "SAP 01 Fundamental",
        "semester" : 1,
    }
}

for key,value in daftar_lab.items():
    print("Nama lab :",key)
    for key2 in value:
        print(key2, ":",value[key2])
    print()
