# 編程範型
## Programming paradigm

--

## What is Programming paradigm?
* Programming paradigm是一種寫程式的風格或方法
* 「有些」程式語言是被設計為，讓某種或多種Paradigm方便使用

--
## Why?
* 針對不同問題，有所適合不同的方法
* Programming paradigm就像是寫程式的心法
  * 根據特定流程、方式去思考，簡化思考難度
  * 避免常見問題發生
* 選擇適合的Programming paradigm解決問題
* 瞭解程式語言適合使用什麼Programming paradigm

--

## 常見分類
* Imperative (指令式)
  * Structured (結構化)
    * Procedural （程序式)
    * Object Oriented (物件導向)
* Declarative (宣告式)
  * Functional (函數式)

--

## Imperative
- 電腦的硬體工作幾乎是指令式
- 每一個行為都是一個指令
- 現實例子: 食譜
- 易於理解、想像

--

```
i = 0
sum = 0
start:
  if i >= 5 goto end
  sum = sum + i
  if i < 5 goto next
next:
  i = i + 1
  goto start
end:
  return sum
```

--

## Imperative
- 簡單、有效率
- 支援的硬體設計簡單
- Code複雜、難寫

--

## Structured
- 引進
  - Subroutine
    - procedure
    - function
    - method
    - callable Unit
  - 以迴圈取代goto
    - while
    - for

--
## Structured
```
sum = 0
for(i=0;i<5;++i)
  sum = sum+i;
return sum;
```

--

## Structured
- 高階語言通常支援
  - 運算語句
  - 迴圈語句
  - 條件分支語句 (if)
  - 無條件分支語句 (goto)
    - 有時會刻意不支援goto
    - 強迫使用者使用其他方式取代goto
    - 例如使用迴圈及函式呼叫
    - Go To Statement Considered Harmful

--
## Procedural
- 由結構化衍伸
- 主要採取Procedure call和Function call進行流程控制
- 現在大多的程式語言都支援Procedural Programming

--

## Object Oriented
- 由結構化衍伸
- 今天的重點，晚點再講

```
for number in numbers:
  sum.add(number);
return sum;
```

--

## Declarative
- 與Imperative相反
- 告訴電腦想要的目標，而非流程
  - 告訴電腦要算「什麼」，而非「如何」計算
- 通常沒有迴圈、Assign
- 很多Domain Specific Languages(DSLs)都是這種形式
- 現實例子：販賣機、3D列印
```
select sum(number)
from numbers
where number < 5
```

--

## Functional
- 連續運用簡單的函數(function)
- 結果不斷漸進為最終目標
- 很多Big Data的計算Framework常用到相關概念

--

## 小結
- 一個程式語言可能寫出不同種Paradigm
  - C++支援
    - Unstructured Imperative
    - structured Imperative
  - Python
    - 平常是 Imperative
    - Lambda -> Functional
    - 也能寫Object-Oriented
- 了解不同的程式語言適合哪種Paradigm很重要
- 了解每種Paradigm的優缺點也很重要
- 靈活運用不同的Paradigm以利解決問題
