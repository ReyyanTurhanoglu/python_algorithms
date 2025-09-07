#Bir dizideki ilk sayıyı son sayıyla,ikinci sayıyı sondan ikinci sayıyla ve sayılar bitene kadar eşleştiren bir fonksiyon yazın.
#Notlar:
# eğer eleman sayısı tekse ortadaki sayıyı kendisiyle eşleştir
# küme boşsa boş olarak döndür
# examples
#      (1,2,3,4,5,6,7)  ->   ((1,7),(2,6),(3,5),(4,4))
#       (1,2,3,4,5,6)    ->   ((1,6),(2,5),(3,4))
#             ()         ->        ()


def eşleştir(list):
    list_new=[]
    for i in range(len(list)//2):
        list_new.append([list[i],list[-1-i]])
    if len(list)%2==1:
        list_new.append([list[len(list)//2],list[len(list)//2]])
    print(list_new) 
a=[1,2,3,4,5,6,7]
eşleştir(a)

