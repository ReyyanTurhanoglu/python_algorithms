# Birden fazla kelime içeren uzun bir dizi alın ve bu diziyi kelime kelime tersten yazdırın 
dizi=input("uzun bir cumle girin:")
a=dizi.split() 
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]+" "
print(b)
