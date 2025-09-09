 # Given a list of tuples, implement a method that sort a list in ascending order by the second element inside the tuples and return the list
# input =[("b",1),("c",2),("x",3),("x",4),("z",0)]
# output =[("z",0),("b",1),("c",2),("x",3),("x",4)]

list1=[("John",1),("Jade",2),("Lisa",3),("Rose",6),("Louie",0)]
list1=sorted(list1,key=lambda x:x[1])
print(list1)