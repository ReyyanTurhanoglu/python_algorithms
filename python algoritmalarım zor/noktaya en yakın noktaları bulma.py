# analitik düzleme ait bir nokta listesi,bir merkez nokta ve bir k tamsayısı verildiğinde,merkez noktaya en yakın k kadar noktayı bulun.
# Example:
def nearist_points(list1,cen,k):
 result=[]
 for i in list1:
  a=((i[0]-cen[0])**2+(i[1]-cen[1])**2)**0.5
  result.append([a,i])
 return [ v for k,v in sorted(result)[:k]]

print(nearist_points([(1,3),(5,2),(2,4)],(4,1),2))

