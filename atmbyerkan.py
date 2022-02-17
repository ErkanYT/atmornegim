print("***************************\nAtm Programına Hoşgeldiniz\n***************************")

print("Bakiye Sorgulama = 1\nPara Yatırma = 2\nPara Çekme = 3\nProgramdan Çıkış Yap = 4\n***************************")


bakiye = 500 #kendi bakiyem

sayi = int(input("İşlem Sayısı Seçiniz: "))  # karşıdakine sayıyı sectiriyorum

if sayi == 1:
    print("Bakiyeniz: {}".format(bakiye))

elif sayi == 2:
    addmoney = int(input("Yatırmak İstediğiniz Tutar: "))
    bakiye += addmoney
    print("İşlem Başarılı... Bakiyeniz: {}".format(bakiye))

elif sayi == 3:
    remoney = int(input("Çekmek İstediğiniz Tutar: "))
    bakiye -= remoney
    print("İşlem Başarılı... Bakiyeniz: {}".format(bakiye))

elif sayi == 4:
    print("Yine Bekleriz")

else:
    print("Doğru İşlemler Girin")


