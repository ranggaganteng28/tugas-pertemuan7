#herliyansyah
print("------TUGAS PRAKTIKUM 3------")
print("Program Mengitung Laba Dengan Modal 100.000.000")
print("")
print("Note")
print("Bulan Pertama dan ke 2 = 0%")
print("Pada Bulan ke 3 = 1%")
print("Pada Bulan Ke 5 = 5%")
print("Pada Bulan ke 8 = 2%")
print("")

#variable
a = 1000000000
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        print("Laba bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("Laba bulan ke-",x," : ",c)
    if(x>5 and x<=7):
        d = a*0.5
        print("Laba bulan ke-",x," : ",d)
    if(x==8):
        e = a*0.5
        print("Laba bulan ke-",x," : ",e)
#hasil dari total tersebut
total=b+b+c+c+d+d+e
print("\n Total : ",total)
