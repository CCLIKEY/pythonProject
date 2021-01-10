"""
https://www.runoob.com/python/os-open.html
概述
os.open() 方法用于打开一个文件，并且设置需要的打开选项，模式参数mode参数是可选的，默认为 0777。
语法
open()方法语法格式如下：
os.open(file, flags[, mode]);
参数
file -- 要打开的文件
flags -- 该参数可以是以下选项，多个使用 "|" 隔开：
os.O_RDONLY: 以只读的方式打开
os.O_WRONLY: 以只写的方式打开
os.O_RDWR : 以读写的方式打开
os.O_NONBLOCK: 打开时不阻塞
os.O_APPEND: 以追加的方式打开
os.O_CREAT: 创建并打开一个新文件
os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
os.O_EXCL: 如果指定的文件存在，返回错误
os.O_SHLOCK: 自动获取共享锁
os.O_EXLOCK: 自动获取独立锁
os.O_DIRECT: 消除或减少缓存效果
os.O_FSYNC : 同步写入
os.O_NOFOLLOW: 不追踪软链接
mode -- 类似 chmod()。
返回值
返回新打开文件的描述符。

"""
import os
def create_article():
    get_name=  input("请输入文章名字:")
    os.mkdir(get_name)
    file_format = ['md','docx','xlsx']
    for each in file_format:
        file= get_name + "//" + get_name + '.' + each
        os.open(file, os.O_CREAT)
    print("创建成功哈!")


if __name__ == '__main__':
    create_article()


