#1
def square_generator(n):
    result = []  
    for i in range(n):
        k = i**2
        result.append(k)
    return result

n = int(input("n: "))
squares = square_generator(n)

for square in squares:
    print(square)


#2
def evens(n):
    result=[]
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result

n=int(input("n:"))
k=evens(n)
print(k)


#3
def d34(n):
    result=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            result.append(i)
    return result

n=int(input("n:"))
k=d34(n)
print(k)


#4
def squares(a,b):
    result=[]
    for i in range(a,b,1):
        result.append(i**2)
    return result

a=int(input("a: "))
b=int(input("b: "))
c=squares(a,b)
print(c)

#5
def from_n_to_0(n):
    result=[]
    for i in range(n,-1,-1):
        result.append(i)
    return result

n=int(input("n: "))
print(from_n_to_0(n))
