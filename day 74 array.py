print("menambah array satu dimensi")
# untuk membuat data kelompok yang dimana setiap anggotanya hanya berasal dari tipe yang sejenis,
# anda perlu menggunakan kelas array dalam modul array .
# namaArray=array.array("kodetipe"[nilaiinisal 1, nilaiinisaial2,....])
import array
A=array.array('i',[2,7,5,7,9,3,25])
print(A)
# kode i di gunakan untuk tipe int
import array
A=array.array('f',[2,7,5,7,9,3,25])
print(A)
#kode f digunakan untuk tipe float
print(A[0])
print(A[4])
# untuk mengetahiu data yang ada pada indeks kita dapat menggunakan kurung siku [] sama dengan menggunakan data list
B=array.array('i',[2,8,5,7,9,3,25])
print(B)
B.append(50)
print(B)
# append () untuk menambahkan elemen pada array
B.insert(4,65)
print(B)
# insert () untuk menyisipkan elemen pada arry dengan menentukan indeks yang kita mau
B.remove(7)
print(B)
# remove() untuk menghapus elemen pada array
B[3]=11
print(B)
x=B.pop()
print(B)
print(x)
# di gunakan untuk mengambil nilai elemen terakhir, kemudian menghapus elemen tersebut 