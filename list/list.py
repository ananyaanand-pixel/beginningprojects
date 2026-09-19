#list work acc/to class
A= [18,'hi',34,89,0,'bye',66,10,2,35]
B= [3,8,1,0,2,9,7,5,9,6]
#in L->R , 0,1,2,3......
print(B[3])

#in R->L , -1,-2,-3......
print(B[-1])

#for range use ':' , last m jo number h usse 1 less answer m aayega
print(A[2:7])
print(B[2:8])

#for skipping use ':' twice, minimum 2 skip hoga if use 1 then kuch bhi skip nhi karega
print(B[1:9:2])
print(B[1:9:1])

print(B[:])
print(B[3:])
print(B[:6])

print(A[3:7])
print(A[3:7:2])
print(A[-6:-1:2])
print(A[-6:-1:-2]) #empty list because -2 is not in range of -6 to -1, yaha ye isliye hua cuz ye already ulta likhega and hum aur -2 dal diye so ulta ko ulta nhi karega
print(A[::-1]) #reverse list

A.append(100) #add 100 at end of list
print(A)
print(A.count(10)) #count how many 10 in list
A.insert(3,200) #add 200 at index 3
print(A)
print(A.index(200)) #find index of 200
A.remove(200) #remove 200 from list
print(A)
A.extend([300,400,500]) #add multiple values at end of list
print(A)
A.append([56,79]) #add list at end of list
print(A)


A.sort() #sort list in ascending order
print(A)
A.sort(reverse=True) #sort list in descending order
print(A)


