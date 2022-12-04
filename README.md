# lab6


# Praktikum 6
### lakukan import dan buat variabel berupa dictionary untuk menampung data utama
![awal dan penyiapan data](https://user-images.githubusercontent.com/47426095/204299764-1b064500-6531-4348-97b9-9dd7ae76a713.PNG) <br>
``` python
from tabulate import tabulate

print("Nama         :   Orta Yamaesa")
print("NIM          :   312210147")
print("Kelas        :   TI.22.B1")
print("Mata Kuliah  :   Bahasa Pemrograman \n")

# Buat dictionary yang memiliki value berupa list
data = {'nama' : [], 'nilai': [] }
```
keterangan : 
* modul tabulate kita gunakan untuk membuat tabel pada saat menampilkan data
* variabel data digunakan sebagai penampung seluruh data
* variabel data berupa dictionary yang memiliki key nama dan nilai, tiap key memiliki value berupa list

### buat fungsi tampilkan() untuk menampilkan semua data
![def tampilkan](https://user-images.githubusercontent.com/47426095/204537780-5b7a9f2c-4f92-4428-89ad-39c717823e56.PNG) <br>
``` python
def tampilkan():
    # variabel i untuk membuat penomoran data ketika dibuat tabel
    i = range(1, len(data['nama'])+1)
    # membuat list header kolom yang akan ditampilkan
    headers = ["No", "Nama", "Nilai"]

    # data dapat ditampilkan jika variabel data terisi minimal satu data
    if len(data['nama']) > 0:
        print(tabulate(data, headers, showindex=i,tablefmt="rounded_outline"))

    # jika tidak ada data, maka tampilkan pesan
    else:
        print("\nTidak Ada Data \n")
```
keterangan : 
* variabel i digunakan untuk membuat penomoran angka pada saat menampilkan data (dimulai dari 1)
* kita gunakan key 'nama' sebagai parameter pengecekan isi data
* variabel headers digunakan untuk menampung urutan header pada tabel yang akan menampilkan data
* jika ada data, maka dicetak menggunakan tabulate, jika tidak ada, tampilkan pesan

### buat fungsi tambah() untuk menambahkan data
![def tambah](https://user-images.githubusercontent.com/47426095/205480250-66b227b9-7883-40ab-bec4-615bf969050a.PNG) <br>
keterangan : 
* 
