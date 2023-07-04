import random

class Okul():
    def __init__(self,isim):
        self.isim=isim
    class Ogrenci():
        def __init__(self,isim,soyisim,no,sinif,disiplin_puani,ders={"Türkçe":0,"Matematik":0}):
            self.isim=isim
            self.soyisim=soyisim
            self.no=no
            self.sinif=sinif
            self.disiplin_puani=disiplin_puani
            self.ders=ders
        def disiplin(self):
            disiplin=input("Ögrenci disipline gitti mi?(Evet ya da Hayir):")

            if(disiplin=="Evet"):
                self.disiplin_puani -=10
                if (self.disiplin_puani<=0):
                    print("Ögrenci Kaydi Silindi!")
                    self.isim=None
                    self.soyisim=None
                    self.no=None
                    self.sinif=None
                    self.disiplin_puani=None
                else:
                    print("Ögrencimizin Disiplin Puani 10 Puan Düsürülmüstür! Yeni Puani:",self.disiplin_puani)

            elif(disiplin !="Evet" or disiplin=="Hayir"):
                print("Meşgul Etmeyiniz!")
                
        
        def goruntule(self):
            print("""
            -------------------
            Ögrenci Bilgileri:
            -------------------
            
            İsim:{}
            Soyisim:{}
            Numara:{}
            Sinifi:{}
            Disiplin Puani:{}
            
            
            
            """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplin_puani))
        
        def puan_degis(self):
            girdi=input("Lütfen Puanini Degiştirmek İstediginiz Dersi Giriniz ('Türkçe' ya da 'Matematik'):")
            if girdi=="Türkçe":
                self.ders["Türkçe"]=int(input("Lütfen Puani Giriniz:"))
                if 0<=self.ders["Türkçe"]<=100:
                    print("Basarili Bir Sekilde Puan Degistirildi.Türkçe Puaniniz:",self.ders["Türkçe"])
                else:
                    print("Puan Degistirilemedi!")
                    self.ders["Türkçe"]=0
            elif girdi=="Matematik":
                self.ders["Matematik"]=int(input("Lütfen Puani Giriniz:"))
                if 0<=self.ders["Matematik"]<=100:
                    print("Basarili Bir Sekilde Puan Degistirildi.Matematik Puaniniz:",self.ders["Matematik"])
                else:
                    print("Puan Degistirilemedi!")
                    self.ders["Matematik"]=0
            
            else:
                print("Boyle Bir Ders Yok!")


        def puan_goruntule(self):
            print("""
            ----------------
            {} {}
            ----------------
            Turkce Notunuz:{}
            Matematik Notunuz:{}
            
            """.format(self.isim ,self.soyisim,self.ders["Türkçe"],self.ders["Matematik"]))
        
        def hoca_yakalama(self):
            sayi=random.randint(1,2)
            if sayi==1:
                print("Hocaya Yakalandik!")
                self.disiplin_puani -=2
            elif sayi==2:
                print("Yanlis Alarm!")

    class Ogretmen():
        def __init__(self,isim,soyisim,sifre=12345):
            self.isim=isim
            self.soyisim=soyisim
            self.sifre=sifre
        def Ogretmen_bilgi(self):
            print("""
            
            Ogretmen Bilgileri:
        -------------------------------
            
            İsim:{}
            Soyisim:{}
        
        -------------------------------
        """.format(self.isim,self.soyisim))
            

           