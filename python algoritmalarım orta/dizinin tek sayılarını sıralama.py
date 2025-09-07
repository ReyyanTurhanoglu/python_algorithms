# Verilen dizide tek sayıları sıralı , çift sayıları orijinal konumlarında tutan bir algoritma oluşturun.
 # EXAMPLES
  # (5,8,6,3,4) >> (3,8,6,5,4)

listem=[5,8,1,6,3,4,7]  #  -> tekler kendi aralarında 1,3,5,7 şeklinde sıralanmalı
odd=[i for i in listem if i%2]
odd=sorted(odd)
yenilistem=[]
k=0
for i in listem:
    if i%2:
        yenilistem.append(odd[k])
        k+=1
    else:
        yenilistem.append(i)
print(yenilistem)



