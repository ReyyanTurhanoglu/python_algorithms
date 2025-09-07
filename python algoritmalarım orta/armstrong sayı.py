# ARMSTRONG NUMBER
# Armstrong Sayı Nedir ?
# N haneli bir sayının basamaklarının n'inci üstlerinin toplamı, sayının kendisine eşitse, böyle sayılara Armstrong sayı denir.
# Örneğin: 0,1,153,370,371,407 
number=input("lütfen bir sayi giriniz:")
uzunluk=len(number)
toplam=0
for i in number:
    toplam+=int(i)**uzunluk
if(int(number)==toplam):
    print(f"{number} bir armstrong sayidir")
else:
    print(f"{number} bir armstrong sayi değildir")