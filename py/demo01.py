class Person(object):
    def __init__(self,name,age):
        print('1',self)
        self.name =name
        self.age = age
    def show(self):
        print('3',self)
        print(f'姓名为：{self.name},年龄为：{self.age}')

    def __del__(self):
        print('4',self)

p = Person('小强',19)
print('2',p)
print(id(p),type(p))
p.show()
