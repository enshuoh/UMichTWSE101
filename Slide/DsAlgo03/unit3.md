# Unit 3
## Sorted Arrays

<img src="http://www.kdnuggets.com/wp-content/uploads/sorting.jpg">

--

## 為什麼要排序？

<img src="http://i.imgur.com/7PRjHvd.png">

* 比較符合人類邏輯、 
* 能有效率地搜尋、
* 因為人類只能循序漸進地做事。

--

## 為什麼要研究排序？

<figure>
<img src="http://bbs.ahalei.com/data/attachment/forum/201402/23/120852kg1dvagi0b1ijtlv.png">
<figcaption>http://bbs.ahalei.com/thread-4399-1-1.html</figcaption>
</figure>

* Q: 要怎麼從一堆數字當中找出最大的那個？
* [參考說法：排序在資訊領域的重要性](https://www.quora.com/Why-is-sorting-important-in-computer-science-and-programming)

--

## 演算法的效率

* <font color=yellow>Time Complexity</font>（時間複雜度）
  - 對於一個演算法 $\mathcal{A}$ 而言，當輸入的資料量為 $n$ 的時候，最壞情形下執行的時間為 $f(n)$。


--

## 時間複雜度

* <font color=yellow>Time Complexity</font>（時間複雜度）
  - 對於一個演算法 $\mathcal{A}$ 而言，當輸入的<font color=red>資料量</font>為 $n$ 的時候，<font color=red>最壞情形下</font>執行的<font color=red>時間</font>為 $f(n)$。
  - 我們（目前）只關心成長率：隨著資料增長，執行時間的增長幅度為何？ <!-- .element: class="fragment" -->
* <!-- .element: class="fragment" --><font color=yellow>漸進函數 $\Theta(f(n))$</font> 
  - 上界函數 $O(f(n))$
  - 下界函數 $\Omega(f(n))$
  - <font color=grey>What is $U(m)$</font>?

--

## 重點摘要

* $\Theta(1)$
* $\Theta(\log n)$
* $\Theta(\log^2 n)$
* $\Theta(\sqrt{n})$
* $\Theta(n)$
* $\Theta(n\log n)$
* $\Theta(n^2)$
* $\Theta(2^n)$

http://vaxxxa.github.io/talks/introduction.to.algorithms-computational.complexity/index.html#/28

--

## 關於排序演算法

<figure>
<img src="http://i.imgur.com/fq0A8hx.gif">
<figcaption>https://www.toptal.com/developers/sorting-algorithms/</figcaption>
</figure>

--

## 現成的排序實作 I

回傳一個新的、排序好的 List

```py
arr = [('A', 5), ('C', 1), ('E', 4), ('D', 2), ('B', 3)]
sorted(arr)
# [('A', 5), ('B', 3), ('C', 1), ('D', 2), ('E', 4)]
```
<!-- .element style="font-size:36%" -->

在原本的 List 上面直接排序

```py
arr.sort()
```
<!-- .element style="font-size:36%" -->

--

## 現成的排序實作 II

* Reverse flag

```py
sorted(arr, reverse=True)
# [('E', 4), ('D', 2), ('C', 1),
#  ('B', 3), ('A', 5)]
```
<!-- .element style="font-size:50%" -->

* Key functions

```py
from operator import itemgetter, attrgetter
sorted(arr, key=itemgetter(1))
# [('C', 1), ('D', 2), ('B', 3),
#  ('E', 4), ('A', 5)]
```
<!-- .element style="font-size:50%" -->

--

## 現成的排序實作 III

* Custom Comparison Function

```py
def mycmp(x, y):
    return x[1] - y[1]

from functools import cmp_to_key
sorted(arr, key=cmp_to_key(mycmp))
```

--

## 附帶一提

* <font color=red>[延伸閱讀]</font> [TimSort](https://en.wikipedia.org/wiki/Timsort) (Python), [IntroSort](https://en.wikipedia.org/wiki/Introsort) (C++)

--

## 附帶一題

* https://leetcode.com/problems/compare-version-numbers/

--

## 排序的應用 1

* 找最大值
* 找最小值
* 找中位數
* 找第 $k$ 小的數

--

## 排序的應用 2

* 移除重複元素

```py
import numpy as np
np.unique([1, 2, 3, 4, 1, 1, 3, 1])
# [1, 2, 3, 4]
```

--

## 排序的應用 3

* 給你 $N$ 個數字，問最接近的兩個數字其距離為何？（$x, y$ 的距離就是 $|x-y|$）

--

## 排序的應用 4

* Intersection of Two Arrays
* https://leetcode.com/problems/intersection-of-two-arrays/

--

## 排序的應用 5 - I

* 搜尋某個給定的值(key) 
* 二分搜尋法
* https://docs.python.org/3.5/library/bisect.html
* https://leetcode.com/problems/search-insert-position/

```py
from bisect import bisect
bisect(arr, x, lo, hi)
```

--

## 排序的應用 5 - II

* Column-wise & Row-wise Sorted Matrix
* https://leetcode.com/problems/search-a-2d-matrix/
* https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

--


