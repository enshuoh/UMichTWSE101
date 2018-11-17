
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

* 資訊
    * A 和 B 手上都有相同的 <span class="green">資訊</span>（輸入）。
* 狀態
    * A 想要告訴 B 關於這資訊的某個相關的狀態<span class="red">描述</span>
* 關聯
    * B 想要告訴 A，與剛才收到的狀態有<span class="blue">關聯</span>的其他狀態。

--

### 例一

* 資訊：字串 $S$
* 狀態：任何一個連續的子字串 (substring)
* 關聯：把這個子字串的第一個或最後一個字母去掉


![](images/example1.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例二

* 資訊：$n$ 個數字
* 狀態：描述任一子集合 (subset)
* 關聯：從這個子集合中去掉任一個數值

![](images/example2.png)
<!-- .element: style="float:right;height:150px" -->

--

### 例三

* 資訊：一棵二元樹 $T$
* 狀態：描述任一子樹 (subtree)
* 關聯：這個子樹的子樹

![](https://uniform.wingzero.tw/assets/images/badge/tw-taipei-lssh.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例四

* 資訊：一棵二元樹 $T$
* 狀態：描述任一子樹 (subtree)
* 關聯：與這個子樹同構的所有子樹

![](https://www.moedict.tw/%E7%AB%8B%E5%97%A3.png)
<!-- .element: style="float:right;height:200px" -->

--

### 例五

* 資訊：$n\times n$ 大小的棋盤，每一格有一片拼圖，依照由上而下、由左至右的順序編號 $1, 2, \ldots, n\times n$。
* 狀態：鋪滿前 $k$ 塊拼圖以後的邊界狀況。  
[![](https://bbsmax.ikafan.com/static/L3Byb3h5L2h0dHAvYWNtLmhkdS5lZHUuY24vZGF0YS9pbWFnZXMvQzM0OC0xMDA0LTIuanBn.jpg)](https://www.bbsmax.com/A/rV57MaBqzP/)
* 關聯：鋪滿前 $k+1$ 塊拼圖以後的邊界狀況。

--

### 例六

