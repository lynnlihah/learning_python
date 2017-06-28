# 使用__slots__ - 用于限制实例的属性绑定
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
class Student(object):
    pass
s = Student()
s.name = 'Micheal'  # 动态给实例绑定一个属性
s.name # Micheal

def set_age(self, age):  # 给实例绑定一个方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 绑定完成
s.set_age(25)
s.age # 25

def set_score(self, score):  # 给class绑定方法
    self.score = score
Student.set_score = set_score

s.set_score(100)
s.score # 100

# 使用 __slots__ : 只允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义

s = Student()
s.name = 'Micheal'
s.age = 25
# s.score = 99 # AttributeError: 'Student' object has no attribute 'score'
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999 # 正常运行 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是
               # 自身的__slots__加上父类的__slots__。


# 只用@property - 内置装饰器，用于把一个方法变成属性
# 在get函数前加 @property
# 在set函数前加 @name.setter
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 使用
s = Student()
s.score = 60 # 实际转化为s.set_score(60)
s.score # 实际转化为s.get_score()
# s.score = 'str' # ValueError: score must be an interger!

class Student(object): #可读写属性和只读属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth # age 只读属性

# 多重继承
# Dog Bat Parrot Ostrich（鸵鸟）
class Animal(object):
    pass
# 大类：
class Mammal(Animal): # 哺乳类
    pass
class Bird(Animal):
    pass
# 具体动物：
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')


#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass
#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass

#MixIn - 指多重继承
# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
# 而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。
# 通过组合，我们就可以创造出合适的服务来。
'''
# 比如，编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 编写一个多线程模式的UDP服务，定义如下：

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：

class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
'''

# 定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# 修改前
class Student(object):
    def __init__(self, name):
        self.name = name
Student('Michael') # <__main__.Student object at 0x00000000028CB5C0>

# 修改后
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
Student('Michael') # Student object (name: Michael)

# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
# 所以，有个偷懒的写法： __repr__ = __str__

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000000:
            raise StopIteration()
        return self.a
    # __getitem__ - 使fib可以通过list取值
    '''
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a '''
    # 使fib可以使用切片(简陋版) -  传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# 使用
for n in Fib():
    #print(n)
    pass

f = Fib()
f[0] # 1

# __getattr__ - 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
s.score # 99 不重写 __getattr__会报错:AttributeError: 'Student' object has no attribute 'score'
s.age() # 返回lambda 25
# s.notexist # 不写raise,不会报错，显示：None


# 可利用__getattr__ 在写sdk的时候写一个链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path

    __repr__ = __str__

Chain().status.user.timeline.list # output: /status/user/timeline/list
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

# __call__ - 用于直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
# s() # My name is Michael.

# 要判断一个对象是否能被调用:
callable(Student('name')) # True
callable(max) # True
callable([1, 2, 3]) # False


# 枚举类 - unique 检查以保证没有重复值
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    # print(name, '=>', member, ',', member.value) # Jun => Month.Jun , 6 其中一条数据
    pass
@unique
class Weekday(Enum):
    Sun = 0 # # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问枚举值
day1 = Weekday.Mon # day1 值即为Weekday.Mon
Weekday['Tue'] # Weekday.Tue
Weekday.Tue.value # 2
Weekday(1) # Weekday.Mon


# 使用元类
# type() - 动态创建类
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建
# 出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
# h.hello() # Hello, world.
type(Hello) # <class 'type'> 跟用class关键字定义是一样的
type(h) # <class '__main__.Hello'>

# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# metaclass - metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
        # __new__()方法接收到的参数依次是：
        # 当前准备创建的类的对象；
        # 类的名字；
        # 类继承的父类集合；
        # 类的方法集合。

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，
# 然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L # output: [1]

# 而普通的list没有add()方法：
L2 = list()
# L2.add(1) # AttributeError: 'list' object has no attribute 'add'

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
# 也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# 尝试编写一个ORM框架：

# 1. 写出期待使用者用的调用接口代码，如一个User类来操作对应的数据库表User
'''
class User(Model):
    #  定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库
u.save()
'''
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法
# 比如save()全部由metaclass自动完成。

# 2. 按接口实现该ORM
# Field 类，用于保存数据库的字段名和字段类型
class Field(object):
    def __init__(self, name, columb_type):
        self.name = name
        self.column_type = columb_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field, 比如StringField, IntegerField等
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name, 'bigint')

# 3.编写ModelMetaclass - 最复杂
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' %(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 4.基类 Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
'''
ouput:
Found model: User
Found mapping: id ==> <IntegerField:id>
Found mapping: name ==> <StringField:username>
Found mapping: email ==> <StringField:email>
Found mapping: password ==> <StringField:password>
SQL: insert into User (id,username,email,password) values (?,?,?,?)
ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
'''

'''
当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
在ModelMetaclass中，一共做了几件事情：
    排除掉对Model类的修改；
    在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
    同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
    把表名保存到__table__中，这里简化为表名默认为类名。
在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
'''