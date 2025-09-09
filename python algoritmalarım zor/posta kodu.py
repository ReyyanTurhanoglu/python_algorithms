# girdiğimiz sayıdaki rakamlarla oluşturulabilecek farklı posta kodlarını bulma,bulduğumuz posta kodlarından postalcode.txt dosyasında olanları tespit edip ekrana yazdırma

""" 
ELDE ETMEK İSTEDİĞİMİZ ÇIKTI:
2000 - ANTWERPEN
2020 - ANTWERPEN
2200 - HERENTALS,Morkhoven,Noorderwijk
2220 - Hallaar,HEIST-OP-DEN-BERG
2222 - Itegem,Wiekevorst
2280 - GROBBENDONK
2288 - Bouwel
2800 - MECHELEN,Walem
2820 - BONHEIDEN,Rijmenam
2880 - BORNEM,Hingene,Mariekerke,Weert
8000 - BRUGGE,Koolkerke
8020 - Hertsberge,OOSTKAMP,Ruddervoorde,Waardamme
8200 - Sint-Andries,Sint-Michiels
8800 - Beveren,Oekene,ROESELARE,Rumbeke
8820 - TORHOUT
8880 - LEDEGEM,Rollegem-Kapelle,Sint-Eloois-Winkel
"""

with open ("postalcode.txt","r",encoding="Latin-1") as file:
    txt=file.readlines()
def zip_code(number):
    set_number=list(set(str(number)))
    list1=[i+j+k+n for i in set_number for j in set_number for k in set_number for n in set_number]
    list2=[i for i in list1 if not i.startswith("0")]
    list3=[i for i in txt if i[0:4] in list2]
    list4=[i.replace("\t"," ").replace("\n","") for i in list3]
    dict1=dict()
    for i in sorted(list4,key=str.lower):
        if i[0:4] in dict1:
            dict1[i[0:4]]+=","+i[5:]
        else:
            dict1[i[0:4]]=i[5:]
    key_list=list(dict1.keys())
    values_list=list(dict1.values())
    for i in range(len(key_list)):
        print(key_list[i]+" - "+values_list[i])

zip_code(2800)
