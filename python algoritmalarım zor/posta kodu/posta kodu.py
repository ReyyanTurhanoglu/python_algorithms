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
