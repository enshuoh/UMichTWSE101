# Unit 5
## Divide and Conquer

<img src="http://bigdata.ices.utexas.edu/wp-content/uploads/2014/03/divide-and-conquer1.png" style="width:500px">

--

## Majority Element

* [題目敘述](https://leetcode.com/problems/majority-element/)
* 給你 $n$ 個數字，請問出現嚴格大於 $\lfloor n/2\rfloor$ 次的數字為何？

--

## Majority Element

```python
n = len(nums)
if n <= 1:
    return nums[0]
a = self.majorityElement(nums[0:n/2])
b = self.majorityElement(nums[n/2:])
if nums.count(a) > n/2:
    return a
if nums.count(b) > n/2:
    return b
return None
```

--

## Longest Substring with at least K repeating characters

* [題目敘述](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)


--

## Solution

```python
# import string
# import re

# 計算字元頻率
hashmap = map(lambda x: (x, s.count(x)), string.lowercase)

# 篩選不該出現的字元
badchar = filter(lambda (x, y): y > 0 and y < k, hashmap)
if len(badchar) == 0:
    return len(s)
    
# 把字串切成一段一段
pattern = ''.join(map(lambda (x,y): x, badchar))
substrs = re.split("[%s]"%pattern, s)

# 分而治之找出最佳解
ret = list(map(lambda x: self.longestSubstring(x, k), substrs))
return max(ret)
```
<!-- .element: style="font-size:35%" -->

--

## Count of Range Sum

* [題目敘述](https://leetcode.com/problems/count-of-range-sum/)


--

## 先備知識

[合併排序法 Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)

<img src="https://tshop.r10s.com/8f0/814/b7ab/fe36/b09f/58bb/9b47/11a8e6bf81005056ae3884.jpg" style="width:500px">

--

## Solution Hint

* 「不超過 $upper$ 的 $(i, j)$ 數量」扣除<br>「嚴格小於 $lower$ 的 $(i, j)$ 數量」
* Divide and Conquer <font color=gray>like a boss</font>

<img src="http://synergizeonline.net/bookmark-awards/wp-content/uploads/2013/09/like-a-boss21.jpg" style="width:300px">