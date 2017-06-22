# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
# bart.print_score()  # Bart Simpson: 59
# lisa.print_score()  # Lisa Simpson: 87

# 类和实例
Student # 类 <class '__main__.Student'>
bart #  实例<__main__.Student object at 0x00000000024E9DD8>

#有了__init__方法，在创建实例的时候，必须传入与__init__方法匹配的参数
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
# 虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart.age = 8    # print(bart.age) output:8
# lisa.age    #'Student' object has no attribute 'age'

# 访问限制
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print__score(selfs):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 98)
# bart.__name # AttributeError: 'Student' object has no attribute '__name'

# 访问方法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print__score(selfs):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('Bart Simpson', 98)
bart.get_name() # Bart Simpson
# _name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器
# 对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
# 不同版本的Python解释器可能会把__name改成不同的变量名， 不建议使用

# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running...')
    pass

dog = Dog()
cat = Cat()
# dog.run()   # Dog is running...
# cat.run()   # Cat is running...

def run_twice(animal):
    animal.run()
    animal.run()

# run_twice(Animal()) # Animal is running...
# run_twice(Dog()) # Dog is running...

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

# run_twice(Tortoise()) # Tortoise is running slowly...

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# 获取对象信息
# type() - 返回对应的Class类型
# types 模块中有定义的常量用于判断数据类型
type(123) # <class 'int'>
import types
def fn():
    pass
type(fn) == types.FunctionType # True
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType

# ininstance()