Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#### LIST ####
#### how to declare List ####
[]
[]
k = []
k
[]
type(k)
<class 'list'>
k = [10,20,30,40,50]
k
[10, 20, 30, 40, 50]
#### List allows Duplicate items ####
k = [10,20,30,40,50,10,20,10]
k
[10, 20, 30, 40, 50, 10, 20, 10]
#### Background datastructure of list is an array so it supports slicing,indexing ####
k[:]
[10, 20, 30, 40, 50, 10, 20, 10]
#### when nothing is given by default it takes complete list ####
k[0]
10
k[-1]
10
k[4]
50
k[:-1]
[10, 20, 30, 40, 50, 10, 20]
k[:-3]
[10, 20, 30, 40, 50]
k[2:]
[30, 40, 50, 10, 20, 10]
#### we can reverse the list ####
k[::-1]
[10, 20, 10, 50, 40, 30, 20, 10]
#### to access elements between 50 & 20 ####
k[4:7]
[50, 10, 20]
#### here i considered reversed list however the actual list is declared at the top #####
k[-2:-4]
[]
k[-2:-4:-1]
[20, 10]
#### list supports hetrogenous and homogenous values ####
#### when list consists of elements of same data type then it is homogeneous e.g [10,20,30,40,50] ####
#### [10,'a',3.14,i+7j] when list contains elements of different data types then it is hetrogenous.####
#### Sequence order is preserved in list ####
#### Duplicates are allowed in list ####
#### List is mutable ####
#### example of mutable ####
v = [10,20,30,40,50]
id(v)
2760962328128
#### lets edit v ####
v[1]
20
v[1] = 200
v
[10, 200, 30, 40, 50]
id(v)
2760962328128
v
[10, 200, 30, 40, 50]
#### here we can say id of the lists are same that means we do not require new object to save the changes,change is saved in the same object thats why it is called as mutable ####
v
[10, 200, 30, 40, 50]
#### lets make changes in v lets add 300 and 400 in place of 30 & 40 ####
v[2:4]
[30, 40]
v[2:4] = [300,400]
v
[10, 200, 300, 400, 50]
#### also change 10 to 100 and 50 to 500 ####
v[0] = [100]
v
[[100], 200, 300, 400, 50]
v[0] = 100
v
[100, 200, 300, 400, 50]
v[4] = 500
v
[100, 200, 300, 400, 500]
#### lets add element in the list ####
v.append('a')
v
[100, 200, 300, 400, 500, 'a']
v.append('b,c,d,e')
v
[100, 200, 300, 400, 500, 'a', 'b,c,d,e']
#### append adds the element to the end of the list ####
v.append(3.14)
v
[100, 200, 300, 400, 500, 'a', 'b,c,d,e', 3.14]
#### lets check methods of list ####
dir(v)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#### lets check clear ####
v.clear()
v
[]
#### it removes all the elements from the list ####
v = ['vaibhav',10,20,'vidya',30,40,'vivaan',50,60,'vidip',70,80]
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
v.copy()
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
#### copy method copies all the elements of the list ####
#### lets see what is shallow copy and deep copy ####
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
g = v.copy()
g
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
id(v)
2760993643456
id(g)
2760962328128
g.append('ladge')
g
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge']
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
#### in the above example we can see object ids of both the objects are different however the elements in the object are same.
#### if we make changes in one object it does not affect the other object ####
#### this is called shallow copy####
v = g
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge']
g
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge']
id(v)
2760962328128
id(g)
2760962328128
g[:-1]
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
g
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge']
v[:-1]
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80]
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge']
v.append('how are you')
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you']
g
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you']
#### in the above example we can see id's of both the objects are same ,if we make change in one object the same change can be seen in other object as well ####
#### this is called as deep copy #####
#### lets see method count ####
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you']
v.count('v')
0
v.count('zoo')
0
c = ['vaibhav vikas ladge,vidya vaibhav ladge,vivaan vaibhav ladge,vidip vaibhav ladge']
c
['vaibhav vikas ladge,vidya vaibhav ladge,vivaan vaibhav ladge,vidip vaibhav ladge']
c.count('vaibhav')
0
c = ['vaibhav vikas ladge','vidya vaibhav ladge','vivaan vaibhav ladge','vidip vaibhav ladge']
c
['vaibhav vikas ladge', 'vidya vaibhav ladge', 'vivaan vaibhav ladge', 'vidip vaibhav ladge']
c.count('vaibhav')
0
['vaibhav vikas ladge', 'vidya vaibhav ladge', 'vivaan vaibhav ladge', 'vidip vaibhav ladge','vaibhav vikas ladge']
['vaibhav vikas ladge', 'vidya vaibhav ladge', 'vivaan vaibhav ladge', 'vidip vaibhav ladge', 'vaibhav vikas ladge']
c.count('vaibhav vikas ladge')
1
['vaibhav vikas ladge', 'vidya vaibhav ladge', 'vivaan vaibhav ladge', 'vidip vaibhav ladge','vaibhav vikas ladge','vaibhav vikas ladge']
['vaibhav vikas ladge', 'vidya vaibhav ladge', 'vivaan vaibhav ladge', 'vidip vaibhav ladge', 'vaibhav vikas ladge', 'vaibhav vikas ladge']
c.count('vaibhav vikas ladge')
1
['vaibhav vikas ladge, vidya vaibhav ladge, vivaan vaibhav ladge, vidip vaibhav ladge,vaibhav vikas ladge,vaibhav vikas ladge']
['vaibhav vikas ladge, vidya vaibhav ladge, vivaan vaibhav ladge, vidip vaibhav ladge,vaibhav vikas ladge,vaibhav vikas ladge']
c.count('vaibhav vikas ladge')
1
c = [10,20,10,30,10,40,10]
c
[10, 20, 10, 30, 10, 40, 10]
c.count(10)
4
b = ['vaibhav vikas ladge,vaibhav vikas ladge,vaibhav vikas ladge']
b
['vaibhav vikas ladge,vaibhav vikas ladge,vaibhav vikas ladge']
b.count('vaibhav vikas ladge')
0
c = [a,a,a,a,a]
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    c = [a,a,a,a,a]
NameError: name 'a' is not defined
c = ['a','a','a','a']
c
['a', 'a', 'a', 'a']
c.count('a')
4
b = ['vaibhav vikas ladge','vaibhav vikas ladge','vaibhav vikas ladge']
b
['vaibhav vikas ladge', 'vaibhav vikas ladge', 'vaibhav vikas ladge']
b.count('vaibhav vikas ladge')
3
 v
 
SyntaxError: unexpected indent
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you']
v.append(110,'swati')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    v.append(110,'swati')
TypeError: list.append() takes exactly one argument (2 given)
v.extend(110,'swati')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    v.extend(110,'swati')
TypeError: list.extend() takes exactly one argument (2 given)
v.extend[110,'swati']
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    v.extend[110,'swati']
TypeError: 'builtin_function_or_method' object is not subscriptable
v.extend([110,'swati'])
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you', 110, 'swati']
v.append([110,'swati'])
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you', 110, 'swati', [110, 'swati']]
v.extend['swati']
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    v.extend['swati']
TypeError: 'builtin_function_or_method' object is not subscriptable
v.extend('swati')
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you', 110, 'swati', [110, 'swati'], 's', 'w', 'a', 't', 'i']
v.append(3.14)
v
['vaibhav', 10, 20, 'vidya', 30, 40, 'vivaan', 50, 60, 'vidip', 70, 80, 'ladge', 'how are you', 110, 'swati', [110, 'swati'], 's', 'w', 'a', 't', 'i', 3.14]
v.extend(3.14)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    v.extend(3.14)
TypeError: 'float' object is not iterable
v.extend[3.14]
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    v.extend[3.14]
TypeError: 'builtin_function_or_method' object is not subscriptable
#### lets see the difference between append and extend ####
#### extend does not includes float,decimal,boolean whereas append includes everything####
#### append includes the element as a single whereas extend includes the element as different items ####

##########################################################
####          List of List          ####
d = [[10,20][30,40]]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    d = [[10,20][30,40]]
TypeError: list indices must be integers or slices, not tuple
d = [[10,20],[30,40]]
d
[[10, 20], [30, 40]]
d[0]
[10, 20]
d[1]
[30, 40]
d[-1]
[30, 40]
d[-2]
[10, 20]
#### lets change value of all the elements ####
d[0][0]
10
d[0][0] = 100
d
[[100, 20], [30, 40]]
d[0][1] = 200
d
[[100, 200], [30, 40]]
d[1][0] = 300
d
[[100, 200], [300, 40]]
d[1][1] = 400
d
[[100, 200], [300, 400]]
#### lets add name in the list ####
d[0].append('vaibhav')
d
[[100, 200, 'vaibhav'], [300, 400]]
d[1].append('vidya')
d
[[100, 200, 'vaibhav'], [300, 400, 'vidya']]
###################################################
####            Index method        ####
v.index('vaibhav')
0
v.index('vidya')
3
v.index('vikas')
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    v.index('vikas')
ValueError: 'vikas' is not in list
d = ['manisha','priya','sapna','rashmi']
d
['manisha', 'priya', 'sapna', 'rashmi']
v.index('p')
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    v.index('p')
ValueError: 'p' is not in list
v.index('priya')
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    v.index('priya')
ValueError: 'priya' is not in list
v.index('manisha')
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    v.index('manisha')
ValueError: 'manisha' is not in list
d.index('rashmi')
3
##########################################################
d = ['a','b','a']
d
['a', 'b', 'a']
d.index('a')
0
###################################################
####     method insert     ####
#### inserts element before the given index ####
k = [12,24,48,60,84,108]
k
[12, 24, 48, 60, 84, 108]
k.insert(2,36)
k
[12, 24, 36, 48, 60, 84, 108]
k.insert(5,72)
k
[12, 24, 36, 48, 60, 72, 84, 108]
k.insert(7,96)
k
[12, 24, 36, 48, 60, 72, 84, 96, 108]
k.insert(-1,100)
k
[12, 24, 36, 48, 60, 72, 84, 96, 100, 108]
k.insert(-5,66)
k
[12, 24, 36, 48, 60, 66, 72, 84, 96, 100, 108]
#### add element at the end after 108 ####
len(k)
11
k.insert(12,120)
k
[12, 24, 36, 48, 60, 66, 72, 84, 96, 100, 108, 120]
k.insert(len(k+1),132)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    k.insert(len(k+1),132)
TypeError: can only concatenate list (not "int") to list
k.insert((len(k + 1)),132)
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    k.insert((len(k + 1)),132)
TypeError: can only concatenate list (not "int") to list
#############################################################
####    method pop    ####
k
[12, 24, 36, 48, 60, 66, 72, 84, 96, 100, 108, 120]
k.pop()
120
k.pop()
108
k
[12, 24, 36, 48, 60, 66, 72, 84, 96, 100]
k.pop(3)
48
k
[12, 24, 36, 60, 66, 72, 84, 96, 100]
k.pop(-3)
84
k
[12, 24, 36, 60, 66, 72, 96, 100]
#### pop removes only one item at a time
#### pop removes element from right to left by default
#### pop can remove particular item by passing index of the element
#### pop throughs error if the element is not present in the list
k.pop(8)
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    k.pop(8)
IndexError: pop index out of range
############################################################
####    method remove    ####
#### remove is value based
#### removes the element occuring at first index when multiple items of same value are present
k
[12, 24, 36, 60, 66, 72, 96, 100]
k.remove(24)
k
[12, 36, 60, 66, 72, 96, 100]
k.remove()
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    k.remove()
TypeError: list.remove() takes exactly one argument (0 given)
k.remove(72)
k
[12, 36, 60, 66, 96, 100]
k.remove(5)
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    k.remove(5)
ValueError: list.remove(x): x not in list
################################################################
####    Method reverse and reversed    ####
k
[12, 36, 60, 66, 96, 100]
k.reverse()
k
[100, 96, 66, 60, 36, 12]
k
[100, 96, 66, 60, 36, 12]
k.reverse()
k
[12, 36, 60, 66, 96, 100]
k.reversed()
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    k.reversed()
AttributeError: 'list' object has no attribute 'reversed'. Did you mean: 'reverse'?
reversed(k)
<list_reverseiterator object at 0x00000282D80931C0>
list[reversed(k)]
list[<list_reverseiterator object at 0x00000282D8093430>]
list(reversed(k))
[100, 96, 66, 60, 36, 12]
#########################################################
####    sort    ####
k
[12, 36, 60, 66, 96, 100]
k.sort()
k
[12, 36, 60, 66, 96, 100]
k = [96, 0 ,80,18,76,22,32,70,66]
k.sort()
k
[0, 18, 22, 32, 66, 70, 76, 80, 96]
#### sort methos by default sorts list in ascending order ####
k
[0, 18, 22, 32, 66, 70, 76, 80, 96]
k.sort(reverse = true)
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    k.sort(reverse = true)
NameError: name 'true' is not defined. Did you mean: 'True'?
k.sort(reverse = True)
k
[96, 80, 76, 70, 66, 32, 22, 18, 0]
#### by using reverse = True we can sort the list in descending order  ####
k
[96, 80, 76, 70, 66, 32, 22, 18, 0]
k = [96,80,76,'and','or','del']
k
[96, 80, 76, 'and', 'or', 'del']
k.sort()
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    k.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
k = ['c','f','a','m','q','b']
k
['c', 'f', 'a', 'm', 'q', 'b']
k.sort()
k
['a', 'b', 'c', 'f', 'm', 'q']
k.sort(reverse = True)
k
['q', 'm', 'f', 'c', 'b', 'a']
#### Sort method cannot sort list with string and integer either it has to be string or integer. ####
