# Pertemuan 7
## Kondisi dan Perulangan
***

## Tugas Melengkapi Pertemuan 7
| Nama | kelas | Nim | Matkul |
| -- | --- | ---- | ----------- |
| Rangga Saputra | TI.20.A2 | 312010266 | Bahasa Pemrograman |
## Daftar Isi
| No | ISI | Link | Source Code |
| -- | --- | ---- | ----------- |
| 1. | Latihan 1 | [penjelasan](#Latihan-1) | [codenye](#latihan1.py) |
| 2. | Latihan 2 | [penjelasan](#Latihan-2) | [codenye](#latihan2.py) |
| 1. | praktikum 3 | [penjelasan](#program-1) | [codenye](#program1.py) |

### Latihan 1 
* Saya diberikan tugas untuk membuat program perulangan bersarang/bertingkat (nested for) yang menghasilkan output berikut

![output 1](isi%20fhoto/tugas%201.png)

Maka program yang saya buat sebagai berikut atau bisa dilihat di [Source Code](latihan1.py)

```python
# helloow

baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
```

Penjelasan

1. Pendeklarasian variable
```python
baris = 10
kolom = baris
```

2. Untuk perulangan baris dan kolom menggunakan `nested for`
```python
for bar in range(baris):
    for col in range(kolom):
        tab = bar+col        
```
3. Untuk menampikan hasil dari perulangan
     * Agar terlihat rapih menggunakan `format string` rata ke kanan sebanyak 5 karakter
     * Agar tidak membuat baris baru menggunakan `end=''` (baris)
     * Penggunaan `print()` untuk membuat baris baru (kolom)
```python
  print("{0:>5}".format(tab), end='')
print()    
```

Maka program yang di hasil seperti berikut

![hasil ke1](isi%20fhoto/hasil%201.png)


### Latihan 2

* Saya diberikan tugas untuk membuat program :
     * Tampilkan n bilangan acak yang lebih kecil dari 0.5
     * Nilai n diisi pada saat runtime
     
Seperti pada gambar berikut

![output 2](isi%20fhoto/tugas%202.png)

Maka program yang saya buat sebagai berikut atau bisa dilihat di [hasil Code](latihan2.py)

```python
import random
print(39*"=")
print("Bilangan acak yang lebih kecil dari 0,5")
print(39*"=")
jum = int( input("Masukan nilai n : "))
i = 0
for i in range(jum):
    i += 1
    angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)
 
 ```

Penjelasan

1. Mengimport module `random` untuk membuat bilangan acak
```python
import random
```

2. Untuk menentukan jumlah input yang diinginkan dan dikonversi ke dalam bilangan bulat (integer) yang dimasukan ke variable `jum`
```python
jum = int( input("Masukan nilai n : "))
```

3. Untuk pengulangan range yang diinputkan oleh variable `jum`
```python
for i in range(jum):
```

4. Untuk menampilkan urutan data sesuai jumlah inputan dengan hasil di bawah 0.5
```python
angkaDec = random.uniform(0, 0.5)
    print("Data ke", i, " = ", angkaDec)
```

Maka program yang dihasilkan akan seperti berikut

![tampil 2](isi%20fhoto/hasil%202.png)


### program 1

soal hasil praktikum.....

![GitHub Logo](isi%20fhoto/tugas%203.png) <h2>

  *Membuat program sederhana dengan perulangan :

 Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya 
dengan modal awal 100 juta,

- Pada bulan pertama dan kedua belum mendapatkan laba.

- Pada bulan ketiga baru mulia mendapatkan laba sebesar 1%

- Pada bulan ke lima pendapatan meningkat 5%

- Pada bulan ke delapan mengalami penurunan keuntungan sebesar 2%, 
sehingga laba menjadi 3%.

- Hitung total keuntungan selama 8 bulan berjalan usahanya.

 *ALGORITMA menghitung keuntungan selama 8 bulan berjalannya usaha.

1. Mulai

2. Mencetak latihan1

3. Mencetak "Program menghitung laba dengan modal awal 100 juta"

4. Membuat Note

5. Mencetak Bulan pertama dan kedua = 0%

6. Mencetak bulan ke 3 = 1%

7. Mencetak bulan ke 5 = 5%

8. Mencetak bulan ke 8 = 2%

9. integer a = 100.000.000( modal awal)

10. Menggunakan fungsi looping for pada nilai x 1-9 untuk menampilkan 
bulan 1 sampai bulan 8.

11. Menggunakan fungsi if, untuk menghitung laba bulan 1 sampai 8

12. bulan pertama dan kedua laba adalah 0

13. bulan ke 3 dan ke 4 mendapat laba 1% sehingga modal di kali 1% = 
keuntungan

14. bulan ke 5 mendapatkan laba 5%, sehingga modal dikali 5% = 
keuntungan

15. Bulan ke 8 mmendapatkan laba 2% sehingga keuntungan menurun dari 
bulan sebelumnya, modal dikali 2% = keuntungan.

16. Menghitung jumlah total laba dengan menjumlah keuntungan dari bulan 
ke 1 sampai bulan 8, hasilnya adalah total keuntungan yang didapat.

17. Selesai

Maka program yang saya buat sebagai berikut atau bisa dilihat di [hasil Code](program1.py)

## Syntax program 1 sebagai berikut :
```python 
#Rangga

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
```

## Hasil output program3 ketika run time adalah sebagai berikut :

# ![GitHub Logo](isi%20fhoto/hasil%203.png) <h2>


# keep spirit.....



