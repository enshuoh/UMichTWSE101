# Unit 6
## Two Pointers

<img src="https://thumbs.dreamstime.com/z/map-closeup-two-pointers-set-route-67911947.jpg" style="width:500px">


--

## 先放資源

* [Quora: The Two Pointer Algorithm](https://tp-iiita.quora.com/The-Two-Pointer-Algorithm)

--

## 單調性 Monotonicity

* 遞增 increasing = non-decreasing
* 遞減 decreasing = non-increasing
* 嚴格遞增 strictly increasing
* 嚴格遞減 strictly decreasing

--

## 暖身題 1：合併排序法

* [Leetcode 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)


--

## Merge Sorted Array

```python
i, j = m, n
for k in range(m+n, 0, -1):
  if j == 0 or (i > 0 and
              j > 0 and
              nums1[i-1] > nums2[j-1]):
    nums1[k-1] = nums1[i-1]
    i -= 1
  else:
    nums1[k-1] = nums2[j-1]
    j -= 1
```

--

## 思考問題

```python
if j == 0 or (i > 0 and
            j > 0 and
            nums1[i-1] > nums2[j-1]):
```

寫成以下形式

```python
if j == 0 or (i > 0 and
            nums1[i-1] > nums2[j-1]):
```

是否可行？

--

## 暖身題 2：快速排序法

* 給定一個陣列 $A[0..n-1]$。設 $x = A[0]$，原地把所有數字分成兩段：$\le x$ 與 $>x$ 的兩段。

<a href="http://algs4.cs.princeton.edu/23quicksort/images/partitioning-overview.png"><img src="http://algs4.cs.princeton.edu/23quicksort/images/partitioning-overview.png" style="width:450px"></a>

<!--* 類似題：[Leetcode 283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)-->
<!--* 類似題：[Leetcode 86. Partition List](https://leetcode.com/problems/partition-list/)-->
* 類似題：[Leetcode 75. Sort Colors](https://leetcode.com/problems/sort-colors/)

--

## 暖身題 3：Two Sum II

* [Leetcode 167. Two Sum II - Input Array is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
* 給定一個遞增數列 $numbers[1..n]$，請找到兩個數字加起來等於 $target$
<img src="http://www.supercouponlady.com/wp-content/uploads/2015/11/target_416x416.jpg" style="width:50px;vertical-align:middle" >
* 例子：$\\{1, 2, 4, 6, 7, 8, 12\\}$, $target=11$

--

## 暖身題 3：Two Sum II

```python
lo = 0
hi = len(numbers)-1
while lo < hi:
  S = numbers[lo] + numbers[hi]
  if S == target:
    return [lo+1, hi+1]
  elif S < target:
    lo += 1
  else:
    hi -= 1
```

--

## 暖身題 3：Two Sum II

另一種寫法：逐一嘗試左界。

```python
hi = len(numbers)-1
for lo in range(0, len(numbers)):
  while hi > 0 and numbers[lo] + numbers[hi] > target:
    hi -= 1
  if numbers[lo] + numbers[hi] == target:
    return [lo+1, hi+1]
```
<!-- .element: style="font-size:40%" -->

--

## 暖身題 4：Search a 2D Matrix

* [Leetcode 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```

* target=3, return=`True`

--

## 暖身題 4：Search a 2D Matrix

* Two Sum II 是上面這題的一個特例（為什麼？）

```python
N = len(matrix)
M = len(matrix[0])
j = M-1
for i in range(N):
  while j > 0 and matrix[i][j] > target:
    j -= 1
  if matrix[i][j] == target:
    return True
return False
```
<!-- .element: style="font-size:48%" -->

--

## 熱身題 5：Count $A[i] < B[j]$

* 給你兩個**已由小到大排序**陣列 $A[0..n-1]$ 以及 $B[0..m-1]$，問有多少個數對 $(i, j)$ 使得 $A[i] < B[j]$？

--

## 發燒題 6：Count of Range Sum

* [題目敘述](https://leetcode.com/problems/count-of-range-sum/)


--

## 先備知識

[合併排序法 Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)

<img src="https://tshop.r10s.com/8f0/814/b7ab/fe36/b09f/58bb/9b47/11a8e6bf81005056ae3884.jpg" style="width:500px">

--

## 先備知識 2

* 前綴和 (Prefix Sum, Cumulative Sum)

```python
import numpy
a = [1, 2, 3]
numpy.cumsum(a) # [1, 3, 6]
```

--

## Solution Hint

* 「不超過 $upper$ 的 $(i, j)$ 數量」扣除<br>「嚴格小於 $lower$ 的 $(i, j)$ 數量」
* Divide and Conquer <font color=gray>like a boss</font>

<img src="http://synergizeonline.net/bookmark-awards/wp-content/uploads/2013/09/like-a-boss21.jpg" style="width:300px">

--

# Have a good weekend!
