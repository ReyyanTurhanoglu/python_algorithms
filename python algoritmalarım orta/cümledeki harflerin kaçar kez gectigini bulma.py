# cümledeki harflerin kaçar kez gectigini donduren program kodunu yazın
cumle=input("cumle girin:")
harfler=list(cumle)
dict={}
for i in harfler:
    sayi=harfler.count(i)
    dict[i]=sayi
print("BULUNAN HARFLER VE SAYILARI")
for key,value in dict.items():
    print(key,":",value)