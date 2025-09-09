# sayıyı doğru tahmin etmeye çalışacağız, cow=rakam ve yeri doğru ; bul=rakam sayıda var ama o konumda değil başka bir sırada.
import random
sayi="".join(random.sample("0123456789",4))
print(f"sayi:{sayi}")
count=0
cow,bul=0,0
while cow!=len(sayi):
    cow,bul=0,0
    guess=input("enter a 4 digit number:")
    for i in range(len(sayi)):
        if sayi[i]==guess[i]:
            cow+=1
        elif guess[i] in sayi:
            bul+=1
    count+=1
    print(f"guess:{count} cow:{cow},bul:{bul}")
print(f"Congrats! Number of try: {count}")

