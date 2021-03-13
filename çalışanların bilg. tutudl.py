def main():
    calisan_sayisi=int(input("Kaç adet çalışan girilecek?"))
    calisan_dosyasi=open("calisanlar.txt","w")

    for sayac in range(1,calisan_sayisi+1):
        print("Veriliri giriniz çalışan#",sayac,sep="")
        isim=input('isim:   ')
        sicil=input('sicil: ')
        bolum=input("bolum: ")

        calisan_dosyasi.write(isim+'\n')
        calisan_dosyasi.write(sicil+'\n')
        calisan_dosyasi.write(bolum+'\n')
        print()
    calisan_dosyasi.close()
    print("veriler calisan_dosyasi kısmına yazıldı.")
main()    
