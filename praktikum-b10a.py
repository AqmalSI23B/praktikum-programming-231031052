import os
def judul():
    os.system('clear')
    print('program menghitung Volume dan Luas Permukaan'.center(45))
    print('bangun Ruang Balok'.center(45))
    print()

def inputan():
    p = float(input('Masukan Panjang :'))
    l = float(input('Masukan Lebar :'))
    t = float(input('Masukkan Tinggi :'))
    return p,l,t

def hitung(p,l,t):
    vol = p*l*t
    luas_surf = 2*(p*l + p*t + l*t) 
    luas_non_tutup = luas_surf - p*l
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f'Nilai {pesan} : {nilai}')

def pilihan():
    pilih = input('Apakah lanjutan [y/n]')
    if pilih =='y':
        a = True
    else:
        a = False
        print('Terimakasih!')
    return a 

def main():
    judul()                                     # judul
    p,l,t = inputan()                           # inputan
    vol,luas_surf,luas_non_tutup = hitung(p,l,t)# hitung
    # tampilan
    tampilan('Volume',vol)
    tampilan('Luas permukaan',luas_surf)
    tampilan('Luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()                               # pilihan
    return a

a = True
while a:
    a = main()
