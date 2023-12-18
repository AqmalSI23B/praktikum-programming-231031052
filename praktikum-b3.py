print('praktikum-3 \n')
print('NAMA    : Muhammad Aqmal Nurfauzi')
print('NIM     : 231031052')
print('Prodi   : Sistem Informasi B')

#######################
a=True
b=False

print('\n============NAND============')
hasil=not (a and a)
print(a,'nand',a,'adalah=',hasil)
hasil=not (a and b)
print(a,'nand',b,'adalah=',hasil)
hasil=not (b and a)
print(b,'nand',a,'adalah=',hasil)
hasil=not (b and b)
print(b,'nand',b,'adalah=',hasil)

print('\n============NOR============')
hasil=not (a or a)
print(a,'nor',a,'adalah=',hasil)
hasil=not (a or b)
print(a,'nor',b,'adalah=',hasil)
hasil=not (b or a)
print(b,'nor',a,'adalah=',hasil)
hasil=not (b or b)
print(b,'nor',b,'adalah=',hasil)

print('\n============NXOR============')
hasil=not (a ^ a)
print(a,'nxor',a,'adalah=',hasil)
hasil=not (a ^ b)
print(a,'nxor',b,'adalah=',hasil)
hasil=not (b ^ a)
print(b,'nxor',a,'adalah=',hasil)
hasil=not (b ^ b)
print(b,'nxor',b,'adalah=',hasil)

#INI OPERATOR MEMBERSHIP
print('\n============IN============')
nama = 'Muhammad Aqmal Nurfauzi'

test= 'ma' #ISI DENGAN DUA HURUF YANG ADA DI NAMA
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)

test= 'am' #ISI DENGAN DUA HURUF YANG ADA DI NAMA
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'ada di',nama,'adalah=',cek)

cek = test2 in nama
print(test2,'ada di',nama,'adalah=',cek)

cek = test3 in nama
print(test3,'ada di',nama,'adalah=',cek)

cek = test4 in nama
print(test4,'ada di',nama,'adalah=',cek)

cek = test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

#TUGAS lanjutkan kode
#dengan cara yang sama buat operator not in

#INI Operator BITWISE
print('\n')
a = 4 #Tanggal lahir
b = 5 #Bulan lahir
a +=60
b +=80
print('========AND========')
print('nilai',a,'biner adalah     =',format(a,'09b'))
print('nilai',b,'biner adalah     =',format(b,'09b'))
print('______________________________________AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah= ',format(c,'09b'))

#Tugas buat untuk OR
print('========OR========')
print('nilai',a,'biner adalah     =',format(a,'09b'))
print('nilai',b,'biner adalah     =',format(b,'09b'))
print('______________________________________OR')
c = a & b
print('Nilai',a,'&',b,'biner adalah= ',format(c,'09b'))

#Tugas buat untuk XOR
print('========XOR========')
print('nilai',a,'biner adalah     =',format(a,'09b'))
print('nilai',b,'biner adalah     =',format(b,'09b'))
print('______________________________________XOR')
c = a & b
print('Nilai',a,'&',b,'biner adalah= ',format(c,'09b'))


print('\n========NOT========')
c = ~a
print('nilai',a,'biner adalah    =',format(a,'09b'))
print('Nilai not',a,'biner adalah=',format(c,'09b'))
#Tugas lanjutkan untuk not b
print('\n========NOT========')
c = ~b
print('nilai',b,'biner adalah    =',format(b,'09b'))
print('Nilai not',b,'biner adalah=',format(c,'09b'))

print('\n========Left Shift========')
c = a<<2
print('nilai',a,'biner adalah    =',format(a,'09b'))
print('Nilai',a,'<<2biner adalah=',format(c,'09b'))
c = b<<2
print('nilai',b,'biner adalah    =',format(a,'09b'))
print('Nilai',b,'<<2biner adalah=',format(c,'09b'))

print('\n========Right Shift========')
c = a>>2
print('nilai',a,'biner adalah    =',format(a,'09b'))
print('Nilai',a,'>>2biner adalah=',format(c,'09b'))
c = b>>2
print('nilai',b,'biner adalah    =',format(a,'09b'))
print('Nilai',b,'>>2biner adalah=',format(c,'09b'))

print('========NOT AND========')
#Tugas buat untuk NOT AND
print('========NOT OR========')
#Tugas buat untuk NOT OR
print('========NOT XOR========')
#Tugas buat untuk NOT XOR
print('========NOT <<2========')
#Tugas buat untuk c=~(a<<2)
#Tugas buat untuk c=~(b<<2)
print('========NOT >>2========')
#Tugas buat untuk c=~(a>>2)
#Tugas buat untuk c=~(b>>2)

