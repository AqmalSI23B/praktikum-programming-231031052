nama = 'Muhammad aqmal nurfauzi'
nim = '231031052'
meet = 'praktikum 4'
prodi = 'Sistem Informasi B'
email = 'aqmalnurfauzi@gmail.com'
tanggal = '11 oktober 2023'
sp = 40
print()
print(len(nama))

#print(len(nama))
print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp)+f'\r{meet}')
#print(prodi.rjust(sp))
print(email.rjust(sp)+f'\r{tanggal}')
print('-'*sp)

paragraf = '''Halo, selamat datang perkenalkan nama
saya{} dengan NIM {} dari prodi {}
ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

print('++++++++8--------')
#--------8++++++++
x = 3 #input
hasil = x<8
print(x,'hasiladalah',hasil)

print('++++++++8--------') 
#++++++++8--------
x = 9 #input
hasil = x<8
print(x,'hasiladalah',hasil)

print('--------4++++++8--------')
x = 9
#cek1 = x>4 true
cek1 = x>4
#cek = x<8 true
cek2 = x<8
#hasil = cek1 and cek2 -->true
hasil = cek1 and cek2
#cetak hasil
print(x,'hasilnya adalah',hasil)

print('--------4++++++8--------')
x = 2
#cek1 = x<4 true
cek1 = x<4
#cek = x>8 true
cek2 = x>8
#hasil = cek1 and cek2 -->true
hasil = cek1 or cek2
#cetak hasil
print(x,'hasilnya adalah',hasil)











































