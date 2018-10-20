## 實戰演練

Dynamic Programming Examples

---

### [Leetcode 321. Create Maximum Number](https://leetcode.com/problems/create-maximum-number/description/)

* Given two arrays of length $m$ and $n$ with digits `0`-`9` representing two numbers. Create the maximum number of length $k \le m + n$ from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the $k$ digits.

---

### [Leetcode 552. Students Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/description/)

* Given a positive integer $n$, return the number of all possible attendance records with length $n$, which will be regarded as rewardable. The answer may be very large, return it after mod $10^9 + 7$.
* A student attendance record is a string that only contains the following three characters:
  * `A` : Absent.
  * `L` : Late.
  * `P` : Present.
* A record is regarded as rewardable if it doesn't contain more than one `A` (absent) or more than two continuous `L` (late).

---

### [Leetcode 312. Burst Balloons](https://leetcode.com/problems/burst-balloons/description/)

* Given $n$ balloons, indexed from $0$ to $n-1$. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon $i$ you will get `nums[$left$] $\times$ nums[$i$] $\times$ nums[$right$]` coins. Here left and right are adjacent indices of $i$. After the burst, the left and right then becomes adjacent.
* Find the maximum coins you can collect by bursting the balloons wisely.