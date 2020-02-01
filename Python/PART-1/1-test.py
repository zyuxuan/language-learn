#!/usr/bin/env python3

print('hello world')

# 一、Python基础
# 1、使用list和tuple
#（1）list
'''
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
比如，列出班里所有同学的名字，就可以用一个list表示：
'''
classmates = ['a','b','c']
print(len(classmates)) # 用len()函数可以获得list元素的个数,用索引来访问list中每一个位置的元素，索引是从0开始的
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素,以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-1]," ",classmates[-2]," ",classmates[-3]," ")
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append("d")
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'v')
print(classmates)
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

'''
list里面的元素的数据类型也可以不同，比如：
>>> L = ['Apple', 123, True]
list元素也可以是另一个list，比如：
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4
要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
'''

#（2）tuple
'''
 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
 >>> classmates = ('Michael', 'Bob', 'Tracy')
现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
>>> t = (1, 2)
>>> t
(1, 2)
如果要定义一个空的tuple，可以写成()：
>>> t = ()
>>> t
()
但是，要定义一个只有1个元素的tuple，如果你这么定义：
>>> t = (1)
>>> t
1
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
>>> t = (1,)
>>> t
(1,)
Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
最后来看一个“可变的”tuple：
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

小结
list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
'''

# 2、条件判断
'''
根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
'''
age = 20
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 3、循环
'''
Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
'''
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和
'''
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 4、使用dict和set
#（1）dict
'''
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，
直接取出来，所以速度非常快。

你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
>>> d['Adam'] = 67
>>> d['Adam']
67
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88
如果key不存在，dict就会报错：

>>> d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

>>> 'Thomas' in d
False
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：

>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
注意：返回None的时候Python的交互环境不显示结果。

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
'''

#（2）set
'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：

>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

重复元素在set中自动被过滤：

>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：

>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
通过remove(key)方法可以删除元素：

>>> s.remove(4)
>>> s
{1, 2, 3}
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，
也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
'''
s1 = set([1, 2, 3])
#s2 = set([2, 3, [1, 2, 3]])
'''
再议不可变对象
上面我们讲了，str是不变对象，而list是可变对象。

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
而对于不可变对象，比如str，对str进行操作呢：

>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？

我们先把代码改成下面这样：

>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

┌───┐                  ┌───────┐
│ a │─────────────────>│ 'abc' │
└───┘                  └───────┘
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

┌───┐                  ┌───────┐
│ a │─────────────────>│ 'abc' │
└───┘                  └───────┘
┌───┐                  ┌───────┐
│ b │─────────────────>│ 'Abc' │
└───┘                  └───────┘
所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

小结
使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。

https://github.com/michaelliao/learn-python3/blob/master/samples/basic/the_list.py
https://github.com/michaelliao/learn-python3/blob/master/samples/basic/the_tuple.py

https://github.com/michaelliao/learn-python3/blob/master/samples/basic/the_dict.py
https://github.com/michaelliao/learn-python3/blob/master/samples/basic/the_set.py

list:
classmates = ['Michael', 'Bob', 'Tracy']

tuple:
classmates = ('Michael', 'Bob', 'Tracy')

dict:
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

set:
s1 = set([1, 1, 2, 2, 3, 3])

'''











