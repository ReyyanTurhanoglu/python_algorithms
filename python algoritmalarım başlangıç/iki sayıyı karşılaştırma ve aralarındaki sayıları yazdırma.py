# Get two numbers from user.If the first of these numbers is greater than the second,order all the  numbers between these numbers
#  from largest to smallest, otherwise from smallest to largest ...
#   Examples:

'''
input >> 20,15 , output >> 20,19,18,17,16,15
input >> 17,21 , output >> 17,18,19,20,21

'''
a=int(input("birinci sayi:"))
b=int(input("ikinci sayi:"))
if(a>b):
    for i in range(a,b-1,-1):
        print(i)
else:
    for i in range(a,b+1,1):
        print(i)