# 1. 模块
- 一个模块就是一个包含python代码的文件，后缀名是.py就可以，模块就是个python文件
- 为什么我们要有模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写，
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块命名应该遵守变量命名规则
    - 模块直接导入
            - 假如导入模块名称直接以数字开头，需要借助于importlib包可以实现导入以数字开头的模块名称
            
            import importlib
            新的模块名 = importlib.import_module("要导入的模块名")  # 相当于导入了一个模块并把导入模块赋值给了新的模块
            
    - 语法
    
        import module_name
        module_name.function_name
        module_name.class_name
    - 案例p01,p02
    - import 模块名 as 别名
        - 导入的同时给模块起一个别名（用as关键字）
        - 其余语法跟第一种相同
        
    - from module_name import func_name, class_name
        - 按上述方法有选择性地导入
        - 使用的时候直接使用导入的内容，不需要前缀
        - 案例p03(与p02对比使用区别)
        
    - from module_name import *
        - 导入模块所有内容
        - 此方法优点是使用时不需要模块名做前缀，但缺点是可能会产生命名污染的问题
    - if `__name__ == "__main__"` 的使用
        - 可以有效避免模块代码被导入的时候被动执行的问题
        - 建议所有程序的入口都以此代码为入口
        
# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径：
        - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
        # 案例p04
        
- 添加搜索路径(给list里添加东西)

            sys.path.append(dir)
- 模块的加载顺序
    1. 先搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径
    
# 2. 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构（必须有__init__.py的文件）

              |---包
              |---|--- __init__.py  包的标志文件
              |---|--- 模块1
              |---|--- 模块2
              |---|--- 子包(子文件夹)
              |---|---|--- __init__.py  包的标志文件
              |---|---|--- 子包模块1
              |---|---|--- 子包模块2

- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是：
            
                package_name.func_name()
                package_name.class_name.func_name()
        
    - import 包名 as 别名
        - 具体用法跟作用方式，跟上述模块导入一致
    - 注意的是此种方法是默认对当前包内的 __init__ .py 文件中内容的导入
    
    - import package_name.module_name
        - 导入包中一个具体的模块
        - 使用方法
        
                package_name.module_name.func_name()
                pakage_name.module_name.class_name().func_name()
                pakage_name.module_name.class_name().var()
        - 案例pkg01,p05
        
    - import package_name.module_name as 别名
    
- from ... import 导入
    - from package_name import module_name1, module_name2,...
    - 此种导入方法不执行当前包内的 __init__ .py 文件中的内容
    
            from package_name import module_name
            module_name.func_name()
    
    - from package_name import *
        - 导入当前包内的 __init__.py 文件中所有的函数和类
        - 使用方法
        
               func_name()
               class_name().func_name()
               class_name().var()
        案例p06，注意此种导入的具体内容
        
- from package_name.module.name import *
    - 导入包中指定的模块的所有内容
    - 使用方法
    
            func_name()
            class_name().func_name()
            
- 在开发环境中经常会所以用其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
    
- `__all__` 的用法
    - 在使用 from package_name import * 的时候，*可以导入的内容
    - `__init__.py` 中如果文件为空，或没有`__all__` ，那么只可以把`__init__`中的内容导入
    - `__init__` 如果设置了`__all__` 的值，那么按照`__all__` 指定的子包或者模块进行加载 如此则不会载入`__init__`中的内容
    - `__all__` = `[`'module1'`, `'module2'`, `'package1'`, ......]`
    - 案例p07，注意与p06 的区别
    
# 3. 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突

        setname()
        Student.setname()
        Dog.setname()
