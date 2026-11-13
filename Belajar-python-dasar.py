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

