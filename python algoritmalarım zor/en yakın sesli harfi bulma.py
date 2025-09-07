# Bir harf verildiğinde,harfe en yakın sesli harfi döndüren bir fonksiyon oluşturun.
# Verilen harfe iki sesli harf eşit uzaklıktaysa,sonraki sesli harfi döndürün

# EXAMPLES:
# nearest_vowel("s")-> "u"
# nearest_vowel("c")-> "e"
# nearest_vowel("i")-> "i"
# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

str=input("bir harf girin:")
list=[]
sesli={0:"a",1:"e",2:"i",3:"o",4:"u"}
for i in sesli.values():
    list.append(abs(ord(str)-ord(i)))
print(list)
enkucuk=min(list)
enkucukler=[]

for j in range(len(list)):
    if(list[j]==enkucuk):
        soldaki=j
sonuc=sesli[soldaki]
print(sonuc)

