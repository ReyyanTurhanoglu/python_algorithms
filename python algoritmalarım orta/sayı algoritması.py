# Create an algorithm that if the place value of the number you get from the user is less than 3,print the square of the number instead
# if greater than 3 and odd,print the 2 less of the number instead
# if greater than 3 and even,print the 1 more of the number instead
# if no valid value is entered, print "invalid input"

sayi=input("lütfen bir sayi giriniz:")
if(sayi.isdigit()):
  
  for i in sayi:
    i=int(i)
    if i<3:
         print(i**2)
    elif(i>=3 and i%2 !=0):
         print(i-2)
    else:
         print(i+1)
else:
 print("geçersiz giriş")


