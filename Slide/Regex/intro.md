# 正規表達式
## Regular Expression

--

## 什麼是正規表達式？

* **精簡地** 描述一類字串集合的方法。

`[ab]{3}` $= \\{aaa, aab, aba, abb, baa, bab, bba, bbb\\}$


--

## 模式匹配 Pattern Matching

* 利用正規表達式做到模式匹配：從大量的文件資料裡頭，找出我們想要的字句。

--

## 百家爭鳴

* [Regular Expression Engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines)
* 每一家能夠表達的字串集合不盡相同、語法和適用性也稍有不同。
* 不過有一些基本的、共同的要素。

--

## 一點理論、一點歷史

* 怎麼定義「解題」？
* Decision Problems：是非題
* 把輸入想像成一個有限長度的字串，每一個字母來自於一個固定的字母集合 $\Sigma$。


--

## 關於計算模型 I

* Alonzo Church ($\lambda$-calculus, 1936)
* Alan Turing (a-machine, 1936)
* [Church-Turing Thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)

<img src="https://upload.wikimedia.org/wikipedia/en/a/a6/Alonzo_Church.jpg" style="width:350px">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Alan_Turing_Aged_16.jpg/440px-Alan_Turing_Aged_16.jpg" style="width:350px;vertical-align:top">

--

## 關於計算模型 II

* John von Neumann
* 匈牙利數學家，提出計算模型的實作 (1945)

<img src="http://ysfine.com/wigner/neum/vnc01.jpg" style="width: 500px">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Von_Neumann_architecture.svg" style="width: 300px">

--

## 形式語言 Formal Languages

* Stephen Cole Kleene

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Kleene.jpg" style="width:400px">

--

## 串接 Concatination

* 給定兩個字串集合 $A = \\{a_1, a_2, \ldots\\}$, $B = \\{b_1, b_2, \ldots \\}$，則兩個集合的串接定義為
$A\bullet B = \\{a_ib_j\ |\ \forall i, j\\}$

--

## 克里尼之星 Kleene Star

* $A^* = \varepsilon \cup A \cup A^2 \cup A^3 \cup \cdots$
* 註：形式語言就是字串集合 $L\subseteq \Sigma^*$

--

## 正規形式語言 Regular Languages

* 定義：
  - $A = \emptyset$ （空集合）是 Regular
  - $A = \\{\varepsilon\\}$ （空字串）是 Regular
  - 對任意字母 $a\in \Sigma$，$A = \\{a\\}$ 是 Regular
  - 對任意 Regular $A, B$，$A\cup B$ 是 Regular
  - 對任意 Regular $A, B$，$A\bullet B$ 是 Regular
  - 對任意 Regular $A$，$A^*$ 是 Regular

--

## 正規表達式 Regular Expression

* 用一個字串描述「合法的字串集合」
* 單一字元：`a`, `[a-z]`, `[abc]`, `[^abc]`, `.`
* 串接：`abc`
* 聯集：`(first|second|third)`
* Kleene Star：`a*`, `(ab)*`, `[abc]*`, `.*`

--

## 擴充語法 I
### Extended Regular Expression

* 重複 0 次或多次：`($pattern$)*`
* 出現 0 次或 1 次：`($pattern$)?`
* 重複 $n$ 次：`($pattern$){$n$}`
* 重複 $n$ 次到 $m$ 次之間：`($pattern$){$n$,$m$}`

--

## 正規語言範例

* 整數  
  ```
  [+-]?(0|[1-9][0-9]*)
  ```
* [科學計數](http://stackoverflow.com/questions/638565/parsing-scientific-notation-sensibly)   
  ```
  -?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?
  ```
  <!-- .element: style="font-size:40%" -->
* 合法的變數名稱   
  ```
  [A-Za-z_][A-Za-z0-9_]*
  ```
* Email   
  ```
  ([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})
  ```
  <!-- .element: style="font-size:30%;left:-60px;min-width:700px" -->
* [Url](https://mathiasbynens.be/demo/url-regex)

--

<img src="http://www.json.org/number.gif" style="width:700px;background-color:white">

--

## 非正規語言範例
### Non-regular Languages

* 長度是質數的字串
* $\\{\mathtt{a}^n\mathtt{b}^n\\}$
* 同樣的字串貼兩次
* 迴文字串 Palindromes
* 合法括弧字串

--

## Challenges

* [RegexOne - Learn Regular Expression with simple, interactive exercises](https://regexone.com/)
