import time
def claPI():
    N = 100_000_000 #计算1千万次累加
    sum = 0.0
    getInitTimes = time.time()
    for i in range(N+1):
        if(i%2==0):
            sum = sum + 1/(2*i+1)
        elif(i%2==1):
            sum = sum - 1/(2*i+1)
    print("waste:"+str(time.time()-getInitTimes)+"s") #返回值 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    print(sum*4)
if __name__ == '__main__':
    claPI()