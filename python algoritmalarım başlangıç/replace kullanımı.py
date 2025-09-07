# size verilen veya kullanıcıdan alınan stringin ilk karakterini değiştirmeden ilk karakter ile aynı olan karakteri ? ile değiştiren kodu yazınız.
#input >> restart
#output >> resta?t
#1. ÇÖZÜM
x=input("enter a word:")
kelime=x.replace(x[0],"?")[1:]
print(x[0]+kelime)
                 
#2. ÇÖZÜM
kelime=input("bir kelime girin:")
baslangic=kelime[0]
for i in range(len(kelime)):
    if kelime[i]==baslangic and i!=0:
        kelime=kelime[:i]+"?"+kelime[i+1:]
print(kelime)      
    
    