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
```python
def tambah():
    # buat inputan untuk mengisi nama
    nama = input("Masukkan Nama : ")
    while len(nama) < 3:
        nama = input("Masukkan Nama : ")
    
    # jika nim yang di input tersedia pada variabel data, cetak pesan lalu lakukan input ulang
    while nama in data['nama']:
        print("Mahasiswa dengan nama yang sama sudah ada")
        nama = input("Masukkan Nama : ")
    
    nilai = input("masukkan nilai : ")
    while not nilai.isnumeric():
        nilai = input("masukkan nilai : ")
    
    data['nama'].append(nama)
    data['nilai'].append(int(nilai))
    print("Data Berhasil Ditambah!!")
```
keterangan : 
* lakukan input nama
* lakukan pengecekan terhadap inputan nama, selama kurang dari 3 karakter masukkan ulang nama
* lakukan pengecekan terhadap inputan nama, selama ada nama yang sama pada data, maka masukkan nama secara berulang
* lakukan input nilai
* selama variabel nilai bukan angka, maka ulamgi hingga user memasukkan angka
* masukkan data nama dan nilai yang baru ke dalam data menggunakan fungsi append()
* kemudian cetak pesan berhasil menambah data

### buat fungsi hapus(nama) untuk menghapus data
![def hapus](https://user-images.githubusercontent.com/47426095/205586909-b051b1c1-2836-4c66-8082-baca2c5636d2.PNG) <br>
``` python
def hapus(nama):
    if nama in data['nama']:
        # buat dictionary kosong untuk menampilkan data yang cocok sesuai input NIM
        dataMhs = {}
        index = data['nama'].index(nama)

        # lakukan pengisian data yang cocok ke dalam variabel dataMhs
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        # lakukan konfirmasi penghapusan
        confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

        # jika input selain y atau t lakukan konfirmasi berulang
        while (confirm not in ['y', 't']):
            print("input salah")
            confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

        # jika konfirmasi selesai dilakukan, maka hapus data mahasiswa pada variabel data
        if confirm == "y":
            for key in data.keys():
                data[key].pop(index)
            print("Data Berhasil Dihapus!!\n")

    else:
        print("data nama tidak ditemukan!!")
```
Keterangan : 
* lakukan input nama
* jika tidak ada data yang sesuai, taampilkan pesan "data nama tidak sesuai"
* lakukan pengecekan terhadap inputan nama, selama ada nama yang sama pada data, maka cetak pesan bahwa data sudah ada kemudian masukkan nama secara berulang
* buat dictionary untuk menampung nama mahasiswa berdasarkan index, kemudian tampilkan data lengkap mahasiswa terpilih
* lakukan konfirmasi penghapusan data
* jika input selain y atau t lakukan konfirmasi berulang
* jika input y maka hapus dengan fungsi pop(index)
* kemudian cetak pesan berhasil menghapus data
