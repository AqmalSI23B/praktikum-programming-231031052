#Praktikum 8

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login')
        a = False
    else:
        if i== limit:
            a = False
            print('Anda Kehabisan Kesempatan')
        else:
            print('Password Salah!')
            print(f'Kesempatan anda tersisa {limit-i}kali!',)
            
           
komputer memilih angka [1...5]
user tebak angka
jika salah 1: Anda salah, anda memiliki 2 kesempatan lagi
jika salah 2: Anda salah, anda memiliki 1 kesempatan lagi
jika salah 3: Anda salah,belum berhasil
              Angka yang dicari adalah x

jika benar: anda benar angka yang ditebak adalah x (program selesai)
