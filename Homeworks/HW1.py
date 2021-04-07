#Question 1
list1 =[1,2,3,4,5,6,7,8,9,10]
print("Original List = ",list1)
list2 = list()
for i in range(1,(len(list1)//2)+1):
  list2.append(list1[(-1)])
  list1.pop()
list2.reverse()
list2.extend(list1)
list1[:] = []
list1.extend(list2)
print("Final List = ",list1)   

#Question 2
control=True
while control :
  n=int(input("Please input a single digit integer: "))
  if 0<n<10:
    for i in range(n+1):
      if (i%2==0):
        print(i)
    control=False
  elif 0>n>-10:
    for i in range(0,n-1,-1):
      if (i%2==0):
       print(i)
    control=False
  else:
    print("ERROR! Number is not a single digit integer!\n")
