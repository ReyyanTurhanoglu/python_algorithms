# Bir kelimenin birinci hecesinde kalın bir ünlü (a,ı,o,u) bulunuyorsa diğer hecelerdeki ünlüler de kalın örneğin -> rapor,sakal,yarın
# ince bir ünlü (e,i,ö,ü) bulunuyorsa diğer hecelerdeki ünlüler de ince örneğin -> nergis,süre,sözlü
# olursa kelimemiz büyük ünlü uyumuna uyar. 
kelime=input("bir kelime girin:")
kalın_ünlü=0
ince_ünlü=0
for i in kelime:
    if i in 'aıou':
        kalın_ünlü+=1
    if i in 'eiöü':
        ince_ünlü+=1

if(kalın_ünlü+ince_ünlü==1):  #Tek sesli harf varsa büyük ünlü uyumu aramayız örneğin -> tren,kalp,ses
    print("Büyük ünlü uyumu aranmaz")
elif(kalın_ünlü!=0 and ince_ünlü==0 or kalın_ünlü==0 and ince_ünlü!=0):
    print("Büyük ünlü uyumuna uyuyor")
else:
    print("Büyük ünlü uyumuna uymuyor")



