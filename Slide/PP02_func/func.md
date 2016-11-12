# Functional Programming

--

## Why
- 邏輯簡單易懂
- 模組化更容易
- 利於平行化

--

## 範例
- 指令式
```python
  def fib(n):
    a,b = 1,1
    for i in range(2, n):
      tmp = b
      b = a+b
      a = tmp
    return b
```
- 函數式
```python
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)
```

--

## 範例
- 函數式2
```python
fib = lambda n:reduce(
        lambda x,n:[x[1],x[0]+x[1]],
        range(n),[0,1])[0]
```

--

## FP的定義
- 嚴格
  - 沒有mutable variables
  - 沒有賦值(assignments)
  - 沒有loop或其他imperative的控制結構
  - Ex: Pure Lisp
- 寬松
  - 專注於設計函數
  - 可以產生、接收、合成函式
    - Higher-order function

--

## Mutable vs. Immutable
- Mutable
  - 可改變
  - 例如 : Python的List
- Immutable
  - 不可改變
  - 例如 : Python的String, tuple

--

## 什麼組成了FP、特色
- 高階函數(Higher-order function)
  - 通常也支援一級函數(First-class function)
- 沒有副作用的操作（no side effect）

--
## 高階函數
- function可以做為其輸入的參數
- function可以做為其回傳值
- 範例
  ```
    def twice(function, x):
        return function(function(x))

    def f(x):
        return x + 3

    print(twice(f, 7)) # 13
  ```
  - map
  - reduce

--

## 一級函數 First-class function
- First-class citizen (First-class object)
  - 第一類物件具有特性:
    - 可被存入變數或其他結構
    - 可以作為參數被傳遞
    - 可以作為返回值
    - 可以在run-time被創造
    - 沒有被繫結至某一名稱，也可以存在
      - Ex: 匿名函數
  - 一級函數是高階函數的超集
    - 一級函數包含高階函數
  - C++ 11, java 8部分支援

--

## 沒有副作用
- 每個函數的執行都沒有副作用
  - 函數就是用來返回一個值
  - 不能修改外部變量的值
    - 所以純FP的語言，甚至不支援賦值
- Ex: i = i+1
  - 數學式看來毫無邏輯
- Ex: i++
  - i+1被存在某個地方，造成狀態的改變

--

## 沒有副作用 - 特色
- 浪費記憶體空間
- 獨立部分的執行順序可以打亂
  - 便於平行化 Lock free
  - Lazy Evaluation
  - 編譯器易於優化
  - Tail Recursion

--

## 平行化的阻礙 - Non-determinism
- 當平行執行的程式，共同存取到相同的變數時
  - 可能產生不同的結果
- Non-determinism =
  - Parallel processing + Mutable state

--

## Lazy Evaluation
- 需要的時候再執行 (Call by Need)
- 避免不必要的計算
  - 省下空間
  - 省下計算
- 讓無限長度的計算可行

--

## Tail Recursion
- 在函式裡的最後一個動作是函式呼叫
  - 可以直接利用現在函式的空間
  - 避免遞迴過深，記憶體Stack用完

--

## 常用的高階函式介紹
- map
  - 尋訪每個元素，加以處理，並且回傳處理後的元素
- filter
  - 回傳 布林值，以決定是否處理該元素
- reduce
  - 尋訪每個元素，依序組合元素，轉換成結果，丟給下個元素運算組合，然後產生最終組合的結果

--

## map
```python
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
```

--

## filter
```python
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
```

--

## reduce
```python
from functools import reduce
reduce(lambda x,y: x+y, [47,11,42,13])

f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])
```
