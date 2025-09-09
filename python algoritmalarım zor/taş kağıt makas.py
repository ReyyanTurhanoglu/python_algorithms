import random
print("***TAŞ KAĞIT MAKAS OYUNUNA HOŞ GELDİNİZ***")
secenek=["taş","kağıt","makas"]
kişi,laptop=0,0
oyun=0
while True:
    bilgisayar=random.choice(secenek)
    oyuncu=input("seçiniz:")
    print("bilgisayar:",bilgisayar)
    if oyuncu=="taş" and bilgisayar=="taş"or oyuncu=="kağıt" and bilgisayar=="kağıt" or oyuncu=="makas" and bilgisayar=="makas":
        print("berabere")
    elif oyuncu=="taş" and bilgisayar=="makas" or oyuncu=="kağıt" and bilgisayar=="taş" or oyuncu=="makas" and bilgisayar=="kağıt":
        print("tebrikler kazandınız")
        kişi+=1
    else:
        print("maalesef bilgisayar kazandı")
        laptop+=1
    oyun+=1
    print(f"{oyun}.oyun SKOR\noyuncu:{kişi}-bilgisayar:{laptop}")
    istek=input("tekrar oynamak ister misiniz evet/hayır: ")
    if istek=="evet":
        continue
    else:
        break


