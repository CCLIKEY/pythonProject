nums = [1,23,5,4,6,54,12,23,21,31,34,14,0,5,9,10]
target = 21

def findsum():
    count_i = 0
    count_j = 0
    for i in nums:
        for j in nums:
            if (i + j == target):
                return count_i,count_j
            count_j += 1
        count_j = 0
        count_i += 1


def F(N):
    if((N==0)or(N==1)):
        return N
    return F(N-1)+F(N-2)

def fib(n):
    sqrt5 = 5**0.5
    fibnN = ((1+sqrt5)/2)**n-((1-sqrt5)/2)**n
    return round(fibnN/sqrt5)


if __name__ == '__main__':
    for i in range(10):
        print(F(i),end=" ")
    print("\r\n")
    for i in range(10):
        print(i,end=" ")
    print("\r\n")
    print(fib(9))


