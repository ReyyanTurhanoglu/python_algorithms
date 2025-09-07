# Bir liste ve hedef sayısı verildiğinde listenin hangi iki elemanı ile o sayıya ulaşılabileceğini
# belirten bir python kodu yazın
# EXAMPLE :[2,8,9,15,5,12], target_num=17 >> [[0,3],[1,2],[2,1],[3,0],[4,5],[5,4]]

new_list=[]
def find(liste,target_num):

 for i in range(len(liste)):
    for j in range(len(liste)):
        if(liste[i]+liste[j]==target_num):
            new_list.append([i,j])
 
find([2,8,9,15,5,12],target_num=17)
print(new_list)




