
UMTW-SE101 Fall 2018

## 動態規劃《填表篇》

萬丈高樓平地起

![](https://images.1111.com.tw/discussPic/85/50951785_50857463.9567466.png)

--

### 回顧

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSAbYvhKu8RGSPBe4NToOg9E_t41fGhtPepv-GlFE_qHNkaOKDm3IZPwv_ucrly9_tG42MZYlgJ3FJo/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

--

![](https://images.1111.com.tw/discussPic/85/50951785_34510577.1958167.png)

--

### 解題思維 Algorithmic Thinking (1/4)

* 枚舉 Enumeration
    * <!-- .element: class="fragment brown" -->
    『你剛用身上所有的零錢買了 $n \le 10^9$ 罐可樂，已知每回收 $514$ 個空瓶可以換得 $87$ 瓶新的可樂。請問你要跟鄰居借多少空瓶，才可以喝到最多的可樂？』
    * <!-- .element: class="fragment" -->
    驗證答案比算出答案簡單太多了 $\Rightarrow$ 逐一考慮所有答案。

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe-UeJcGuTticR6XPv7Rgx2PAfrHc8yM9r_WvyC3B_UuxAZ_TT)
<!-- .element: style="width:20%;float:right;" -->

--

### 解題思維 Algorithmic Thinking (2/4)
* 迭代 Iteration
    * <!-- .element: class="fragment brown" -->
    『你想要把一個長度為 $n$ 的陣列打亂其排列，請問有沒有什麼好的方法？』
    * <!-- .element: class="fragment" -->
    不斷重複做類似的事情，但每一次得到的結果總會越來越接近答案。

[![](https://i.ytimg.com/vi/qbHYV8884Mg/maxresdefault.jpg)](https://t.cj.sina.com.cn/articles/view/6423062596/17ed82844001009289?cre=tianyi&mod=pcpager_fintoutiao&loc=35&r=9&doct=0&rfunc=100&tj=none&tr=9)
<!-- .element: style="width:20%;float:right;" -->

--
### 解題思維 Algorithmic Thinking (3/4)

* 歸納 Induction
    * <!-- .element: class="fragment brown" -->
    『給你一個字串 $S$，你能不能把字串裡面的東西重新排列過，使得任何兩個相鄰的字元都不相同？』
    * <!-- .element: class="fragment" -->
    子問題對了，原本的問題也不錯了。

![](https://image.shutterstock.com/image-photo/hand-showing-introduction-word-through-260nw-172869146.jpg)
<!-- .element: style="width:20%;float:right;" -->

--

### 解題思維 Algorithmic Thinking (4/4)

* 轉化 Reduction
    * <!-- .element: class="fragment brown" -->
    『給你一個二維黑白陣列影像 $A$、以及一個較小的模板 $P$，請找出這個影像中所有模板出現的位置。』
    * <!-- .element: class="fragment" -->
    如果我會解問題 A，那我就會解問題 B。

![](https://cdn-images-1.medium.com/max/1200/1*nsPddn7l4D26NpiLs2nz9A.jpeg)
<!-- .element: style="width:20%;float:right;" -->

--

### 什麼是題目？

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSpPnVXnYRbYvhBRzodrXjd0sG0yo2PV4z77SfqTIis9eni8rmMODv3_r-7T4Sb1QnkCfFDXjQW6jUy/embed?start=false&loop=false&delayms=3000" frameborder="0" width="90%" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

--

### 解題方法 Algorithmic Paradigms

* 分而治之 Divide and Conquer
* <!-- .element: class="brown" -->
動態規劃 Dynamic Programming
* 貪婪法 Greedy Algorithms
* 回溯與搜索 Backtracking and Searching

--



### 費事數列

<img src="https://i.redd.it/5bombjko3fa01.jpg" style="float:right;width:20%"/>

- `$F_0 = 0$`
- `$F_1 = 1$`
- `$F_n = F_{n-1} + F_{n-2}$` (for `$n > 1$`)

<div style="clear:both" />

--

### 遞迴計算費氏數列

```cpp
int Fib(int n) {
    if (n < 2) return n;
    return Fib(n - 1) + Fib(n - 2);
}
```


--
<!-- .slide: data-background="#FDA" -->
### <span style="font-size:90%">Dynamic Programming in a nutshell</span>

* <span style="color:#B72">Step (1):</span>
    Write a recursive algorithm for your problem.
* <span style="color:#B72">Step (2):</span>
    Answer a couple questions:
    - <b>Q1</b>. Does my recursive algorithm solve the <b><i>same subproblems</i></b> numerous times?
    - <b>Q2</b>. How many distinct subproblems are solved in total?
* <img src="https://cdn.bulbagarden.net/upload/thumb/d/d4/Pok%C3%A9mon_Diamond_Pok%C3%A9mon_Pearl_Super_Music_Collection.png/1200px-Pok%C3%A9mon_Diamond_Pok%C3%A9mon_Pearl_Super_Music_Collection.png" style="float:right;width:15%"/>
    <span style="color:#B72">Step (3):</span>
    <div style="display:inline-block;vertical-align:text-top"> If the answer are "yes" and "not that many", <br> fix your algorithm from <span style="color:#B72">Step (1)</span>. </div>


--
<!-- .slide: data-background="#FDA" -->
### <span style="font-size:90%">腦殼裡的動態規劃</span>

* <span style="color:#B72">第 1 步：</span>
    用遞迴方法實作你的程式。
* <span style="color:#B72">第 2 步：</span>
    捫心自問：
    - <b>Q1</b>. 大量重複的<span class="blue">子問題</span>？
    - <b>Q2</b>. 總共有多少不同的子問題要處理？
* <img src="http://w2.tcfsh.tc.edu.tw/uploads/asset/data/55a5d6f374700034a600011f/%E4%B8%AD%E4%B8%80%E4%B8%ADLOGO.jpg" style="float:right;width:15%"/>
    <span style="color:#B72">第 3 步：</span>
    <div style="display:inline-block;vertical-align:text-top"> 若答案分別是「是」或「沒那麼多」, <br> 把<span style="color:#B72">第 1 步</span>的演算法修好。</div>

--
<!-- .slide: data-background="#FDA" -->
### <span style="font-size:90%">腦殼裡的動態規劃</span>

* <span style="color:#B72">第 3 步：</span>
    <div style="display:inline-block;vertical-align:text-top"> 修好你的<span style="color:#B72">第 1 步</span>。</div>
  </span>
* <!-- .element: class="fragment" data-fragment-index="1" -->
    One way: <span style="color:blue">記憶化搜索 <b><i>memoization</i></b></span>
    - 算過的記起來，再次呼叫的時候就直接回傳答案。
* <!-- .element: class="fragment" data-fragment-index="2" -->
    Another way: solve the subproblems <span style="color:blue">自下而上 <b><i>bottom up</i></b></span>
    - 從最小的（潛在會被用到的）子問題開始計算。

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoCUf2Vp0XuRDK9KdjqK5CADnfWXbZ5OB-sXl38l4d21ovR7qc)
<!-- .element: class="fragment" data-fragment-index="1" style="float:right" -->

--

### Memoization & Tabulation

* A memoized Fibonacci algorithm.

```cpp
// Suppose we want to compute Fib(k).
unordered_map<int, int> A;
// Then we define the recursive function and calls Fib(k).
int Fib(int n) {
    if (A.find(n) != A.end()) {
        return A[n];
    }
    if (n < 2) {
        A[n] = n;
    } else {
        A[n] = Fib(n - 1) + Fib(n - 2);
    }
    return A[n];
}
```

--

### Memoization & Tabulation

* A simpler bottom-up version

```cpp
int Fib(int k) {
    // (Optional) Initialize an array of k+1 entries.
    vector<int> A = {0, 1};
    A.resize(k + 1);
    // Compute each recurrence from smallest to k.
    for (int i = 2; i <= k; i++) {
        A[i] = A[i - 1] + A[i - 2];
    }
    return A[k];
}
```

--

<!-- .slide: data-background="#ABD" -->
### 動態規劃的重點

1. 定義<span class="blue">遞迴函數</span>。
2. 找出<span class="red">遞迴關係</span>。
3. 確定<span class="green">邊界條件</span>。
