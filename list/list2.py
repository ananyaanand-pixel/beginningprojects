P= ['banana', 'apple', 'orange', 'grape', 'kiwi']
for x in P:
    print(x)

W= [4,7,2,3,8,-2,-7,-9,56,89,-74]
Y= []
B=[]
C= []
for x in W:
    if x>0:
        Y.append(x)


print(Y)

for x in W:
    if x%2==0: 
        B.append(x)

print(B)


for x in W:
    if x%2==0 and x>0: 
        C.append(x)

print(C)
