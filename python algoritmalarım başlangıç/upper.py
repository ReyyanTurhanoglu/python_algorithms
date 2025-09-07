# Kullanıcıdan bir kelime alan ve bu kelimenin ilk harfinden başlayarak her seferinde bir harfi büyük harf olacak şekilde son harfe kadar işlemi tekrarlayan
# ve sonuçları liste içinde çıktı veren bir algoritma oluşturun.
#EXAMPLE:  >>   ['Reyyan', 'rEyyan', 'reYyan', 'reyYan', 'reyyAn', 'reyyaN']

kelime=input("bir kelime giriniz:")
kelime=kelime.lower()
liste=[]
uzunluk=len(kelime)
i=0
if(i!=uzunluk):
  for j in kelime:
    yenikelime=kelime[:i]+j.upper()+kelime[i+1:]
    liste.append(yenikelime)
    i+=1
      
print(liste)

