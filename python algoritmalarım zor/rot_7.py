# Kullanıcıdan aldığınız bir cümle veya kelimeyi ilk harfi 7 nci harfi olacak şekilde kodlayıp çıktı olarak veren bir algoritma oluşturun
# Example:
# Joseph >> Ötyiüm
# Mr.Bean >> Sv.Gifş
def cyrpto(word):
    str=""
    alphabet="a,b,c,ç,d,e,f,g,ğ,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z"
    rot_7=   "f,g,ğ,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z,a,b,c,ç,d,e"
    for i in word:
        if(i.isupper()):
         str+= rot_7[alphabet.index(i.lower()) ].upper()
        elif(i.islower()):
           str+=rot_7[alphabet.index(i)]
        else:
           str+=i
    print(str)
      

word=input("cümle veya kelime girişi:")
cyrpto(word)
