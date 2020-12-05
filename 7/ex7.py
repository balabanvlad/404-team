n = int(input("Introduceti nr de pitici: "))
A = []
B = []
print("Introducti cate pitic-kilograme slabesti la fiecare casa: ")
for x in range(n):
    w = int(input())
    A.append(w)

print("Introducti cate pitic-kilograme doreste sa slabeasca fiecare pitic: ")
for x in range(n):
    w = int(input())
    B.append(w)

j = 0
count = 0
visited = 0
check = 0
count = [1]*n

def func(count):
    maxim = count[0]
    count2 = 0
    print("rezultat final: ")
    for x in range(len(count)):
        maxim = max(count[x], maxim)
    print("maxim = ", maxim)
    for x in range(0, len(count)):
        if(count[x] == maxim):
            count2 += 1
    print("de cate ori ", count2)
    print("\n\n\n")

for i in range(0,n):
    obiectiv = A[i]
    j = i
    p = i
    check = 0
    visited = i-1
    if obiectiv >= B[i]:
        obiectiv = A[i]
        print("Piticul ", i, "a vizitat casa" )
        print(i)
        print("\n")
    else:
        print("Piticul", i, "a vizitat casele")

    for k in range(i, n):
        check += A[k]
    if check < B[i]:
        for k in range(i, n):
            print(k)
        print("dar nu a reusit sa-si atinga obiectivul")

    while(obiectiv < B[i]):
        if(j < n-1):
            j += 1
            obiectiv += A[j]
            count[j] += 1
            while(visited < j):
                    visited += 1
                    print(visited)
    if ( j == n-2):
        func(count)
