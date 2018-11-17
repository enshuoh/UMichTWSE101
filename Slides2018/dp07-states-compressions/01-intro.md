
UMTW-SE101 Fall 2018

### 動態規劃《狀態壓縮 DP》

![](https://i1.kknews.cc/SIG=s6389j/2n430003p5367o8so39s.jpg)
<!-- .element: style="height:400px" --><br/>

--

<!-- .slide: data-background="#ABD" -->
### 動態規劃的重點

1. 定義<span class="blue">遞迴函數</span>。
2. 找出<span class="red">遞迴關係</span>。
3. 確定<span class="green">邊界條件</span>。

--

### 什麼是狀態壓縮

* 「狀態」就是遞迴函數的參數，也就是「子問題」。
* 「壓縮」是把我們在解題過程中所有遇到的子問題，用<span class="red">有效率</span>的形式儲存。
    * 這個「有效率」可以是時間上的、可以是空間上的。
    * 目標是為了<span class="blue">有效率地</span>操作並描述「狀態的改變」

--

### 概念

* 溝通
* 描述
* 改變

--

### 例一

* 給定字串 $S$，描述任一子字串(substring)。
* $[i, j]$ <!-- .element: class="fragment" -->

![](images/example1.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例二

* 給定 $n$ 個數字，描述任一子集合(subset)。
* bit strings <!-- .element: class="fragment" -->

![](images/example2.png)
<!-- .element: style="float:right;height:150px" -->

--

### 例三

* 給定一棵樹，描述任一子樹(subtree)。

![](https://uniform.wingzero.tw/assets/images/badge/tw-taipei-lssh.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例四

* 給定一棵樹，描述任一同構子樹。

![](https://www.moedict.tw/%E7%AB%8B%E5%97%A3.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例五

* 給定鋪設一半的水管線路，描述邊界的連通狀況。

![](https://files.cnblogs.com/files/RogerDTZ/ct4.bmp)