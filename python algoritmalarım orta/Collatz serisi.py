# Collatz serisi oluşturmak için kullanıcıdan bir tam sayı alın.Seriyi ve 
# serinin en büyük tam sayısını döndüren bir algoritma oluşturun.

#Collatz sanısının kuralları şudur:
#ifade olarak sayıya 'x' diyelim.
#Bu sayı çiftse 'x/2' ye dönüşür
#Bu sayı tekse '3x+1' e dönüşür
#Bu sanıya göre tüm sayılar,1'e kolayca indirilebilir.Bu,sayının büyüklüğüyle alakalı değildir.
# Örneğin:
#   "x=4" diyelim.O halde 4-2-1 olur.
# Örneğin:
#   "x=7" olsun. O halde 7-22-11-34-17-52-26-13-40-20-10-5-16-8-4-2-1  olur
#   Bu sayı kuramında 7'nin vardığı en büyük sayı 52'dir.

sayi=int(input("bir sayi giriniz:"))
list=[]
list.append(sayi)
while(sayi!=1):
    if(sayi%2==0):
        sayi=sayi/2
        list.append(sayi)
        continue
    if(sayi%2!=0):
        sayi=3*sayi+1
        list.append(sayi)
        continue

print(list)
print(max(list))
    




