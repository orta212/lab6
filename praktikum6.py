from tabulate import tabulate

print("Nama         :   Orta Yamaesa")
print("NIM          :   312210147")
print("Kelas        :   TI.22.B1")
print("Mata Kuliah  :   Bahasa Pemrograman \n")

# Buat dictionary yang memiliki value berupa list
data = {'nama' : [], 'nilai': [] }


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


def tambah():
    # buat inputan untuk mengisi nim
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


def ubah(nama):
    if nama in data['nama']:
        # buat dictionary kosong untuk menampilkan data yang cocok sesuai input nama
        dataMhs = {}
        index = data['nama'].index(nama)
        # lakukan pengisian data yang cocok ke dalam variabel dataMhs
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])

        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        # lakukan input data apa yang akan diubah
        pilihan = input("pilih field yang akan diubah : \n1.Nama\n2.Nilai\n")
        # lakukan pengecekan pada variabel pilihan yang dikonversi menjadi nilai integer
        match int(pilihan):
            case 1:
                print("data nama sebelumnya : " + dataMhs['nama'][0])
                nama = input("Masukkan nama Baru : ")
                while nama in data['nama']:
                    if nama == dataMhs['nama'][0]:
                        break
                    print("Mahasiswa dengan nama yang sama sudah ada")
                    nama = input("Masukkan nama Baru : ")
                data['nama'][index] = nama

            case 2:
                print("data nilai sebelumnya :" , dataMhs['nilai'][0])
                nilai = input("Masukkan nilai baru : ")
                data['nilai'][index] = nilai

        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))

    else:
        print("data nama tidak ditemukan!")

while True:
    print("[ (l)ihat , (t)ambah, (u)bah, (h)apus, (k)eluar ] \n")
    tanya = input("Masukkan Pilihan : ")
    match tanya:
        case "l":
            tampilkan()
        case "t":
            tambah()
        case "u":
            tampilkan()
            if len(data['nama']) > 0:
                nama = input("masukkan nama siswa yang akan diubah : ")
                ubah(nama)
        case "h":
            tampilkan()
            if len(data['nama']) > 0:
                nama = input("masukkan nama siswa yang akan dihapus : ")
                hapus(nama)
        case "k":
            print("anda sudah Keluar dari program")
            break
        case _:
            print("Tidak Sesuai Pilihan, Silahkan Pilih Kembali!!\n")
            continue
