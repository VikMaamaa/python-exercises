Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the length of side A 6
Enter the length of side B 6
Enter the length of side B 6
The triangle is an equilateral triangle 
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the length of side A 3
Enter the length of side B 4
Enter the length of hypothenus, C 5
The triangle is a right angle triangle 
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the smaller number: 3
Enter the larger number: 4
Traceback (most recent call last):
  File "C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py", line 6, in <module>
    while true:
NameError: name 'true' is not defined
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the smaller number: 3
Enter the larger number: 2
Traceback (most recent call last):
  File "C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py", line 4, in <module>
    myNumber = random.randint(smaller, larger)
  File "C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\lib\random.py", line 221, in randint
    return self.randrange(a, b+1)
  File "C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\lib\random.py", line 199, in randrange
    raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (3,3, 0)
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the smaller number: 3
Enter the larger number: 9
Enter your guess4
You have got it in 1 tries
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
>>> d
{'b': -20, 'a': 35}
>>> d['c'] = 40
>>> d
{'b': -20, 'a': 35, 'c': 40}
>>> d['b'] = ""
>>> d
{'b': '', 'a': 35, 'c': 40}
>>> d.keys()
dict_keys(['b', 'a', 'c'])
>>> sort(d.keys())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sort(d.keys())
NameError: name 'sort' is not defined
>>> sorted(d.keys())
['a', 'b', 'c']
>>> data = "myprogram.exe"
>>> data = "myprogram.exe"
>>> data[6:10]
'ram.'
>>> data[5:10]
'gram.'
>>> data[5:9]
'gram'
>>> len(data)
13
>>> data[:10]
'myprogram.'
>>> data = data[:10]
>>> data
'myprogram.'
>>> data[1] = "h"
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data[1] = "h"
TypeError: 'str' object does not support item assignment
>>> data = "myprogram.exe"
>>> len(data)
13
>>> int(13/2)
6
>>> 13/2
6.5
>>> round(13/2)
6
>>> round(13/2,0)
6.0
>>> round(13/2,1)
6.5
>>> float(13/2,1)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(13/2,1)
TypeError: float() takes at most 1 argument (2 given)
>>> 13 % 2
1
>>> 12%2
0
>>> data[7]
'a'
>>> 
== RESTART: C:\Users\MAAMAA\AppData\Local\Programs\Python\Python36-32\as.py ==
Enter the string john
n h o j 
>>> 
