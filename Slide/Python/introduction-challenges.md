# Section 1
## Introduction Challenges

![imgur](http://i.imgur.com/s77tH2H.png)

--

## Say "Hello, World!" With Python

* 學習重點：如何使用 print function

```py
print("Hello, World!")
```

* 思考重點：這麼做可以把字串印到螢幕上（我們把這裡的螢幕視為<font color="yellow">標準輸出 stdout</font>）

--

## Reading Raw Input

* 學習重點：如何使用 input function 讀入字串

```py
s = input()  # 先從鍵盤(stdin) 讀入字串
print(s)     # 直接輸出到螢幕(stdout) 上面
```

--

## Python If-Else （提示篇）

* [題目連結](https://www.hackerrank.com/challenges/py-if-else)
* 學習重點：
  - `if`, `elif`, `else`
  - 記得判斷式後面要加冒號、內容要縮排
* 他已經幫你寫好輸入了，可以直接使用變數 $N$：
```py
import sys
N = int(input().strip())
```
* 觀察：`int()` 是一個可以把字串轉換成整數的方法（這叫做 <font color="yellow">Type Conversion</font>）

--

## Python If-Else （解答篇）

```py
if N%2==1:
    print("Weird")
elif N >= 6 and N <= 20:
    print("Weird")
else:
    print("Not Weird")
```

* 觀察
  - 如果有 AND/OR 請記得直接寫 `and`/`or`，不像其他語言有奇怪的符號～
  - `N%2` 代表的是「計算 $N$ 除以 $2$ 的餘數」


--

## Arithmetic Operators

```py
a = int(input())  # 輸入 a
b = int(input())  # 輸入 b
```

```py
print(a + b)
print(a - b)
print(a * b)
```

--

## Python: Division

* 整數除法：捨棄任何餘數的除法計算
* 浮點數除法：會算出小數部分

首先讀入兩個數，然後利用 `//` 和 `/` 計算。

```py
print(a // b)  # 整數除法
print(a / b)   # 浮點數除法
```

--

## Loops

* [題目連結](https://www.hackerrank.com/challenges/python-loops)
* 學習重點：`for` 迴圈、或是 `while` 迴圈。

```py
for i in range(0, N):
    print(i * i)
```

* 觀察：`range(0, N)` 會產生一個 $0$ 到 $N-1$ 的 list

--

## Write a function

* [題目連結](https://www.hackerrank.com/challenges/write-a-function)
* 學習重點：函式裡頭記得要縮排！

```py
if ((year%4==0 and year%100!=0)
        or year%400==0):
    # 把回傳值設為 True
    leap = True
```

* 觀察：`True` 和 `False` 是個「常量」，要注意大小寫！
* 備註：
  - 進行運算時，True 和 False 會被當成 1 (或 0) 計算。
  - 跨行程式碼建議摺疊至運算式中。

--

## Print Function（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/python-print)
* 學習重點：`print()` 函式一次都印一行，要怎麼做才能把全部東西塞在同一行？
* 提示：
  - 方法一：翻翻 [Document](https://docs.python.org/3/library/functions.html#print)，有沒有什麼參數可以設定
  - 方法二：把所有數字轉成字串以後接在一起

--

## Print Function（解答篇）

```py
for i in range(1, N+1):
    print(i, end="")
```

* <font color="red">[看不懂請跳過]</font>進階用法：如果你會用 `string`, `map`, `join`，也可以把它全部接起來。

```py
print("".join(map(str, range(1, N+1))))
```


--

<div class="pyro">
<div class="before"></div>

# 恭喜你
## 第一階段完成

[請按 $\rightarrow$ 進入第二大關]

<div class="after"></div>
</div>

<style>

.pyro > .before, .pyro > .after {
  position: absolute;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  box-shadow: 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff, 0 0 #fff;
  -moz-animation: 1s bang ease-out infinite backwards, 1s gravity ease-in infinite backwards, 5s position linear infinite backwards;
  -webkit-animation: 1s bang ease-out infinite backwards, 1s gravity ease-in infinite backwards, 5s position linear infinite backwards;
  -o-animation: 1s bang ease-out infinite backwards, 1s gravity ease-in infinite backwards, 5s position linear infinite backwards;
  -ms-animation: 1s bang ease-out infinite backwards, 1s gravity ease-in infinite backwards, 5s position linear infinite backwards;
  animation: 1s bang ease-out infinite backwards, 1s gravity ease-in infinite backwards, 5s position linear infinite backwards;
}

.pyro > .after {
  -moz-animation-delay: 1.25s, 1.25s, 1.25s;
  -webkit-animation-delay: 1.25s, 1.25s, 1.25s;
  -o-animation-delay: 1.25s, 1.25s, 1.25s;
  -ms-animation-delay: 1.25s, 1.25s, 1.25s;
  animation-delay: 1.25s, 1.25s, 1.25s;
  -moz-animation-duration: 1.25s, 1.25s, 6.25s;
  -webkit-animation-duration: 1.25s, 1.25s, 6.25s;
  -o-animation-duration: 1.25s, 1.25s, 6.25s;
  -ms-animation-duration: 1.25s, 1.25s, 6.25s;
  animation-duration: 1.25s, 1.25s, 6.25s;
}

@-webkit-keyframes bang {
  to {
    box-shadow: 127px -40.66667px #ff9900, -215px -208.66667px #001eff, 33px -48.66667px #73ff00, 173px 8.33333px #ff0062, -62px -185.66667px #a600ff, -191px -289.66667px #d5ff00, 172px 83.33333px #00a6ff, 239px -222.66667px #ff0066, 34px -100.66667px #002bff, 98px 12.33333px #b700ff, 232px -6.66667px #00ff11, 169px -83.66667px #1e00ff, -164px -219.66667px #c8ff00, -119px -353.66667px #ff8800, 185px 5.33333px #005eff, 0px -197.66667px #88ff00, -41px -14.66667px #00ff88, -39px -251.66667px #00ff91, -68px -123.66667px #00b3ff, 223px -37.66667px #f7ff00, 183px -230.66667px #ff0033, 217px -210.66667px #ffe600, 238px 20.33333px #1eff00, -189px -255.66667px #ff2200, 65px -361.66667px #ff6200, -213px -220.66667px #ffd500, 113px -353.66667px #ff4d00, 244px -414.66667px #00ffa2, -9px -223.66667px #ff0062, -105px -230.66667px #b3ff00, -236px -55.66667px #00f2ff, 209px -388.66667px #fffb00, 11px -183.66667px #a600ff, -43px -164.66667px #00ffea, -88px -162.66667px #e600ff, -161px -330.66667px #00e1ff, -97px -145.66667px #002fff, 206px -321.66667px #88ff00, 15px -313.66667px #6200ff, -164px -293.66667px #ff1100, 164px -164.66667px #008cff, -88px -6.66667px #1500ff, 133px -387.66667px #0dff00, -58px -60.66667px #ff00c8, 189px 25.33333px #00ff37, -74px 80.33333px #ff0004, 213px -208.66667px #ff4400, -110px -87.66667px #6aff00, -231px -345.66667px #4800ff, -200px -321.66667px #00ffb7, -154px -411.66667px #91ff00;
  }
}
@-moz-keyframes bang {
  to {
    box-shadow: 127px -40.66667px #ff9900, -215px -208.66667px #001eff, 33px -48.66667px #73ff00, 173px 8.33333px #ff0062, -62px -185.66667px #a600ff, -191px -289.66667px #d5ff00, 172px 83.33333px #00a6ff, 239px -222.66667px #ff0066, 34px -100.66667px #002bff, 98px 12.33333px #b700ff, 232px -6.66667px #00ff11, 169px -83.66667px #1e00ff, -164px -219.66667px #c8ff00, -119px -353.66667px #ff8800, 185px 5.33333px #005eff, 0px -197.66667px #88ff00, -41px -14.66667px #00ff88, -39px -251.66667px #00ff91, -68px -123.66667px #00b3ff, 223px -37.66667px #f7ff00, 183px -230.66667px #ff0033, 217px -210.66667px #ffe600, 238px 20.33333px #1eff00, -189px -255.66667px #ff2200, 65px -361.66667px #ff6200, -213px -220.66667px #ffd500, 113px -353.66667px #ff4d00, 244px -414.66667px #00ffa2, -9px -223.66667px #ff0062, -105px -230.66667px #b3ff00, -236px -55.66667px #00f2ff, 209px -388.66667px #fffb00, 11px -183.66667px #a600ff, -43px -164.66667px #00ffea, -88px -162.66667px #e600ff, -161px -330.66667px #00e1ff, -97px -145.66667px #002fff, 206px -321.66667px #88ff00, 15px -313.66667px #6200ff, -164px -293.66667px #ff1100, 164px -164.66667px #008cff, -88px -6.66667px #1500ff, 133px -387.66667px #0dff00, -58px -60.66667px #ff00c8, 189px 25.33333px #00ff37, -74px 80.33333px #ff0004, 213px -208.66667px #ff4400, -110px -87.66667px #6aff00, -231px -345.66667px #4800ff, -200px -321.66667px #00ffb7, -154px -411.66667px #91ff00;
  }
}
@-o-keyframes bang {
  to {
    box-shadow: 127px -40.66667px #ff9900, -215px -208.66667px #001eff, 33px -48.66667px #73ff00, 173px 8.33333px #ff0062, -62px -185.66667px #a600ff, -191px -289.66667px #d5ff00, 172px 83.33333px #00a6ff, 239px -222.66667px #ff0066, 34px -100.66667px #002bff, 98px 12.33333px #b700ff, 232px -6.66667px #00ff11, 169px -83.66667px #1e00ff, -164px -219.66667px #c8ff00, -119px -353.66667px #ff8800, 185px 5.33333px #005eff, 0px -197.66667px #88ff00, -41px -14.66667px #00ff88, -39px -251.66667px #00ff91, -68px -123.66667px #00b3ff, 223px -37.66667px #f7ff00, 183px -230.66667px #ff0033, 217px -210.66667px #ffe600, 238px 20.33333px #1eff00, -189px -255.66667px #ff2200, 65px -361.66667px #ff6200, -213px -220.66667px #ffd500, 113px -353.66667px #ff4d00, 244px -414.66667px #00ffa2, -9px -223.66667px #ff0062, -105px -230.66667px #b3ff00, -236px -55.66667px #00f2ff, 209px -388.66667px #fffb00, 11px -183.66667px #a600ff, -43px -164.66667px #00ffea, -88px -162.66667px #e600ff, -161px -330.66667px #00e1ff, -97px -145.66667px #002fff, 206px -321.66667px #88ff00, 15px -313.66667px #6200ff, -164px -293.66667px #ff1100, 164px -164.66667px #008cff, -88px -6.66667px #1500ff, 133px -387.66667px #0dff00, -58px -60.66667px #ff00c8, 189px 25.33333px #00ff37, -74px 80.33333px #ff0004, 213px -208.66667px #ff4400, -110px -87.66667px #6aff00, -231px -345.66667px #4800ff, -200px -321.66667px #00ffb7, -154px -411.66667px #91ff00;
  }
}
@-ms-keyframes bang {
  to {
    box-shadow: 127px -40.66667px #ff9900, -215px -208.66667px #001eff, 33px -48.66667px #73ff00, 173px 8.33333px #ff0062, -62px -185.66667px #a600ff, -191px -289.66667px #d5ff00, 172px 83.33333px #00a6ff, 239px -222.66667px #ff0066, 34px -100.66667px #002bff, 98px 12.33333px #b700ff, 232px -6.66667px #00ff11, 169px -83.66667px #1e00ff, -164px -219.66667px #c8ff00, -119px -353.66667px #ff8800, 185px 5.33333px #005eff, 0px -197.66667px #88ff00, -41px -14.66667px #00ff88, -39px -251.66667px #00ff91, -68px -123.66667px #00b3ff, 223px -37.66667px #f7ff00, 183px -230.66667px #ff0033, 217px -210.66667px #ffe600, 238px 20.33333px #1eff00, -189px -255.66667px #ff2200, 65px -361.66667px #ff6200, -213px -220.66667px #ffd500, 113px -353.66667px #ff4d00, 244px -414.66667px #00ffa2, -9px -223.66667px #ff0062, -105px -230.66667px #b3ff00, -236px -55.66667px #00f2ff, 209px -388.66667px #fffb00, 11px -183.66667px #a600ff, -43px -164.66667px #00ffea, -88px -162.66667px #e600ff, -161px -330.66667px #00e1ff, -97px -145.66667px #002fff, 206px -321.66667px #88ff00, 15px -313.66667px #6200ff, -164px -293.66667px #ff1100, 164px -164.66667px #008cff, -88px -6.66667px #1500ff, 133px -387.66667px #0dff00, -58px -60.66667px #ff00c8, 189px 25.33333px #00ff37, -74px 80.33333px #ff0004, 213px -208.66667px #ff4400, -110px -87.66667px #6aff00, -231px -345.66667px #4800ff, -200px -321.66667px #00ffb7, -154px -411.66667px #91ff00;
  }
}
@keyframes bang {
  to {
    box-shadow: 127px -40.66667px #ff9900, -215px -208.66667px #001eff, 33px -48.66667px #73ff00, 173px 8.33333px #ff0062, -62px -185.66667px #a600ff, -191px -289.66667px #d5ff00, 172px 83.33333px #00a6ff, 239px -222.66667px #ff0066, 34px -100.66667px #002bff, 98px 12.33333px #b700ff, 232px -6.66667px #00ff11, 169px -83.66667px #1e00ff, -164px -219.66667px #c8ff00, -119px -353.66667px #ff8800, 185px 5.33333px #005eff, 0px -197.66667px #88ff00, -41px -14.66667px #00ff88, -39px -251.66667px #00ff91, -68px -123.66667px #00b3ff, 223px -37.66667px #f7ff00, 183px -230.66667px #ff0033, 217px -210.66667px #ffe600, 238px 20.33333px #1eff00, -189px -255.66667px #ff2200, 65px -361.66667px #ff6200, -213px -220.66667px #ffd500, 113px -353.66667px #ff4d00, 244px -414.66667px #00ffa2, -9px -223.66667px #ff0062, -105px -230.66667px #b3ff00, -236px -55.66667px #00f2ff, 209px -388.66667px #fffb00, 11px -183.66667px #a600ff, -43px -164.66667px #00ffea, -88px -162.66667px #e600ff, -161px -330.66667px #00e1ff, -97px -145.66667px #002fff, 206px -321.66667px #88ff00, 15px -313.66667px #6200ff, -164px -293.66667px #ff1100, 164px -164.66667px #008cff, -88px -6.66667px #1500ff, 133px -387.66667px #0dff00, -58px -60.66667px #ff00c8, 189px 25.33333px #00ff37, -74px 80.33333px #ff0004, 213px -208.66667px #ff4400, -110px -87.66667px #6aff00, -231px -345.66667px #4800ff, -200px -321.66667px #00ffb7, -154px -411.66667px #91ff00;
  }
}
@-webkit-keyframes gravity {
  to {
    transform: translateY(200px);
    -moz-transform: translateY(200px);
    -webkit-transform: translateY(200px);
    -o-transform: translateY(200px);
    -ms-transform: translateY(200px);
    opacity: 0;
  }
}
@-moz-keyframes gravity {
  to {
    transform: translateY(200px);
    -moz-transform: translateY(200px);
    -webkit-transform: translateY(200px);
    -o-transform: translateY(200px);
    -ms-transform: translateY(200px);
    opacity: 0;
  }
}
@-o-keyframes gravity {
  to {
    transform: translateY(200px);
    -moz-transform: translateY(200px);
    -webkit-transform: translateY(200px);
    -o-transform: translateY(200px);
    -ms-transform: translateY(200px);
    opacity: 0;
  }
}
@-ms-keyframes gravity {
  to {
    transform: translateY(200px);
    -moz-transform: translateY(200px);
    -webkit-transform: translateY(200px);
    -o-transform: translateY(200px);
    -ms-transform: translateY(200px);
    opacity: 0;
  }
}
@keyframes gravity {
  to {
    transform: translateY(200px);
    -moz-transform: translateY(200px);
    -webkit-transform: translateY(200px);
    -o-transform: translateY(200px);
    -ms-transform: translateY(200px);
    opacity: 0;
  }
}
@-webkit-keyframes position {
  0%, 19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%, 39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%, 59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%, 79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%, 99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
@-moz-keyframes position {
  0%, 19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%, 39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%, 59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%, 79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%, 99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
@-o-keyframes position {
  0%, 19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%, 39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%, 59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%, 79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%, 99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
@-ms-keyframes position {
  0%, 19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%, 39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%, 59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%, 79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%, 99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
@keyframes position {
  0%, 19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%, 39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%, 59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%, 79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%, 99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
</style>
