# Write a python code that returns the digits value of the given number in a list
# EXAMPLE 1: -153 >> [-100,-50,-3] >> [-(1*10**2),-(5*10**1),-(3*10**0)]
# EXAMPLE 2: 1453 >> [1000,400,50,3]

sayi=input("bir sayi giriniz:")
liste=[]
count=0
if(int(sayi)>0):
  for i in sayi[::-1]:
    liste.append(int(i)*10**count)
    count+=1
  liste.reverse()
else:
  sayi=abs(int(sayi))
  sayi=str(sayi)
 
  for i in sayi[::-1]:
    liste.append(int(i)*10**count*-1)
    count+=1
  liste.reverse()
print(liste)
    
  
      
        


