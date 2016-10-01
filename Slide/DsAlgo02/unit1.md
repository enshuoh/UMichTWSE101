# Unit 1
## Python3 Basic Practices

<a href="https://zonble.gitbooks.io/dailywtf/content/0009/index.html"><img src="https://zonble.gitbooks.io/dailywtf/content/0009/1.jpg"
style="width:500px"></a>

--

## Warm-up: Simple Array Sum

* [題目連結 (Hackerrank)](https://www.hackerrank.com/challenges/simple-array-sum)

給定一個長度為 $N$ 的整數序列，  
請問這些整數加起來的值為何？

--

## Warm-up: Simple Array Sum

```python
print(sum(arr))
```

* `sum()` 函數 [使用說明](https://docs.python.org/3.3/library/functions.html?highlight=sum#sum)

--

## Example 1: Array Rotation

* [題目連結 (Leetcode 189)](https://leetcode.com/problems/rotate-array/)

給你一個 $n$ 個數字的陣列，  
請你將這個陣列的內容向右旋轉 $k$ 格，  
比方說下面有個 $n=7$ 個元素的陣列：

```
[1, 2, 3, 4, 5, 6, 7]
```

向右旋轉 $k=3$ 格會變成：

```
[5, 6, 7, 1, 2, 3, 4]
```

--

## Example 1: Array Rotation

* 利用 [slice 的功能](https://docs.python.org/3.3/library/functions.html?highlight=slice#slice)

```
class Solution(object):
  def rotate(self, nums, k):
    k = len(nums) - k
    nums = nums[k:] + nums[0:k]
```

* 這樣寫有什麼問題？

--

## Example 1: Array Rotation

```
nums = nums[k:] + nums[0:k]
```

- 新得到的 `nums` 跟原本的 `nums` 記憶體位置不同！  
- 所以 Leetcode 抓不到答案！

* 怎麼修正？

--

## Example 1: Array Rotation

* Slice again.

```python
nums[0:len(nums)] = nums[k:] + nums[0:k]
```

* `len()` 函數[使用說明](https://docs.python.org/3.3/library/functions.html?highlight=slice#len)
