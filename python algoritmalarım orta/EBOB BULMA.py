#İki sayının ebobunu bulma

sayi1=int(input("ilk sayi:"))
sayi2=int(input("ikinci sayi:"))
if(sayi1<sayi2):
    for i in range(1,sayi1+1):
        if(sayi2%i==0 and sayi1%i==0):
            ebob=i
else:
    for i in range(1,sayi2+1):
        if(sayi2%i==0 and sayi1%i==0):
            ebob=i
print(f"\n{sayi1} ve {sayi2} 'nin EBOBU {ebob} dur.")
if(ebob==1):
    print("Sayilar aralarinda asaldir")