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
