# Unit 2
## Arrays

<img src="http://images.memes.com/meme/956987"
style="width:450px">

--

## Array

* 連續的記憶體空間
* 記憶體支援隨機存取

<img src="http://i.stack.imgur.com/vIKaD.png"
style="width:600px">

--

## Python List

* 實作了 1D Array (外加上很多方便的功能)

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

* Iterator

```
for x in a:
    print x
```

* List Comprehension

```python
a = range(0, 10)
a = [x**2 for x in a if x%2==0]
```

--

## List of Lists

* http://stackoverflow.com/questions/12791501/python-initializing-a-list-of-lists

--

## Numpy Array

* 實作了高維 Array (Matrix)

```
A = np.zeros((10, 100))
B = np.array([[1, 2, 3], [4, 5, 6]])
C = np.transpose(B)
C.shape
```

--

## Row Major vs Column Major

* Fortran-style Arrays vs C-style Arrays

<img src="https://informebaba.files.wordpress.com/2015/12/fig4.jpg?w=640">

--

## Numpy Array

```
import numpy as np
def set_values():
    m, n = 50, 1000000
    data = np.random.rand(m, n)
    data.sum(axis=0)
```

* 測試執行時間

```
timeit.Timer(set_values).timeit(1)
```

```
def set_values2():
    m, n = 50, 1000000
    data = np.random.rand(m, n)
    data.sum(axis=1)
```

--

## Application: Strings

* 最底層是一個 array of characters

```
list('this is a string')
```

--

## Application: Counters

* 把陣列當成計數器來使用

* Bucket Sort
  - https://leetcode.com/problems/top-k-frequent-elements/

--

## Challenge

* https://leetcode.com/problems/set-matrix-zeroes/
