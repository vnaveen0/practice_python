def elem_prod(r1,row,r2,col,N,r1m,r2n):
    x = 0
    for i in range(N):
        xi = row*N + i
        xj= col + i*r2n
        x+= r1[xi]*r2[xj]

    return x

[r1m,r1n] = [3,2]
r1 = [1,2,3,1,2,3]

[r2m,r2n] = [2,3]
r2 = [2,2,2,3,3,3]

r3 = [None]*r1m*r2n


#r1n==r2m == N
assert ('dimensions do not match multiply not possible',r1n == r2m)
N = r1n
for row in range(r1m):
    for col in range(r2n):
        k = row*r2n+col

        r3[k] = elem_prod(r1,row,r2,col,N,r1m,r2n)

print(r3)

