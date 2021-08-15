a=[1,2,3,4,5,6,7,8,9,10]
b=[2,4,6,8,10]
c=[3,6,9,3]
a.append(100)
print("the edited list is",a)
print("the new sorted list is(ascending order)",a.sort())
print("the empty list",b.clear())
z=a.extend(c)
print("the combined lists of a and c are",a)
print("the new sorted list is",a)
print("the total number of times 3 occurs is ",a.count(3))
print("the index of first element is",a.index(1))
print("inserting 1000 at the beginning",a.insert(0,1000))
print(a)
print("removing the first element",a.pop(0))
print(a)
a.remove(3)
print(a.count(3))
print(a)
a.sort()
print("the list in ascending order",a)
print("the list in descending order",a.reverse())
print(a)




