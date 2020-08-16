n = int(input())
c = list()
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    c += [a+b]
for v in c:
    print(v)