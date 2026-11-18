# Ini adalah komentar
print("Hello, Python!")  # Perintah untuk mencetak teks

# Ini adalah komentar satu baris

"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")

nama = input("Masukkan nama Anda: ")
print("Halo,", nama)

def main():
    print("Hello dari fungsi main!")

if __name__ == "__main__":
    main()

# tipe data dasar
umur = 25
print(type(umur))  # <class 'int'>

tinggi = 170.5
print(type(tinggi))  # <class 'float'>

nama = "MasAmba"
print(type(nama))  # <class 'str'>

is_active = True
print(type(is_active))  # <class 'bool'>

buah = ["apel", "jeruk", "mangga"]
print(type(buah))  # <class 'list'>

warna = ("merah", "hijau", "biru")
print(type(warna))  # <class 'tuple'>

mahasiswa = {"nama": "Ambasing", "umur": 21, "jurusan": "Informatika"}
print(type(mahasiswa))  # <class 'dict'>

angka = {1, 2, 3, 3, 4}
print(angka)  # {1, 2, 3, 4}
print(type(angka))  # <class 'set'>

x = 10       # int
y = float(x) # konversi ke float
z = str(x)   # konversi ke string

print(y, type(y))  # 10.0 <class 'float'>
print(z, type(z))  # "10" <class 'str'>


# bab 4 Variabel

nama = "MasAmba"
umur = 25
tinggi = 170.5
is_active = True

print(nama)      # MasAmba
print(umur)      # 25
print(tinggi)    # 170.5
print(is_active) # True

first_name = "MasAmba"
total_harga = 10000

#2nama = "Salah"     # ❌ diawali angka
#class = "Informatika" # ❌ keyword Python

a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

x = y = z = 100
print(x, y, z)  # 100 100 100

nama = "MasAmba"
umur = 25
tinggi = 170.5

print(type(nama))   # <class 'str'>
print(type(umur))   # <class 'int'>
print(type(tinggi)) # <class 'float'>

x = 10
print(x)  # 10

del x
# print(x)  # ❌ Error karena variable sudah dihapus

PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"

PI = 3.14  # ❌ Secara aturan Python boleh, tapi sebaiknya jangan dilakukan

# constants.py
PI = 3.14159
GRAVITY = 9.8
MAX_RETRY = 3


print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)

TAX_RATE = 0.1  # 10% pajak

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0

buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True
print("pisang" not in buah) # True

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (b menunjuk objek yang sama dengan a)
print(a is c)     # False (c objek berbeda walau isinya sama)
print(a == c)     # True (nilai isinya sama)

nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B

buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Output:
# apel
# jeruk
# mangga

count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

# Output:
# Hitung: 0
# Hitung: 1
# Hitung: 2
# Hitung: 3
# Hitung: 4

for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)

# Output:
# 1
# 2
# 4

def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()

def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Amba")
sapa_nama("SUki")

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)

def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi")  # Menggunakan parameter
sapa_orang()        # Menggunakan default

# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")

# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])   # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)

# Membuat tuple
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1])   # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning"  # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)

# Membuat set
angka = {1, 2, 3, 3, 4, 5}

print(angka)  # {1, 2, 3, 4, 5} (duplikat otomatis hilang)

# Menambah elemen
angka.add(6)

# Menghapus elemen
angka.remove(2)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)   # Union
print(ganjil & genap)   # Intersection
print(ganjil - genap)   # Difference

# Membuat dictionary sederhana
mahasiswa = {
    "nama": "TOTO",
    "umur": 18,
    "jurusan": "RPL"
}

print(mahasiswa)

print(mahasiswa["nama"])    # TOTO
print(mahasiswa.get("umur")) # 18

mahasiswa["angkatan"] = 2023   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

for key, value in mahasiswa.items():
    print(key, ":", value)

kampus = {
    "mahasiswa1": {"nama": "TOTO", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # TOTO

# Membuat class
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

# Membuat object dari class
mhs1 = Mahasiswa("Amba", "Informatika")
mhs2 = Mahasiswa("Sore", "Sistem Informasi")

# Memanggil method
mhs1.sapa()
mhs2.sapa()

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())

class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

akun = BankAccount(1000)
akun.setor(500)
print("Saldo:", akun.lihat_saldo())

class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # private attribute

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

# Child class
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Membuat objek dari class turunan
kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()

class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")
        
burung = Burung("Rio")
burung.suara()
burung.terbang()

class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Andi", "Informatika", 2025)
maba.info()

