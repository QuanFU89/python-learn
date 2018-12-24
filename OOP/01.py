"""
定义一个学生类，用来形容学生
"""
# 定义一个空的类
class Student():
    # 一个空的类，pass代表直接跳过，此处必须有
    pass

# 定义一个对象
FQ = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需注意，def 的缩进层级，系统默认有一个self参数
    def dohomework(self):
        print("在做作业")
        # 在函数末尾使用return语句
        return
# 实例化一个叫FQ的学生，是一个具体的人
FQ = PythonStudent()
print(FQ.name)
print(FQ.age)
# 注意成员函数的调用没有传递进入参数
FQ.dohomework()