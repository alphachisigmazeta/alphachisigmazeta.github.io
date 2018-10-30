---
layout: post
title:  "Coding Session"
date:   2018-10-30
excerpt: "Learn to Code"
image: "/images/fa18-exec.jpg"
published: true
---

## Coding Session

We will be coding in Python!
```python
if __name__ == '__main__':
    main()
```

Here are some basic usages:

First, we will look at basic variables and arrays
```python
x = 5
print(x) # this will print 5

x = x + 5
'''
Question. What will print(x) be?
'''

a = 1.0
b = 1

'''
Question. What's the difference between a and b?
'''

y = x/2
z = (0.0 + x)/2

'''
Hard Question. What are y and x
'''

array = [1,2,3,4,5]
print(array[0]) # this will print 1... I know, weird
print(array[4]) # this will print 5
print(array[-1]) # this will print 5
print(array[-4]) # this will print 2

print(array[1:5]) # will print indices [1,5), so [2,3,4,5]

short_array = array[1:-1]

'''
Question. What will print(short_array) be?
'''

array.append(6)
print(array) # this will print [1,2,3,4,5,6]

'''
Question. What will print(array[-1]) print?
'''

print(len(array)) # will print length of the array :: 6

'''
Question. What will the following print
print(array[len(array)/2]) 
'''

x = 6
y = 7
if(x > y):
    x = y
else:
    y = x
'''
Question. What is the code above doing?
'''
```

### Coding Problem
Given an array of 
```python
arr = [67, 89, 91, 99, 72, 85, 33, 70, 55, 90, 91, 99, 89, 67, 70, 70, 80]
sum = ...
mean = ...
mode = ...
median = ...
max = ...
min = ...
range = ...
```

---

### Coding Competition
This is the [file](/files/teaching-axe-code.zip)

