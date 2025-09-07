# Bir cümlenin palindrom olup olmadığını kontrol eden bir program yazın 
cumle=input("bir cumle giriniz:")
cumle1=cumle
cumle2=cumle[::-1]
for i,j in zip(cumle1,cumle2):
    if(i!=j):
        print("palindrom degil")
        break
else: print("palindrom cumle")

    