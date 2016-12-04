# Itertools
## Iterables, Iterators and Generators

--

http://anandology.com/python-practice-book/iterators.html

--

```python
for num in [1, 2, 3, 4, 5, 6, 7, 8]:
    print(num)
```

```python
for c in "hello world!":
    print(c)
```

```python
for line in open("file.txt"):
    print(line)
```

--


## Iterable

* 只要能夠支援掃過一次的東西都叫做 Iterable
* 例如 List, String, File Handler (Input), Generators...

也有一些內建函式使用 Iterator，比方說：

```py
",".join(["a", "b", "c"])
```

--

## Iteration Protocol

* 只要支援 `__next__()` 就行了。
* 回傳的是「下一個指到東西」
* 沒有東西了以後，要丟 `StopIteration` 出去。

--

## Iterator 迭代器

* 來寫寫 Range 吧！
  * PowerIterator: 希望按照 $1, 2, 4, 8, 16, 32, \ldots$ 輸出！
  * PrimeIterator: 希望按照 $2, 3, 5, 7, \ldots, $ 輸出！
* `next()` 和 `iter()`

--

## Generator 生成器

* 某些情形下 Iterator 寫起來很麻煩！
* 把函數變成「長得很像 Iterator」的東西（就是 Generator 啦）
* 關鍵字 **yield** $\to$ 呼叫函數會回傳 generator!

```py
def get_powers(a, n):
    current = 1
    for _ in range(n):
        yield current
        current *= a
```

--

## Itertools

* 一個 package 提供各式各樣方便的 iteration tools
* 舉例：產生 $1$ 到 $n$ 的全排列

```py
itertools.permutations((1, 2, 3))
```
