Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Nama: Nurfadhilah Aco
#NIM: D0221117
# Kelas: Informatika H

import  math  #utk mendapat nilai pi, digunakan dalam menghitung luas/volume tabung

# kelas orang tua
kelas  BangunRuang :
    def  luas ( self ):
        lulus

    def  volume ( mandiri ):
        lulus

    def  printLuas ( self ):
        print ( "Luas:" , self.luas ( ) )

    def  printVolume ( self ):
        print ( "Volume:" , self .volume ( ))

kelas  Balok ( BangunRuang ):
    def  __init__ ( mandiri ):
        diri . panjang  =  0
        diri . lebar  =  0
        diri . tinggi  =  0

    def  luas ( self ):
        l  =  2  * ( self .panjang  *  self .lebar  + self .lebar * self .tinggi + self .panjang * self .tinggi ) _ _  _ _ _ _      
        kembali  l

    def  volume ( mandiri ):
        v  =  diri sendiri . panjang  *  diri . lebar  *  diri . tinggi
        kembali  v

kelas  Tabung ( Bangun Ruang ):
    def  __init__ ( mandiri ):
        diri . jari_jari  =  0
        diri . tinggi  =  0
    
    def  luas ( self ):
        l  =  2  *  matematika . pi  *  diri sendiri . jari_jari  * ( self . jari_jari  +  self . tinggi )
         putaran kembali ( l , 2 )
 
    def  volume ( mandiri ):
        v  =  matematika . pi  * ( self.jari_jari ** 2 ) * self . _ _ tinggi   
         putaran kembali ( v , 2 )
    

kelas  Kubus ( Bangun Ruang ):
    def  __init__ ( mandiri ):
        diri . sisi  =  0

    def  luas ( self ):
        l  =  6  * ( self .sisi ** 2 ) _
        kembali  l

    def  volume ( mandiri ):
        v  =  diri sendiri . sisi ** 3
        kembali  v

def  ulang ():
    print ( "Ingin menghitung lagi? (y/n)" )
    inp  =  masukan ( "=> " ). lebih rendah ()
    kembalikan  True  jika  inp  ==  "y"  else  False

kelas #panggil
balok  =  Balok ()
tabung  =  Tabung ()
kubus  =  kubus ()

sementara  Benar :
    print ( """ \n Pilih Bangun Ruang
1. Balok
2. Tabung
3. Kubu
4. Berhenti""" )
    pilihan  =  masukan ( "=> " )

    jika  pilihan  ==  "1" :
        sementara  Benar :
            print ( """ \n 1. Luas
2. Volume
3.Keluar""" )
            pilihan1  =  masukan ( "=> " )
            
            jika  pilihan1  ==  "1" :
                sementara  Benar :
                    balok . panjang  =  float ( input ( "Masukkan Panjang: " ))
                    balok . lebar  =  float ( input ( "Masukkan Lebar: " ))
                    balok . tinggi  =  float ( input ( "Masukkan Tinggi: " ))

                    cetak ()
                    balok . cetakLuas ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan1  ==  "2" :
                sementara  Benar :
                    balok . panjang  =  float ( input ( "Masukkan Panjang: " ))
                    balok . lebar  =  float ( input ( "Masukkan Lebar: " ))
                    balok . tinggi  =  float ( input ( "Masukkan Tinggi: " ))

                    cetak ()
                    balok . volume cetak ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan1  ==  "3" :
                merusak
            lain :
                print ( "Masukkan pilihan yang Benar!" )
    elif  pilihan  ==  "2" :
         sementara  Benar :
            print ( """ \n 1. Luas
2. Volume
3.Keluar""" )
            pilihan2  =  masukan ( "=> " )
            
            jika  pilihan2  ==  "1" :
                sementara  Benar :
                    tabung . jari_jari  =  float ( input ( "Masukkan Jari-jari: " ))
                    tabung . tinggi  =  float ( input ( "Masukkan Tinggi: " ))

                    cetak ()
                    tabung . cetakLuas ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan2  ==  "2" :
                sementara  Benar :
                    tabung . jari_jari  =  float ( input ( "Masukkan Jari-jari: " ))
                    tabung . tinggi  =  float ( input ( "Masukkan Tinggi: " ))

                    cetak ()
                    tabung . volume cetak ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan2  ==  "3" :
                merusak
            lain :
                print ( "Masukkan Pilihan yang Benar!" )
    elif  pilihan  ==  "3" :
         sementara  Benar :
            print ( """ \n 1. Luas
2. Volume
3.Keluar""" )
            pilihan3  =  masukan ( "=> " )
            
            jika  pilihan3  ==  "1" :
                sementara  Benar :
                    kubus . sisi  =  float ( input ( "Masukkan Sisi: " ))

                    cetak ()
                    kubus . cetakLuas ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan3  ==  "2" :
                sementara  Benar :
                    kubus . sisi  =  float ( input ( "Masukkan Sisi: " ))
                    
                    cetak ()
                    kubus . volume cetak ()

                    jika  ulang () !=  True :
                        merusak
            elif  pilihan3  ==  "3" :
                merusak
            lain :
                print ( "Masukkan Pilihan yang Benar!" )
    elif  pilihan  ==  "4" :
        merusak
    lain :
        print ( "Masukkan Pilihan yang Benar!" )

print ( "Program berhenti. Selamat tinggal." )