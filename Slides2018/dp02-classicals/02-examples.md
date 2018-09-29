## 實戰演練

Dynamic Programming Examples

---

### [Leetcode 221. Maximal Square](https://leetcode.com/problems/maximal-square/description/)

* Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

<code>
1 0 1 0 0<br>
1 0 <span class="red">1 1</span> 1<br>
1 1 <span class="red">1 1</span> 1<br>
1 0 0 1 0<br>
</code>

--

#### 我的觀察啦

* 定義 $dp[i][j] = $ 右下角在 $(i, j)$ 的最大正方形邊長。
* $dp[i][j] = \min\\{dp[i-1][j], dp[i][j-1], dp[i-1][j-1]\\}+1$

![](http://i.imgur.com/oH1IL8D.jpg)
<!-- .element: style="float:right;width:250px" -->

--

#### C++ Example

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int ans = 0;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (matrix[i-1][j-1] == '1') {
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]),
                                   dp[i-1][j-1])+1;
                    ans = max(ans, dp[i][j]);
                }
        return ans * ans;
    }
};
```
<!-- .element: class="line-numbers" -->

---

### [Leetcode 85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/)

* Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

<code>
1 0 1 0 0<br>
1 0 <span class="red">1 1 1</span><br>
1 1 <span class="red">1 1 1</span><br>
1 0 0 1 0<br>
</code>


--

#### 一點想法啦

* 定義 `$dp[i][j][k] =$` 右下角在 `$(i, j)$` 而且高度是 `$k$` 的最大矩形寬度。
* `$dp[i][j][k] = \begin{cases}
dp[i][j-1][k] + 1 & \text{if $A[i-k+1..i]$ are all 1s.}\\
0 & \text{otherwise.}
\end{cases}$`

[![](https://i.ytimg.com/vi/a5aKFnamWpU/hqdefault.jpg)](https://www.youtube.com/watch?v=a5aKFnamWpU)
<!-- .element: style="float:right;height:300px" -->


--

#### 另一些想法

* 預處理 `$up[i][j]$` 代表「從 `$(i, j)$` 往上面看有多少個連續的 1」
* 對每一個 `$i$`，看起來像是天際線...

[![](https://leetcode.com/static/images/problemset/skyline1.jpg)<!-- .element: style="height:300px" -->](https://leetcode.com/problems/the-skyline-problem/description/)
[![](https://leetcode.com/static/images/problemset/skyline2.jpg)<!-- .element: style="height:300px" -->](https://leetcode.com/problems/the-skyline-problem/description/)

--

#### 決定性的觀察

* 只有在天際線「高度變化」的時候才需要考慮最大矩形！

![](https://mmbiz.qpic.cn/mmbiz_jpg/vaNDRzClX3DG0JBTPYCUNkIm9ibrkLb0pictrN7NuRgOfuZKjrtfC91ib9cQz0ibTYo2twkGHTI54IzH8F1kZToVHQ/640?wx_fmt=jpeg&_ot=1530144000179)
<!-- .element: style="float:right;height:300px" -->

--


#### C++ Example 1

```cpp
class Solution {
public:
    int MaxRectOnRow(vector<int> &row) {
        int ret = 0;
        stack<pair<int, int>> s;
        s.push({0, 0});
        for (int i = 1; i < row.size(); i++) {
            int left = i;
            while (!s.empty() && row[i] <= s.top().second) {
                ret = max(ret, (int)(i - s.top().first) * s.top().second);
                left = s.top().first;
                s.pop();
            }
            s.push({left, row[i]});
        }
        while (!s.empty()) {
            ret = max(ret,
                      (int)(row.size() - s.top().first) * s.top().second);
            s.pop();
        }
        return ret;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> up(m+1, vector<int>(n+1, 0));
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                up[i][j] = (matrix[i-1][j-1] == '0' ? 0 : up[i-1][j] + 1);
        int ans = 0;
        for (int i = 1; i <= m; i++)
            ans = max(ans, MaxRectOnRow(up[i]));
        return ans;
    }
};
```
<!-- .element: class="line-numbers" -->


--

#### 想法中的想法，觀察中的觀察

* 把每一個最大矩形，交給一個認識的格子處理。(Bijection!?)
* Maximal Rectangle 的數量其實不超過 `$O(n^2)$`。

[![](https://img.gifhome.com/gif/s/2018/066b090eebba4d5d904473e79bc5980a.jpg?x-oss-process=image/resize,w_300)<!-- .element: style="float:right;height:300px" -->](https://wap.gifhome.com/s/?cid=141)

--

#### C++ Example 2

```cpp
有空現場寫QQ
```

--

### 小結：DP 小幫手

* stack
* pre-processing


![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAhyhfHYWWTn9Yvy8tyY-Ogzf219WnvHg51m-ZlBtEuvkjLBhu7Q)
<!-- .element: style="float:right;height:300px" -->

---

### [Leetcode 300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

* Given an unsorted array of integers, find the length of longest increasing subsequence.

[![](https://i.ytimg.com/vi/cNMNawe6FHI/hqdefault.jpg)<!-- .element: style="float:right;height:300px" -->](https://www.reddit.com/r/Borderlands2/comments/8pkzsc/borderlands_2_maya_subsequence_conference_call/)

--

#### Idea 1

* 令 $dp[i]=$ 結束在第 $i$ 個數字的 LIS 長度。
* `$dp[i] = 1$ or $\max_{j < i, a[j] < a[i]} \{ dp[j] + 1\}$`

--

#### C++ Example 1

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        int n = nums.size();
        vector<int> dp(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++)
                if (nums[j] < nums[i])
                    dp[i] = max(dp[i], dp[j] + 1);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```
<!-- .element: class="line-numbers" -->

--

#### C++ Example 2

```cpp
有空現場寫QQ
```

---

### [Leetcode 673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/)

Given an unsorted array of integers, find the number of longest increasing subsequence.

![](https://www.fluentu.com/blog/english/wp-content/uploads/sites/4/2015/04/X6BLS9y.png)
<!-- .element: style="float:right;height:300px" -->


--

#### Idea 1

* 令 $dp[i]=$ 結束在第 $i$ 個數字的 LIS 長度。
* `$dp[i] = 1$ or $\max_{j < i, a[j] < a[i]} \{ dp[j] + 1\}$`

--

#### C++ Example 1

```cpp
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        int n = nums.size();
        vector<int> dp(n, 1);
        vector<int> ways(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    if (dp[i] < dp[j] + 1) {
                        dp[i] = dp[j] + 1;
                        ways[i] = 0;
                    }
                    if (dp[i] == dp[j] + 1) {
                        ways[i] += ways[j];
                    }
                }
            }
        }
        int sum = 0;
        int LISlen = *max_element(dp.begin(), dp.end());
        for (int i = 0; i < n; i++)
            if (dp[i] == LISlen)
                sum += ways[i];
        return sum;
    }
};
```
<!-- .element: class="line-numbers" -->

--

#### C++ Example 2

```cpp
有空現場寫QQ
```

---

### [Fit a word into an alphabet grid](https://codegolf.stackexchange.com/questions/141372/fit-a-word-into-an-alphabet-grid?rq=1)

* Problem Design: What kind of problems you would expect?

![](https://i.stack.imgur.com/yLbE3.jpg)
<!-- .element: style="float:right;height:300px" -->

---

### [Leetcode 646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/)

* You are given $n$ pairs of numbers. In every pair, the first number is always smaller than the second number.
* Now, we define a pair $(c, d)$ can follow another pair $(a, b)$ if and only if $b < c$. Chain of pairs can be formed in this fashion.
* Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.


---

### [Leetcode 354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/description/)

* You have a number of envelopes with widths and heights given as a pair of integers `$(w, h)$`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

* What is the maximum number of envelopes can you Russian doll? (put one inside other)

* Rotation is not allowed.

---

### [Leetcode 873. Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/)

---

### [Leetcode 322. Coin Change](https://leetcode.com/problems/coin-change/description/)

---

### [Leetcode 518. Coin Change 2](https://leetcode.com/problems/coin-change-2/description/)

---

### [Leetcode 403. Frog Jump](https://leetcode.com/problems/frog-jump/description/)

---

### [Leetcode 363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/)

