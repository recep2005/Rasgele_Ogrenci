import random
from tkinter import *
import os

ogr=[]
klnogr=[]
secim=0
basım=10
modu=1

def ekle():
    dosya = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\sinif.txt",mode="r",encoding="utf-8")
    

    if ogr==[]:
        for i in dosya.readlines():
            ogr.append(i)
        
        yazi.config(text="Öğrenciler Eklendi!\n")
    else:       
        yazi.config(text="Hala Listede Kayıtlı Öğrenci Var!\n")
def mod():
    global modu,basım
    ogr=[]
    dosya = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\sinif.txt",mode="r",encoding="utf-8")
    for i in dosya.readlines():
        ogr.append(i)
    dosyailk = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\secim.txt",mode="r",encoding="utf-8")
    secim = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\secim.txt","w")
    secim.writelines(ogr)
    secim.close()

    

            

    modu = modu+1
    modu=modu%10
    if modu==0:
        modu=1
    print(modu)
    dugme2.config(text="Seçim Ayar="+str(modu))
    if modu==1:
        yazi.config(text="Hiç Bir Öğrenci\nListeden Düşmez!\n Ama Seçim Sıfırlandı!")
    else:
        yazi.config(text="Her "+str(modu)+" Seçimde\n Bir Öğrenci\nListeden Düşmez!\n Ama Seçim Sıfırlandı!")
    ayark = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\ayar.txt","w",encoding="utf-8")
    ayark.write(str(modu))   
    ayark.close()
    


def degistir():
    global basım,modu,secim
    print(os.path.dirname(os.path.realpath(__file__)))
    if ogr ==[]:
        yazi.config(text="Kayıtlı Öğrenci Kalmadı!\n Öğrenci Ekle Butonuna Basın!.")

    else:   
        rast=random.choice(ogr)
        
        
        basım=basım+1
        secim=basım%modu
        print (basım)
        print (modu)
        print (secim)
        
        if secim==0:
            print ("Öğrenci silinmedi")
            basim=4
            yazi.config(text="Seçilen Öğrenci\n"+rast+" \n"+"Öğrenci silinmedi")
            
        else:
            print ("Öğrenci silindi")
            ogr.remove(rast)
            yazi.config(text="Seçilen Öğrenci\n"+rast+"\n"+"Öğrenci silindi")
    secim = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\secim.txt","w")
    secim.writelines(ogr)
    secim.close()
        
dosyailk = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\secim.txt",mode="r")

for i in dosyailk.readlines():
    ogr.append(i)
dosyaayar = open(os.path.dirname(os.path.realpath(__file__))+"\\veri\\ayar.txt","r",encoding="utf-8")
ayar = dosyaayar.read(1)  #Sadece ilk 10 karakteri okur
modu=int(ayar)
pencere=Tk()

pencere.geometry("360x110")
baslik = pencere.title("Öğrenci Seçim Programı")
pencere.resizable(width=FALSE, height=FALSE)

if  len(ogr)==0:
    yazi=Label(pencere,relief=SOLID, text="Öğrenci isimleri\n buraya gelecek\nÖğrenci Ekle butonuna ardından \nÖğrenci Seç butonuna basınız.")
else:
    yazi=Label(pencere,relief=SOLID, text="Seçiminiz Kaldığı Yerden\n  Devam Edecek!.")
        
    



yazi.place(x=130, y=10, width = 220, heigh=90)


dugme=Button(pencere,relief=SOLID,text="Öğrenci Seç",command=degistir, width = 10 )
dugme.place(x=10, y=10)


dugme1=Button(pencere,relief=SOLID,text="Öğrenci Ekle",command=ekle,width = 10)
dugme1.place(x=10, y=40)


dugme2=Button(pencere,relief=SOLID,text="Seçim Ayar="+str(modu),command=mod, width = 10)
dugme2.place(x=10, y=70)

yazi2=Label(pencere,font=("",6,""), text="Recep Çakır")
yazi2.place(x=280, y=100, width = 80, heigh=10)





pencere.mainloop()

