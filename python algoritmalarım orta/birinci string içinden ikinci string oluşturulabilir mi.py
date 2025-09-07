# birinci string içindeki harflerle ikinci string oluşturulabiliyorsa true;oluşturulamıyorsa false döndüren fonksiyon kodunu yazınız.
# örneğin:
# scramble('rkqodlw','world') ==> True
# scramble('katas','steak')  ==> False
def scramble(str1,str2):
 list1=list(str1)
 list2=list(str2)
 try:
   for i in list2:
        list1.remove(i)
    
   return True
 except Exception as e:
  return False

str1="rkqodlw"
str2="world"
print(scramble(str1,str2))      

    



