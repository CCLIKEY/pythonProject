def Fibonacci(N):
    if(N<2):
        return N
    else:
        return Fibonacci(N-1)+ Fibonacci(N-2)

def Fibonacci2(N):
    sqrt5 = 5**0.5
    fibnN = ((1+sqrt5)/2)**N-((1-sqrt5)/2)**N
    return round(fibnN/sqrt5)

value = [20,25,30,35,40]
import time

if __name__ == '__main__':
    # for count in value:
    #     s = time.time()
    #     for i in range(count):
    #         print(Fibonacci2(i),end=" ")
    #     print("\r\n花费时间为: ",(time.time() - s), "s")
    with open("Fibonacci.txt", "w") as f:
        for i in range(50):
            # print(Fibonacci2(i), end=" ")
            f.write(str(Fibonacci2(i)) + "  ")
    f.close()



    """  第一次
        with open("Fibonacci.txt","w") as f:
        for i in range(20):
            print(Fibonacci(i),end=" ")
            f.write(str(Fibonacci(i))+"  ")
        f.close()
    """

