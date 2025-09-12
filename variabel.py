#variable
nama = 'dan' #string
umur = 18   #integer
tinggi = 169.5 #float

#function print
#f-string (formatted string literal)
#digunakan untuk menyisipkan langsung variable ke string
print(f'halo nama saya {nama}, berumur {umur} tahun, dan tinggi {tinggi} cm')

#tidak menggunakan f-string
print('halo nama saya '+nama+' berumur '+str(umur)+' tahun,dan memiliki tinggi '+str(tinggi)+' cm ')

#pengecekan type data
print(type(nama))
print(type(umur))
print(type(tinggi))
