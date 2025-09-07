# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.Bölenlerinin toplamı kendisine eşit olan sayılara "mükemmel sayı" denir.Örnek:6=3+2+1
sayi=int(input("Bir sayi giriniz:"))
toplam=0
for i in range (1,sayi):
    if(sayi%i==0):
        toplam+=i
if(toplam==sayi):
    print("sayiniz mükemmel sayi")
else:
    print("sayiniz mükemmel sayi degil")

