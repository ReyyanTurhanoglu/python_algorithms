#ilk başta 7 dolabın yedisi de kapalı kapalı dolap->0  açık dolap->1 diye kodlansın
#0 0 0 0 0 0 0 
#birinci öğrenci birin katı olan dolapları açıyor
#1 1 1 1 1 1 1 
#ikinci öğrenci ikinci dolaptan başlayarak ikinin katı olan dolapları açıksa kapatıyor;kapalıysa açıyor
#1 0 1 0 1 0 1
#üçüncü öğrenci üçüncü dolaptan başlayarak üçün katı olan dolapları açıksa kapatıyor;kapalıysa açıyor
#1 0 0 0 1 1 1
#dördüncü öğrenci dördüncü dolaptan başlayarak aynı işlemi tekrarlıyor:
#1 0 0 1 1 1 1 
#beşinci öğrenci:
#1 0 0 1 0 1 1 
#altıncı öğrenci:
#1 0 0 1 0 0 1
#yedinci öğrenci:
#1 0 0 1 0 0 0
#sonuçta kaç dolabın açık kalacağını bulan algoritmayı yazın

def locker(sayi):
    locker=[0 for i in range(sayi)]
    for i in range(sayi):
        for j in range(i,sayi,i+1):
            if(locker[j]==0):
                locker[j]=1
            elif locker[j]==1:
                locker[j]=0
    return locker.count(1)

print(locker(7))  #->2 dolap açık kalır
print(locker(500))  #->22 dolap açık kalır

                



