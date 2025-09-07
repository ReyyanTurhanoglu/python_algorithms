 # Given two arrays - list1 and list2 - construct an algorithm that returns the elements of list1 which are subarrays of list2.
 # EXAMPLE
 # list1=["old","int","age","and"]
 # list2=["random","soldier","list","print","introduction"] -> r"and"om   pr"int"  s"old"ier  "int"roduction
 # returns ["old","int","and"]
list1=["old","int","age","and"]
list2=["random","soldier","list","print","introduction"]
new_list=[]
for i in list1:
    for j in list2:
        if i in j:
            new_list.append(i)
new_list=set(new_list)  # iki defa "int" yazmaması için kümeye çeviriyoruz
print(list(new_list))