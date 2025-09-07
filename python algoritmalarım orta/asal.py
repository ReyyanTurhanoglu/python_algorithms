number=int(input("sayi girin:"))
def function():
    if(number==1):
        print("1 asal degildir")
        return 1
    for i in range(2,number):
        if(number%i==0):
            print("sayi asal degil")
            return 0
    else :
        print("Asal")
           
function()
    

