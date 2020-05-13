# 注意：定义好函数后，只表示这个函数封装了一段代码
# 如果不主动调用函数，函数是不会主动执行
name = "小明"
# python 解释器知道下方定义了一个函数


def say_hello():
    """ 打招呼 """
    print('hello1')
    print("hello1")
    print("hello1")


print(name)

# 只有在程序中，主动调用函数，才会让函数执行


say_hello()

print(name)