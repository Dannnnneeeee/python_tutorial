#variable
nama = 'dan' #string
umur = 18   #integer
tinggi = 169.5 #float

#Notasi scientific
speed_of_light = 3e8
very_small = 1e-6

#function print
print(speed_of_light)
print(very_small)
#f-string (formatted string literal)
#digunakan untuk menyisipkan langsung variable ke string
print(f'halo nama saya {nama}, berumur {umur} tahun, dan tinggi {tinggi} cm')

#tidak menggunakan f-string
print('halo nama saya '+nama+' berumur '+str(umur)+' tahun,dan memiliki tinggi '+str(tinggi)+' cm ')

#pengecekan type data
print(type(nama))
print(type(umur))
print(type(tinggi))

#multi-line menggunakan triple quotes (""" """)

#Boolean

is_married = False
is_student = True

#operator logika
print(is_married and is_student)

#multi assignment
x=y=z=0
name, age = "dan", 18

print(name)
print(age)

#menyisipkan variable pada print
panjang = 2
lebar = 2
luas = panjang * lebar

print('panjang luas adalah', luas)
