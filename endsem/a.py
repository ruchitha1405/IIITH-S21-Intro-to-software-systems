A = [10,80,2,3,5]
B = [90,12,4,5,2,3]

A.extend(B)
S=set(A)
L=list(S)
L.sort()
print(L)