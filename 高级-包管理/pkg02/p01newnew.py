
# 包含一个学生类
# 一个sayhello函数
# 一个打印句

class Student():
    def __init__(self, name="fq", age =18):
        self.name = name
        self.age = age
    def into(self):
        print("我的名字是{0}".format(self.name))

def sayhello():
    print("Hi,欢迎来到python的世界")

# 此判断语句建议一直作为程序的入口
if __name__ == "__main__":
    print("我是模块p01，叫我干毛线！")