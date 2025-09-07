# Bir daire ve dairenin içinde ve dışında iki kare hayal edin.
# Bir tam sayı (dairenin yarıçapı) alan ve iki karenin alanlarının farkını döndüren bir program oluşturun
from PIL import Image
#Image.open("C:/Users/lenovo/Desktop/dairekare.png").show()
Image.open("dairekare.png").show()
yaricap=int(input("dairenin yaricap degerini girin:"))
kucuk_kenar=(2*yaricap)/(2**(1/2))
kucuk_kare=kucuk_kenar*kucuk_kenar
buyuk_kenar=2*yaricap
buyuk_kare=buyuk_kenar*buyuk_kenar
print(f"KUCUK KARENIN ALANI->>>{kucuk_kare}")
print(f"BUYUK KARENIN ALANI->>>{buyuk_kare}")
fark=buyuk_kare-kucuk_kare
print(f"karelerin alanlari farki:{fark}")

