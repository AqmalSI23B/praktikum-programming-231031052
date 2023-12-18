import os
os.system('cls')

print('BIODATA'.center(50))
print('\n')
biodata = {'namal' : 'Muhammad Aqmal Nurfauzi',
           'namap' : 'Aqmal',
           'nim' : 231031052,
           'kelas' : 'SI23-B',
           'prodi' : 'Sistem Informasi',
           'ttl' : 'Parepare, 4 mei 2005',
           'agama' : 'Islam',
           'alamat' : 'Jl. Callakara',
           'asalsklh' : 'UPT SMA Negeri 1 Parepare',
          }
print('Nama Lengkap         : ',biodata['namal'])
print('Nama Panggilan       : ',biodata['namap'])
print('NIM                  : ',biodata['nim'])
print('Kelas                : ',biodata['kelas'])
print('Program Studi        : ',biodata['prodi'])
print('Tempat Tanggal Lahir : ',biodata['ttl'])
print('Agama                : ',biodata['agama'])
print('Alamat               : ',biodata['alamat'])
print('Asal Sekolah         : ',biodata['asalsklh'])
print('\n')
print('Tipe data dari biodata adalah',type(biodata))
print('\n')
