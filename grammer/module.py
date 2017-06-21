# 模块:在Python中，一个.py文件就称之为一个模块
# 举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
# python所有内置函数-https://docs.python.org/3/library/functions.html
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
# 目录：
# mycompany
#   __init__.py
#   abc.py
#   xyz.py
# 现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
# 请注意，
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，# 而它的模块名就是mycompany。

# 可以有多级目录
# mycompany
#   web
#     __init__.py
#     utils.py
#     www.py
#   __init__.py
#   abc.py
#   utils.py
#   xyz.py
# 引用： 文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，
# 否则将无法导入系统自带的sys模块。

# 写一个hello模块，查看hello.py
# 使用
import hello
hello.test()    #hello, world!

#_xxx 私有变量或函数，正常写作用域都是public

# 安装第三方模块
# 第三方库都会在Python官方的pypi.python.org网站注册
# pip install $模块名称

# import搜索路径：
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

import sys
sys.path #查看路径

sys.path.append('/Users/michael/my_py_scripts') #添加搜索路径：运行时修改，运行结束后失效
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。