try:
    import usocket as socket
except:
    import socket

def installPackage(package):
    import os
    try:
        import package
    except:
        os.system("pip3 install "+str(package))

import time
def fact(N):
    if(N==0):
        return 1
    elif(N!=0):
        return N*fact(N-1)



a = time.time()
if __name__ == '__main__':
    # installPackage("tensorflow")

    value = fact(99)
    b = time.time() - a
    print("花费时间:"+str(b)+"ms")
    print(value)
