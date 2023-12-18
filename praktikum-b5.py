print('praktikum 5')
nama = 'Muhammad aqmal nurfauzi ' 
nim = '231031052 '
meet = 'praktikum 5 '
prodi = 'Sistem Informasi B '

print(f'{nama+nim+meet+prodi}')

nim = [2,3,1,0,3,1,0,5,2]
print(nim)
#akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir :',nim[len(nim)-1])
#akses indeks negatif
print('item indeks terakhir :',nim[-1])
print('item indeks terakhir :',nim[-len(nim)])
print('item indeks 3: [-6]',nim[-6])
print('item indeks 5: [-4]',nim[-4])
print('item indeks -7: [2]',nim[2])
print('item indeks 2: [-7]',nim[-7])
#akses indeks batas
print(f'item indeks 1,2,.....: {nim[1:]}')
print(f'item indeks 3,4,.....: {nim[3:]}')
print(f'item indeks 0,1,2,3..: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [:4]: {nim[:-5]}')
#pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
#nested list
kelas = [('kalkulus 1',2),
         ('agama 2',3)]
print(kelas)
kelas.append(('pancasila 3',2 ))
print(kelas)
kelas.append(('pemrograman 4',3 ))
kelas.append(('sainster 5',2 ))
print(kelas)
#tambahkan matkul 4 dan 5 dan sksnya

#mata kuliah 1:matkul1 dengan 2 sks
#mata kuliah 2:matkul2 dengan 3 sks
#mata kuliah 3:matkul1 dengan 2 sks
#mata kuliah 4:matkul1 dengan .. sks
#mata kuliah 5:matkul1 dengan .. sks

data = [('Frankel',2023,'aktif'),
        (76,98,89,97,99),
        (2,3,2,2,2),
        ('S1-Regulaer','Sistem informasi B','Ganjil')]


#Nama mahasiswa: aqmal 
#Inisial aqmal: a
#NIM aqmal: 201031052
#Program aqmal: S1-Regulaer Sistem informasi B
#Angkatan aqmal: Ganjil-2023
#Total sks aqmal adalah: 11
#Jumlah Nilai aqmal: 5
#Nilai tertinggi aqmal: 99
#Nilai terendah aqmal: 76
#Rata-rata Nilai aqmal: 92,25
































































































