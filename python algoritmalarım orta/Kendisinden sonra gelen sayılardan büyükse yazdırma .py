# Kendisinden sonra gelen sayılardan büyük olan sayıları yazdıran algoritmayı oluşturun
# EXAMPLES
# [3,13,11,2,1,9,5] >> [13,11,9,5]
# [5,5,5,5] >> [5]
list1=[3,13,11,2,1,9,5]
list2=[]
list2=[list1[i] for i in range(0,len(list1)) if list1[i]<max(list1[i:]) ]
print(list2)
other={i for i in list1 if i not in list2}
print(sorted(list(other),reverse=True))