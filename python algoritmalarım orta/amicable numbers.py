#amicable numbers:220 sayısının kendisi hariç tam bölenleri toplamı 284 yapar.284 sayısının kendsi hariç tam bölenleri toplamı 220 yapıyor bu durumda bu iki sayı amicable numbers oluyorlar.
x=int(input("bir sayı girin (örnek:220) :"))
x_tambölenleri=0
y_tambölenleri=0
for i in range(1,x):
    if(x % i== 0):
        x_tambölenleri+=i
y=x_tambölenleri
print(f"{x}'in tam bölenleri toplamı:{y}")
for i in range(1,y):
    if(y%i==0):
        y_tambölenleri+=i
print(f"{y}'nin tam bölenleri toplamı {y_tambölenleri}")
if(x==y_tambölenleri ):
    print("YES NUMBERS ARE AMICABLE NUMBERS")

else:
    print(f"Sorry,{x} is lonely number")

