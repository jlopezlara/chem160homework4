Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: /Users/JessicaLopez/Documents/chem160homework4-master/point.py ==
>>> from point import *
>>> p1 = point(3, [1,2,3])
>>> print(p1)
1.0 2.0 3.0 
>>> p2 = point(3, [6,7,8])
>>> print(p2)
6.0 7.0 8.0 
>>> print("p1 add p2=", p1.add(p2))
p1 add p2= 27.0
>>> print("p1 add p2=", p1.sqmag(p2))
p1 add p2= 163.0
>>> 
