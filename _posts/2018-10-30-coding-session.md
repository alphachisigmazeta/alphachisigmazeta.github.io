---
layout: post
title:  "Coding Session"
date:   2018-10-30
excerpt: "Learn to Code"
published: true
---

## Coding Session

We will be coding in Python!
```python
if __name__ == '__main__':
    main()
```

### How do I install?
Make sure you have [Python3](https://www.python.org/download/releases/3.0/) installed. I recommend [Anaconda](https://www.anaconda.com/download/#linux) to handle all your downloads. However, it downloads a lot of excess stuff, so if you want to be advanced, you can download from here for [Windows](https://www.python.org/downloads/) and [Mac](https://www.python.org/downloads/mac-osx/).


### Intro to variables and syntax
```python
x = 5

x = x + 5

print(x) # this will print 10

x = x * 2
x = x / 2
x = x - x

print(x)

A = "Alpha"
S = 'Sigma'
print(A + " Chi " + S)

A = "alpha"
print(A + " Chi " + S)

```

1. What will print(x) be?
1. What will the second print() be?
1. What will the third print() be?


```python

a = 1.0
b = 1

y = x/2
z = (0.0 + x)/2

```

1. What's the difference between a and b?
1. (Hard) Are y and z different? How so?

### Now we move to arrays
```python
array = [1,2,3,4,5]

print(array[0]) # this will print 1... I know, weird

print(array[4]) # this will print 5

print(array[-1]) # this will print 5

print(array[-4]) # this will print 2

print(array[1:5]) # will print indices [1,5), so [2,3,4,5]

short_array = array[1:-1]
print(short_array)
```
1. What will print() be?

```python
array.append(6)

print(array) # this will print [1,2,3,4,5,6]

print(len(array)) # will print length of the array :: 6

print(array[len(array)/2]) 

```
1. What will print(array[-1]) print?
1. What will the second print() be

### Conditionals
```python
x = True
y = False

print(x and y) # print False
print(x or y) # print True
print(not x) # print False
```
1. What does False and False print?
1. What does False or False print?

```python
x = 6
y = 7
value = 0

if(x > y):
    value = y
else:
    value = x
```

1. What is the code above doing?

### Iterative Methods
```python
for i in range(5):
    print(i) # this will print values [0,5)

i = 0
while(i < 5):
    print(i)
    i = i + 1

arr = [0,1,2,3,4]
for x in arr:
  print(x)
```
1. What is the difference between the three?

### Finally, functions
```python
def mystery(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total

array = [1,2,3,4,5]
value = mystery(array)
print(value)
```
1. What does the above do?
1. What happens if I call mystery with [0,0,1,1,2]?

### Coding Problem
Given an array `arr`, make some functions that help me find...
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

## Coding Competition
All the necessary files will be [here](/files/teaching-axe-code.zip)

### Background Info
Your job is to make as much money as possible through **real** stocks of Amgen, AbbVie, and Abbott! These are real datasets from 2012-2018. The final competition will be handling all three stocks separately and trying to maximize profit. But how do you make money?

### The Challenge
You start with $0 and no stocks. Period. However, you can take a loan of money or stock whenever you need to. For example, you can buy a stock of Amgen for $40, however your balance will be -$40. Let's say you don't make any changes and at the end of the competition, the price of the Amgen is now $60. Then, your net total is $20, you so made **$20**! This is called **holding**.

Similarly, you can also "sell" a stock. If you "sell" a stock of Amgen at the same $40, you will have $40 in your pocket, but then you have -1 stocks of it. At the end of the game, you have will have $40 but then owe the $60 from Amgen. This is called **shorting**.

This is an example of the stock. As you can see with the ups and down, there are lots of opportunities to hold and sell to make a profit.
[Stock of Amgen Photo](/images/stocks.png)

### How the Code Works
The only file you should be touching is `algorithm.py`. This contains a single function which you have to code. Here's how it works:

The main code in `comp.py` (which will run your `algorithm.py` code) will iterate through each day and grab the stock price up to early 2018, give or take 100 days (The total number of days is about 2000). It will call your `makeDecisionToBuyOrSell()` function to consult whether to buy, sell, or do nothing with the stock. 

In your `makeDecisionToBuyOrsell()`, you are given the price, array to hold any numbers you like, and value of 0,1, or -1 (meaning you own nothing, you have one, or you owe a stock respectively). 

Your job is to use only those three variables to decide whether to return a keyword of "sell", "buy", or "" for nothing. (Note: You can only own one stock, so trying to buy a stock when you have 1 will do nothing).

### How to run the code

Once you have Python3 and your code is error free, just run the compy.py file with `python3 comp.py` to run a single run. We will be using allcomp.py to do the contest. **Make sure to not change comp.py. If you do, the code will remove any changes.**

### Some tips
Here are some basic to advanced tips and how to maximize your profits (and ultimately win a prize).

1. (Basic) 2012-2018 was a [bull market](https://www.investopedia.com/terms/b/bullmarket.asp), meaning it had a net gain. So if you buy a stock early and do nothing, chances are you will make money! Capitalize on this!
1. (Medium) A basic trading principle is called [SMA](https://www.investopedia.com/terms/s/sma.asp), or simple moving average. You basically take the last `x` amount of days and create a "moving" average. It's a simple technique that can tell you how the stock is currently performing to its history. You can see an example here:
![sma](/images/sma.png)
1. (Advanced) The price goes up and down in "waves," which usually rebound on things call [support and resistance](https://www.investopedia.com/trading/support-and-resistance-basics/) lines. If the stock "breaks" either of the lines, it means it will likely "ride" past it for a good amount of time. If you can notice when these happens, then shorting or holding until the end will be good.
