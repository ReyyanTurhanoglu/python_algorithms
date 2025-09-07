# 1'den 50'ye kadar tam sayıları yineleyen bir Pyton programı yazın.3'ün katları için sayı yerine "Big",7'nin katları yerine "Bang" yazın.
# Hem 3'ün hem 7'nin katı olan sayılar için "BigBang" yazdırın.
for i in range (51):
    if i%3 ==0 and i%7==0:
        print("BigBang")
    elif i%3==0:
        print("Big")
    elif i%7==0:
        print("Bang")
    else:
        print(i)




