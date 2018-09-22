## 實戰演練

Dynamic Programming Examples

--

### [Leetcode 221. Maximal Square](https://leetcode.com/problems/maximal-square/description/)

* Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

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

--

#### Python Example

```py

```

---

### [Leetcode 85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/)

* Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

--



--

### [Leetcode 746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

* On a staircase, the $i$-th step has some non-negative cost `cost[i]` assigned (0 indexed).
* Once you pay the cost, you can either climb **one** or **two** steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

--

### Longest Common Subsequence

* 給你兩個字串，問你他們的<span class="blue">共同最長部份子序列</span>的長度為何？

--

### [Leetcode 516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/)

* Given a string $s$, find the longest palindromic subsequence's length in $s$. You may assume that the maximum length of $s$ is 1000.

--

### [Leetcode 132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/description/)

* Given a string $s$, partition $s$ such that every substring of the partition is a palindrome.
* Return the minimum cuts needed for a palindrome partitioning of $s$.

--


### [Leetcode 646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/)

* You are given $n$ pairs of numbers. In every pair, the first number is always smaller than the second number.
* Now, we define a pair $(c, d)$ can follow another pair $(a, b)$ if and only if $b < c$. Chain of pairs can be formed in this fashion.
* Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

--

### [Leetcode 873. Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/)
