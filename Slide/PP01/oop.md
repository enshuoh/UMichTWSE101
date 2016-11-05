# Object-Oriented Programming

--

## 物件導向程式設計簡介
- 由Structured衍生
- 是一種Paradigm也是一種開發方式
- 以物件(Object)為基礎
- 重複使用code
- 提升code的靈活性、可擴充性

--

## 概念
- 程式由各種獨立的Object所組成
- 程式的執行=物件彼此之間互動
- 什麼是類別(Class)？什麼是物件(Object)？
  - 我們平常寫的是類別
  - 使用的是物件
- 封裝性、繼承、多型與抽象化

--

## Class
- 物件的藍圖、設計
- 定義物件的抽象特點，包括
  - 物件的屬性
  - 物件的行為 (method)

--

```python
class Dog:
    def __init__(self, name,
                 height, weight, age):
        self.name = name
        self.kind = 'husky'
        self.height = height
        self.weight = weight
        self.age = age

```

--

```java
public class Dog{
  String name;
  String kind;
  float height;
  float weight;
  int age;
  public Dog(String name, float height,
             float weight, int age){
    this.name = name;
    this.height = height;
    ...
  }
}
```

--

## Object
- Class的實際存在
- 根據Class產生出來的實例(Instance)
- Object vs Instance

```python
jimmy = Dog("Jimmy", 10,100,10)
wei = Dog("Wei", 100, 10, 5)
```

--

## 互動方式
- 以物件之間訊息的傳遞驅動程式
- 接收訊息、處理訊息、傳出訊息會導致不同狀況發生

```python
jimmy.bite(wei)
```

--
## Encapsulation 封裝性
- 隱藏物件的實作細節，只開放用得到的訊息傳遞機制
- 優點
  - 方便合作開發
  - 保留替換的彈性
  - 安全性
- 缺點
  - 不知道裡面到底發生什麼事，很可怕
  - 內部造成外部問題

```
def bite(self, dog):
  self.open_month()
  dog.hurt(self.strength)
  self.close_month()
```

--

## Inheritance 繼承
- 有些狀況下，某些類型可能屬於其他類型的子類別
  - 狗是動物
  - 哈士奇是狗
- 有些屬性跟方法是相同的
  - 人跟狗都是動物都有身高、體重、年齡
- 相通的方法可能會根據不同的類別有差異
  - 人是動物、狗也是動物
  - 人用兩隻腳走、狗用四隻腳走
- 重複使用代碼

```
class Husky(Dog):
  def isStupid(self):
    return True
```
--

## Polymorphism 多型
- 看似相同的東西，在不同的狀況下產生不同的結果
- 主要分為兩種
  - Override 覆寫
    - 子類別繼承父類別後可以改寫父類別的方法
    - 呼叫
  - Overload 多載
    - 同樣名字的函數，給予不同的參數時產生不同的行為
--

## Abstraction 抽象化
- 一個物件可以視使用需求，被視為不同的東西
- 舉例：
  - 人是動物，人的走路通常是兩隻腳
  - 當需要讓人用四肢走路，我們也可以把它當動物
- 小結：
  - Python支援部份的OOP，但是不適合完全套用OOP

--

## 較適合OOP的語言
- Java
- C++
- C#

--

## 進階觀念
- 物件導向程式設計五大原則：SOLID
- S: Single Responsibility Principle
- O: Open-Closed Principle
- L: Liskov’s Substitution Principle
- I: The Interface Segregation Principle
- D: The Dependency Inversion Principle

--

## 練習時間
- 請寫出一個銀行帳戶的類別
- 支援
  - deposit(amount)
  - withdraw(amount)
  - print_deposit()

--
## 練習時間 2
- 寫出一個銀行帳戶的類別
- 支援
  - withdraw(amount)
    - 當銀行內的金額小於固定金額時，無法提領並印出提醒訊息
