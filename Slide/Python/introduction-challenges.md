# Section 1
## Introduction Challenges

![imgur](http://i.imgur.com/s77tH2H.png)

--

## Say "Hello, World!" With Python

* 學習重點：如何使用 print function

```
print("Hello, World!")
```

* 思考重點：這麼做可以把字串印到螢幕上（我們把這裡的螢幕視為<font color="yellow">標準輸出 stdout</font>）

--

## Reading Raw Input

* 學習重點：如何使用 input function 讀入字串

```
s = input()  # 先從鍵盤(stdin) 讀入字串
print(s)     # 直接輸出到螢幕(stdout) 上面
```

--

## Python If-Else （提示篇）

* [題目連結](https://www.hackerrank.com/challenges/py-if-else)
* 學習重點：
  - `if`, `elif`, `else`
  - 記得判斷式後面要加冒號、內容要縮排
* 他已經幫你寫好輸入了，可以直接使用變數 $N$：
```py
import sys
N = int(input().strip())
```
* 觀察：`int()` 是一個可以把字串轉換成整數的方法（這叫做 <font color="yellow">Type Conversion</font>）

--

## Python If-Else （解答篇）

```py
if N%2==1:
    print("Weird")
elif N >= 6 and N <= 20:
    print("Weird")
else:
    print("Not Weird")
```

* 觀察
  - 如果有 AND/OR 請記得直接寫 `and`/`or`，不像其他語言有奇怪的符號～
  - `N%2` 代表的是「計算 $N$ 除以 $2$ 的餘數」

