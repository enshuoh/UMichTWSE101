# Object, Class, Instance

--

## Object
- object由一系列的操作(operations)，以及相關的狀態(state)所組成
- 操作可能影響其儲存的狀態
- 操作（operations）、方法（methods）和行為（behaviors）可以看作同義詞。
- 理想上一個object的狀態只能透過已定義的操作去改變

--

## Class
- 定義Object的藍圖，用於定義、了解Object的操作與狀態

--

## Instance
- Instance是我們根據一個Class的定義所產生，獨一無二的object

--

## 現實例子
- 我們以Class定義馬，馬會跑、有顏色、有體力條
- 跑 -> 行為 (可能影響體力條)
- 顏色 -> 狀態

--

## Instance
- 白馬是馬 (Instance 是 Object)
- 馬是白馬 (Object != Instance)
- Object強調的是，抽象化看待的實體資料結構與程式碼
  - 實體資料結構與程式碼 -> 存在記憶體、硬碟裡的一堆數字
  - 抽象化 -> 我們可以以行為、狀態去描述這堆數字
- Instance強調的是，這是個根據某Class所產生出，獨特的Object

---
# 多型 Polymorphism

--

## 多型的定義
- 相同的訊息傳遞給不同的物件，進而產生出不同的行為反應
- 訊息的意義是由接收者來解釋，而非發出者來解釋
  - 把接收者換成不同的Instance，會導致不同的結果

--

## 範例
- 請問現在幾點？
- 問台灣人
- 問美國人
- 問狗

--

## 如何達到多型的效果？
- 靜態語言
  - C++, Java
  - 用繼承
- 動態語言
  - python
  - 可以不用繼承

--

## 重載(Overloading)是不是多型？
- General概念上：是
- 但是在OOP當中，不是
- OOP的polymorphism通常指的就是動態多型
  - 動態多型：類繼承機制和虛擬函式機制生效於執行期
    - Method overriding
  - 靜態多型：關聯處理於編譯期而非執行期，因此被稱為「靜態」
    - Method overloading
    - Operator overloading
- 細節請參考Wiki

---
# 繼承 Inheritance

--

## 繼承的效果
- 如果B繼承A，則A會變成B的一部份 (DNA傳承)
- 要達到一樣的目標，一定要使用繼承嗎?

--

## 名詞解釋
- Generalization：一般化
  - 把不同的classes共同的特性抽離出來集中放到一個class中
  - 讓原本的那些classes去繼承這個新的class
  - 過程叫做generalization
  - botton-up的方式
  - 好處，需要被維護的code變少
  - 壞處，增加相依性
- Specialization：特殊化
  - 先找到一個與要新增的class B 功能類似的既存class A
  - 讓B先繼承A後，在A身上增加專屬於他自己的行為或資料
  - 違反了Liskov Substitution Principle

--

## 名詞解釋
- Ancestors：祖先
  - 在一個繼承架構中，某個class A之上的所有classes稱之為A的祖先
  - 又稱作superclasses（父類別）
- Descendants：後代
  - 在一個繼承架構中，某個class A之下的所有classes稱之為A的後代
  - 又稱作subclasses（子類別）

--

## 名詞解釋
- Direct descendant
  - B 繼承 A -> B是A的Direct descendant
  - 又稱做child
- Direct ancestor
  - B 繼承 A -> A是B的Direct descendant
  - 又稱做parent
- Abstract classes：抽象類別
  - 目的就是為了要讓其他類別繼承用的
  - 實務上：無法產生instance的class就稱之為abstract class

--

## 使用的時機
- Reuse
  - 假如只是想要Reuse，composition或許是比較好的做法
- Subtyping
  - 一個類別（class）被視為某個型別（type）的實作
  - 通常用於擴充功能
- Specialization
- Conceptual
