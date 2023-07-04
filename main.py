import school
ögrenci1=school.Okul.Ogrenci("Kemal Faruk ","Talay",319,"11-B",100)
ögrenci2=school.Okul.Ogrenci("İclal ","Talay",275,"11-A",100)
ögretmen1=school.Okul.Ogretmen("Ali","Atay",2356)
okul=school.Okul("Atatürk Okulu")

while True:
    print("""
    {}'na Hoşgeldiniz!
    
    """.format(okul.isim))
    islem=input("Ögrenci İslemleri İcin '1' e Basin; Ögretmen İslemleri İcin '2' e Basin (Cikmak İcin '*' a  Basiniz) : ")
    if islem=="1":
        print("Ögrenci Sistemindesiniz!\n") 
        ogrenci_secimi=input(f"Hangi Ogrenci İcin İslem Yapmak İstiyorsunuz :\n{ögrenci1.isim + ögrenci1.soyisim} İcin 1'e,\n{ögrenci2.isim + ögrenci2.soyisim} İcin 2'e Basiniz :")
        if ogrenci_secimi=="1":
            aktif_ogrenci=ögrenci1
        elif ogrenci_secimi=="2":
            aktif_ogrenci=ögrenci2
        else:
            print("Gecersiz Ogrenci Secimi!!")
        
        islem2=input("Puani Gorüntülemek İcin '1'e Basiniz, Ogrenci Bilginizi Gorüntülemek İcin '2'e Basiniz :\n" )
        
        
        if islem2=="1":
            if aktif_ogrenci.disiplin_puani==None:
                pass
            else:
                aktif_ogrenci.puan_goruntule()
        elif islem2=="2":
            aktif_ogrenci.goruntule()
        else:
            print("Gecersiz İslem!")

    elif islem=="2":
        print("Ogretmen Sistemindesiniz! , Hosgeldiniz.")
        islem3=input("""
        
        --------------------------
        Yapabileceginiz İslemler:
        --------------------------
        -Disiplin İcin '1',
        -Ders Notu İcin '2',
        -Ogretmen Bilgileri icin '3' e Basiniz:
        
        """)
        if islem3=="1":
            sifre=int(input("Lütfen Ogretmen Sifrenizi Giriniz :"))
            if sifre==ögretmen1.sifre:
                ogrenci_secimi=input(f"Hangi Ogrenci İcin İslem Yapmak İstiyorsunuz :\n{ögrenci1.isim + ögrenci1.soyisim} İcin 1'e,\n{ögrenci2.isim + ögrenci2.soyisim} İcin 2'e Basiniz :")
                if ogrenci_secimi=="1":
                    aktif_ogrenci=ögrenci1
                    ögrenci1.disiplin()
                elif ogrenci_secimi=="2":
                    aktif_ogrenci=ögrenci2
                    ögrenci2.disiplin()
                else:
                    print("Gecersiz Ogrenci Secimi!!") 
            elif sifre !=ögretmen1.sifre:
                print("Yanlis Sifre Girdiniz!!")
        elif islem3=="2":
            sifre=int(input("Lütfen Ogretmen Sifrenizi Giriniz :"))
            if sifre==ögretmen1.sifre:
                ogrenci_secimi=input(f"Hangi Ogrenci İcin İslem Yapmak İstiyorsunuz :\n{ögrenci1.isim + ögrenci1.soyisim} İcin 1'e,\n{ögrenci2.isim + ögrenci2.soyisim} İcin 2'e Basiniz :")
                if ogrenci_secimi=="1":
                    
                    if ögrenci1.disiplin_puani==None:
                        pass
                    else:
                        ögrenci1.puan_degis()
                    
                elif ogrenci_secimi=="2":
                    
                    if ögrenci2.disiplin_puani==None:
                        pass
                    else:
                        ögrenci2.puan_degis()
                    
                else:
                    print("Gecersiz Ogrenci Secimi!!") 
                
            elif sifre !=ögretmen1.sifre:
                print("Yanlis Sifre Girdiniz!!")

        elif islem3=="3":
            ögretmen1.Ogretmen_bilgi()
    elif islem=="*":
        print("Sistem Kapatiliyor İyi Günler...")
        break


    


