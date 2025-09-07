# write a python code that calculates the factorial of the given number
def factorial(sayi):
    carpim=1
    while(sayi>0):
        carpim=carpim*sayi
        sayi-=1
    print(f"faktöriyeli:{carpim}")
hesapla=int(input("FAKTÖRİYELİ HESAPLANACAK SAYIYI GİRİN:"))
factorial(hesapla)