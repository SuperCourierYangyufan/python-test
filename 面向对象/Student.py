class Student(object):
  # 规定该类只准拥有那些属性
  # 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
  __slots__ = ('id', 'name','sex','__privateInfo','age')

  # 初始化方法
  def __init__(self, id, name, sex):
    self.id = id
    self.name = name
    # 私有属性,无法访问
    self.__privateInfo = sex

  def sayHello(self):
    print("hello!")

  def printInfo(self):
    print('id:%d;name:%s,__privateInfo:%s' % (
      self.id, self.name, self.__privateInfo))


sudent = Student(1, 'tom', '男')
sudent.printInfo()

# 无法访问私有
# print(sudent.__privateInfo)
# 可以使用这种方式访问,不推荐
print(sudent._Student__privateInfo)

print(hasattr(sudent, 'id'))
setattr(sudent, 'age', 18)
print(getattr(sudent, 'age'))
print(getattr(sudent, 'isMaster', '你不是'))
# 删除属性
# del sudent.name
# sudent.printInfo()