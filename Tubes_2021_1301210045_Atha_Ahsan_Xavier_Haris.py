'''
Nama    : Atha Ahsan Xavier Haris
NIM     : 1301210045
Kelas   : IF-45-08
'''

'''
a. membuat dict rumah ganjil & rumah genap
'''
# membaca file teks
file_teks = open("file_teks_tubes.txt","r")
isi_file = file_teks.read()

# inisiasi dictionary rumah ganjil & rumah genap
rumah_ganjil = {}
rumah_genap = {}

# file teks menjadi list
list_isi_file = isi_file.split('\n')

# indeks pertama dalam list_isi_file atau baris pertama dalam file teks dijadikan list
baris1 = list_isi_file[0].split()

# setiap elemen didalam list baris1 dijadikan integer
for i in range(0, len(baris1)):
    baris1[i] = int(baris1[i])

# mengetahui posisi rumah anda berdasarkan indeks pertama dari list baris1 sekaligus menambahkannya kedalam dict rumah ganjil atau rumah genap
if baris1[0] % 2 == 0:
    rumah_genap[baris1[0]] = 'anda'
else:
    rumah_ganjil[baris1[0]] = 'anda'

# inisiasi patokan rumah awal berdasarkan indeks pertama dari list baris1
pov = baris1[0]

# mengetahui jumlah rumah didalam kompleks berdasarkan indeks ke-2 dari list baris1
jumlah_rumah = baris1[1]

# indeks ke-2 seterusnya di dalam list_isi_file dijadikan list, kemudian casting indeks pertama dari setiap list tersebut menjadi integer
for i in range(1,len(list_isi_file)):
    list_isi_file[i] = list_isi_file[i].split()
    for j in list_isi_file:
        list_isi_file[i][0] = int(list_isi_file[i][0])
  
# list indeks ke-2 seterusnya dari list_isi_file atau list dari baris ke-2 seterusnya dari file teks
tata_rumah = list_isi_file[1:]

# penambahan dict rumah ganjil dan rumah genap berdasarkan patokan rumah sebelumnya
for i in range(len(tata_rumah)):
    # penambahan dict jika nomor rumah patokan ganjil
    if pov % 2 != 0:
        if tata_rumah[i][2] == 'seberang' and tata_rumah[i][3] == 'kiri':
            rumah_genap[(pov - 2*tata_rumah[i][0]) + 1] = tata_rumah[i][9]
            pov = (pov - 2*tata_rumah[i][0]) + 1
        elif tata_rumah[i][2] == 'sebelah' and tata_rumah[i][3] == 'kiri':
            rumah_ganjil[pov - 2*tata_rumah[i][0]] = tata_rumah[i][9]
            pov = pov - 2*tata_rumah[i][0]
        elif tata_rumah[i][2] == 'seberang' and tata_rumah[i][3] == 'kanan':
            rumah_genap[(pov + 2*tata_rumah[i][0]) + 1] = tata_rumah[i][9]
            pov = (pov + 2*tata_rumah[i][0]) + 1
        elif tata_rumah[i][2] == 'sebelah' and tata_rumah[i][3] == 'kanan':
            rumah_ganjil[pov + 2*tata_rumah[i][0]] = tata_rumah[i][9]
            pov = pov + 2*tata_rumah[i][0]
    # penambahan dict jika nomor rumah patokan genap
    elif pov % 2 == 0:
        if tata_rumah[i][2] == 'seberang' and tata_rumah[i][3] == 'kiri':
            rumah_ganjil[(pov - 2*tata_rumah[i][0]) - 1] = tata_rumah[i][9]
            pov = (pov - 2*tata_rumah[i][0]) - 1
        elif tata_rumah[i][2] == 'sebelah' and tata_rumah[i][3] == 'kiri':
            rumah_genap[pov - 2*tata_rumah[i][0]] = tata_rumah[i][9]
            pov = pov - 2*tata_rumah[i][0]
        elif tata_rumah[i][2] == 'seberang' and tata_rumah[i][3] == 'kanan':
            rumah_ganjil[(pov + 2*tata_rumah[i][0]) - 1] = tata_rumah[i][9]
            pov = (pov + 2*tata_rumah[i][0]) - 1
        elif tata_rumah[i][2] == 'sebelah' and tata_rumah[i][3] == 'kanan':
            rumah_genap[pov + 2*tata_rumah[i][0]] = tata_rumah[i][9]
            pov = pov + 2*tata_rumah[i][0]

'''
b. membuat fungsi nomor_rumah
'''
def nomor_rumah(nama):
    dict_gabungan = rumah_ganjil | rumah_genap
    list_key = list(dict_gabungan.keys())
    list_val = list(dict_gabungan.values())
    if nama not in list_val:
        return 'tidak tahu'
    else:
        nomor = list_val.index(nama)
        return list_key[nomor]

'''
c. membuat fungsi penghuni_rumah
'''
def penghuni_rumah(nomor):
    dict_gabungan = rumah_ganjil | rumah_genap
    if nomor not in dict_gabungan:
        return 'tidak tahu'
    else:
        nama = dict_gabungan[nomor]
        return nama

# menutup file teks
file_teks.close()

'''
d. main program untuk menampilkan dict & memanggil fungsi
'''
# menampilkan dict rumah ganjil dan rumah genap
print("Dictionary untuk rumah ganjil                            :",rumah_ganjil)
print("Dictionary untuk rumah genap                             :",rumah_genap)
print("=============================================================================================")

# contoh pemanggilan fungsi tanpa input user
print("Contoh")
print("Nomor rumah dari rumah yang dihuni keluarga Joni adalah  :",nomor_rumah("Joni"))
print("Nomor rumah dari rumah yang dihuni keluarga Tono adalah  :",nomor_rumah("Tono"))
print("Nama penghuni rumah dari rumah bernomor 7 adalah         :",penghuni_rumah(7))
print("Nama penghuni rumah dari rumah bernomor 2 adalah         :",penghuni_rumah(2))
print("=============================================================================================")

# pemanggilan fungsi dengan menggunakan input user
x = input("Input nama orang dengan awalan kapital untuk mencari nomor rumah orang tersebut: ")
print("Nomor rumah dari rumah yang dihuni keluarga",x,"adalah:",nomor_rumah(x))
print("=============================================================================================")
y = int(input("Input nomor rumah untuk mencari nama penghuni dari rumah tersebut: "))
print("Nama penghuni rumah dari rumah bernomor",y,"adalah:",penghuni_rumah(y))