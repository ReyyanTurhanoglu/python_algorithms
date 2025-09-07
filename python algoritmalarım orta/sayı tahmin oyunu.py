# Sayı tahmin oyunu
# random seçilen sayıyı tahmin etmeye çalışınız
import random
random_num=random.randint(0,99)
guess_count=0

while True:
    guess_num=int(input("0-99 arasında sayıyı tahmin edin:"))
    if(random_num>guess_num):
        print("daha büyük bir sayı deneyin")
        guess_count+=1
    elif(random_num<guess_num):
        print("daha küçük bir sayı deneyin")
        guess_count+=1
    else:
        print(f"TEBRİKLER {random_num} değerini doğru tahmin ettiniz")
        guess_count+=1
        break
print(f"tahmin sayısı:{guess_count}")
    