# Section 2
## Basic Data Types

<img src='http://i.imgur.com/uGAX3XS.png'>

--

## 前置作業 1: Split a string

* 在進行第二階段之前，我們要先了解如何簡單把輸入變成 list。

```py
s = input().split(" ")
```

如果輸入是

```html
test 1 2 3 4 5
```

那麼執行結果就會是

```py
s = ['test', '1', '2', '3', '4', '5']
```

--

## 前置作業 2: Extended Tuple Unpacking

* 我們還可以利用 Python 的特性，取出 List 前幾個元素、並且把剩下的元素集中到另一個 List 裡頭。

```
a = [1, 2, 3, 4, 5]
head, *rest = a  # 注意 rest 之前有個星星

#### Result:
# head = 1
# rest = [2, 3, 4, 5]
```

--

## 前置作業 3: Convert Strings to Integers

* 目的：把整個 list 每個字串都換成整數。

```py
a = ['1', '2', '3', '4', '5']
b = list(map(int, a))
# b = [1, 2, 3, 4, 5]
```

* 看不懂 [map](https://docs.python.org/3.5/library/functions.html#map) 沒關係，先抄再說！

--

## List（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/python-lists)
* 參考提示：
  - 如何讀入操作總數 $n$？
  - 如何把每一行指令完整讀進來以後切塊？
  - 如何判斷第一個指令是七個指令中的哪一種？
  - List 支援哪些操作？（請參考 [Documentation](https://docs.python.org/3/library/stdtypes.html#lists)）

--

## List（解答篇）


```py
n = int(input())
ans = list()
for x in range(0, n):
    cmd, *args = input().split(" ")
    args = list(map(int, args))
    if cmd == "insert":
        ans.insert(args[0], args[1])
    elif cmd == "print":
        print(ans)
    elif cmd == "append":
        ans.append(args[0])
    elif cmd == "remove":
        ans.remove(args[0])
    elif cmd == "sort":
        ans.sort()
    elif cmd == "pop":
        ans.pop()
    elif cmd == "reverse":
        ans.reverse()
```

* 接下來的內容<font color="red">看不懂請跳過，絕不影響身心健康</font>。

--

## List（延伸篇）

* 我們發現其實參數可以無視長度直接傳進去，比方說剛才的某一行：

```py
ans.insert(args[0], args[1])
```

可以寫成這樣：

```python
ans.insert( *args )
```

--

## List（延伸篇 II）

* 我們還發現有一種叫做 `eval()` 函數的功能，可以把字串即時轉換成 python 語法並且執行。
* 除了 `print` 以外，其他 cmd 都跟實際 list 的語法相同！

```py
elif cmd == "append":
    ans.append(args[0])
elif cmd == "remove":
    ans.remove(args[0])
```

可以換成：

```py
    eval("ans." + cmd + "(args[0])")
```

--

## List（終極篇）

* 我們不需要擔心有沒有參數，反正丟 `*args` 進去就對了！
* 如果你還會 string interpolation 語法的話...

```py
n = int(input())
ans = list()
for x in range(0, n):
    cmd, *args = input().split(" ")
    args = list(map(int, args))
    if cmd == "print":
        print(ans)
    else: #Magic
        eval("ans.%s(*args)" % cmd)
```

* `eval()` 會有資安疑慮，請小心使用。

--

## 前置作業 4: List Comprehension

如果我們想要「產生」一個新的 list，可以利用 List Comprehension 取代產生這個 list 所需要的迴圈。

```python
>>> [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
```

可以用 if 篩選想要的迴圈元素：

```python
>>> [x**2 for x in range(10) if x%3==0]
[0, 9, 36, 81]
```


--

## 前置作業 4: List Comprehension

for 跟 if 可以混著用、多次使用！

```python
>>> [(x, y) for x in range(3)
...         for y in range(3)
...         if (x+y)%2==1]
[(0, 1), (1, 0), (1, 2), (2, 1)]
```

--

## List Comprehensions（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/list-comprehensions)
* 給你 $X, Y, Z, N$ 的值，請找出所有的格子點 $(X_i, Y_i, Z_i)$ 使得他們的座標範圍落在 $[0, X]\times [0, Y]\times [0, Z]$ 而且三個座標值相加不等於 $N$。


--

## List Comprehensions（解答篇）

* 基本上就是跑三個 for 加上一個 if 全部串起來就對啦～

```python
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

ans = [[x, y, z] for x in range(X+1) 
      for y in range(Y+1)
      for z in range(Z+1) if x+y+z!=N]

print(ans)
```


--

## Nested Lists（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/nested-list)
* 給你學生的名字和成績，請輸出成績第二差的所有名字（並依照字典順序排序輸出）

--

## Nested Lists（不給解答篇）

* sort 的應用~




--


## 前置作業 5: Lambda Functions

* 把它想成簡易的「一行文」函數就可以了～
* 推薦參考文章：[https://blog.liang2.tw/python-tutorial-slides/old.2013.04/#lambda-builtin](https://blog.liang2.tw/python-tutorial-slides/old.2013.04/#lambda-builtin)

```
>>> list(map(lambda x: x**2, range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

--


## Any or All（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/any-or-all)
* 給你 $N$ 個數字，請問這 $N$ 個數字是否同時滿足：
    * 條件一：所有數字都是正數
    * 條件二：存在某個數字是迴文數字
* 提示：判斷 $x$ 是否為迴文數字可以用

```python
lambda x: str(x)[::-1] == str(x)
```

--


## Any or All（解答篇）


```python
n = int(input())
arr = list(map(int, input().split()))
print(
  all(map(lambda x: x > 0, arr))
  and
  any(map(
    lambda y: str(y)[::-1] == str(y),
    arr)))
```

--

## 一個困難的問題

為什麼下面這個寫法會錯？


```python
n = int(input())
arr = map(int, input().split())   # ?!
print(
  all(map(lambda x: x > 0, arr))
  and
  any(map(
    lambda y: str(y)[::-1] == str(y),
    arr)))
```

* 我們之後才能回答，看不懂請先認明：想要用 list 的時候就把它強制轉成 list。

--


# Stay Tuned!

## 下集待續
