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

--

# Stay Tuned!

## 下集待續
