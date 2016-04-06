
# ESC+H : terminal commands
* The Jupyter Notebook has two different keyboard input modes. Edit mode allows you to type code/text into a cell and is indicated by a green cell border. Command mode binds the keyboard to notebook level actions and is indicated by a grey cell border with a blue left margin.
* In the new IPython cells could have two states: when it has a green selection rectangle around it you can edit what's inside; when it has a grey rectangle around it you edit the cell itself (copy/paste/delete). Enter/Return makes it go green, Esc makes it go grey. When it is gray, 'dd' will delete it.

# Terminal warmup


```python
pwd
```


```python
ls
```

###### Some tweaks needed from ipython to jupyter: run, paste, edit


```python
9*54
```


```python
# Last command results
_
```


```python
x=_
```


```python
# Show cell 27 contents
rep 27
```


```python
9*54
```


```python
exec _i27
```

# Adavance Python


```python
#Instead of range, use xrange to avoid pre-generate
for i in xrange(2):
    print i;
```

    0
    1



```python
for item in L:
    print item
```


```python
L = ['Tom', 'Henry', 'Harry']

#Looping
print '#Looping'
for item in L:
    print item

#Index
print '#Index'
for i in xrange(len(L)):
    print i, L[i]

#Enumerate
print '#Enumerate in below'
C = enumerate(L)
print C
for i, item in enumerate(L):
    print i, item
```

    #Looping
    Tom
    Henry
    Harry
    #Index
    0 Tom
    1 Henry
    2 Harry
    #Enumerate in below
    <enumerate object at 0x1064229b0>
    0 Tom
    1 Henry
    2 Harry


# String List Zip


```python
first_names = ['Giovanna', 'Ryan', 'Jon']
last_names = ['Thron', 'Orban', 'Dinu']

#Loop two lists together
for i in xrange(len(first_names)):
    print first_names[i], last_names[i]

#Zip two lists by tuples
print zip(first_names, last_names)

#izip
from itertools import izip
for first, last in izip(first_names, last_names):
    print first, last
```

    Giovanna Thron
    Ryan Orban
    Jon Dinu
    [('Giovanna', 'Thron'), ('Ryan', 'Orban'), ('Jon', 'Dinu')]
    Giovanna Thron
    Ryan Orban
    Jon Dinu



```python
from itertools import izip, count
for i, first, last in izip(count(), first_names, last_names): 
    print i, first, last
```

    0 Giovanna Thron
    1 Ryan Orban
    2 Jon Dinu


* note to use count() inside izip() function, instead of count.

# 2D List Comperhension
* **List of list**: Lowest goes first, inside then outside
* **One list**: top to down


```python
#Double loop
L = [[1,2,3],[4,5,6],[7,8,9]]
doubled = []
for row in L:
    row2= []
    for item in row:
        row2.append(item*2)
    doubled.append(row2)
doubled
```




    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]




```python
#List Comprehension
doubled = [[item *2 for item in row]for row in L]
doubled
```

    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]



```python
#Flatten: *Note the order of the loop statements.
flat_double = [item for row in L for item in row]
print flat_double
#or translate to be:
flat_double1=[]
for row in L:
    for item in row:
        flat_double1.append(item)
print flat_double1
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
#If statements as filter
evens = [item for item in flat_double if item%2 ==0]
print evens
```

    [2, 4, 6, 8]
    [2, 4, 6, 8]





    [2, 4, 6, 8]




```python
# or translated to be:
evens1 = []
for item in flat_double:
    if item%2 == 0:
        evens1.append(item)
print evens1
```

    [2, 4, 6, 8]



```python
#Pure computing, no assignment
[item for item in flat_double if item%2 ==0]
```




    [2, 4, 6, 8]



# Generator Comprehension for String


```python
L = ["zack desario", "giovanna thron", "ryan orban", "jonathan dinu"]
M = [item for item in L] #Does not change anything
print 'M = ', M
P = (item.split() for item in L) #List of list by .split().
# Use (), 'P, a gernator, does not give a list, only an object'
print 'P =',P
# Use [], N will be a list.
N = [item.split() for item in L] #List of list by .split().
print 'N = ', N
```

    M =  ['zack desario', 'giovanna thron', 'ryan orban', 'jonathan dinu']
    P = <generator object <genexpr> at 0x1063cceb0>
    N =  [['zack', 'desario'], ['giovanna', 'thron'], ['ryan', 'orban'], ['jonathan', 'dinu']]



```python
# Use [ ]
for name in [item.split()[0] for item in L]:
    print name
```

    zack
    giovanna
    ryan
    jonathan



```python
# Use ( )
for name in (item.split()[0] for item in L):
    print name
```

    zack
    giovanna
    ryan
    jonathan


# Generators so far
* use ( ) instead of [ ]
* item.split()
* use xrange() instead of rang()

# Lambda Functions:

Lambda to define unnamed functions to customize sort and use functions like map, filter and reduce.
Remember, a lambda expression looks like this:
**lambda variable: variable expression**


```python
L = [(2, 4), (5, 3), (6, 8), (4, 1)]
sorted(L)
```




    [(2, 4), (4, 1), (5, 3), (6, 8)]




```python
L.sort(key=lambda x: x[0])
```

**All things you can do with list comprehensions you can also do with map.** It's more "Pythonic" to use list comprehensions, but understanding how to write maps is key for **numpy and pandas**, modules we will be using heavily.


```python
# Double every element of a list
def double_list(L):
    return map(lambda x: x * 2, L)
double_list(L)
```




    [(2, 4, 2, 4), (5, 3, 5, 3), (6, 8, 6, 8), (4, 1, 4, 1)]




```python
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!="X", garbled)
print message
```

    I am another secret message!



```python
#number 1 to 10 means including 10, so range(1,11)
squares = [x**2 for x in range(1,11)]
print squares
print filter(lambda x: x>=30 and x<=70, squares)
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    [36, 49, 64]


Lambdas are useful when you need a quick function to do some work for you.
If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.


```python
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=="Python", languages)
```

    ['Python']


Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.
When we **pass the lambda to filter, filter uses the lambda to determine what to filter**, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.


```python
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
```

    [0, 3, 6, 9, 12, 15]


# String and indices 


```python
#Stride
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]
```




    'BDF'




```python
# Reverse
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=garbled[::-1]
print message
message=message[::2] #Save it back after slicing the string.
print message
```

    IX XaXmX XtXhXeX XsXeXcXrXeXtX XmXeXsXsXaXgXeX!
    I am the secret message!



```python
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
```

    ['E', 'D', 'C', 'B', 'A']



```python
# The default starting index is 0.
# The default ending index is the end of the list.
# The default stride is 1.
# Omit Indices
to_five = ['A', 'B', 'C', 'D', 'E'] 
print to_five[3:] # prints ['D', 'E'] 
print to_five[:2] # prints ['A', 'B'] 
print to_five[::2] # print ['A', 'C', 'E']
```

    ['D', 'E']
    ['A', 'B']
    ['A', 'C', 'E']



```python

```
