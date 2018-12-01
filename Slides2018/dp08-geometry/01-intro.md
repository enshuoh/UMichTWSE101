
UMTW-SE101 Fall 2018

### 動態規劃《計算幾何篇》

![](http://www.shtabook.com.tw/2012.11%E6%9C%88%E5%84%AA%E6%83%A0%E6%B4%BB%E5%8B%95/%E4%BA%BA%E7%94%9F%E5%B9%BE%E4%BD%95.jpg)
<!-- .element: style="height:400px" --><br/>

--

<!-- .slide: data-background="#ABD" -->
### 動態規劃的重點

1. 定義<span class="blue">遞迴函數</span>。
2. 找出<span class="red">遞迴關係</span>。
3. 確定<span class="green">邊界條件</span>。

--

### 計算幾何

* 用電腦處理**<span class="blue">歐幾里得空間</span>**中發生的各種事情XD

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Coord_system_CA_0.svg/250px-Coord_system_CA_0.svg.png)

--

### 基礎建設

* 點 Points
* 線段 Segments
* 平面 Plane
* 圓 Circle

--

### 向量 Vectors

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/3D_Vector.svg/240px-3D_Vector.svg.png)

* 如何計算兩條線段的交點？

![](https://m.media-amazon.com/images/M/MV5BNDM1ZDMwMzItYTc2Mi00MzllLWFjOWItMTQwM2Q4MzdhNzk0XkEyXkFqcGdeQXVyMTY1NzY2NA@@._V1_UY268_CR4,0,182,268_AL_.jpg)<!-- .element: style="float:right; width:150px" -->

--

### 兩個線段交點

![](http://paulbourke.net/geometry/pointlineplane/lineline1.gif)

* 面積法：`$\overline{P_1O}:\overline{OP_2} = \triangle P_1P_4P_3 : \triangle P_2P_3P_4$`

![](https://i.ytimg.com/vi/0LJLokcgQRc/maxresdefault.jpg)<!-- .element: style="float:right;width:300px" -->

--

### 有向三角形與有向面積

![](https://www.techhouse.org/~mdp/midpoint/images/oriented_area.jpg)

![](https://ws3.sinaimg.cn/large/6af89bc8gw1f8pq2gkyzaj206h05r0sz.jpg)<!-- .element: style="float:right;width:200px" -->

--


### 簡單多邊形 Simple Polygons

![](https://rechneronline.de/pi/img/polygon.png)
![](https://www.york.cuny.edu/~malk/microworld29.jpg)

* Q: 如何判斷儲存的多邊形是「順時針序」還是「逆時針序」？

![](https://i.pinimg.com/236x/ee/d3/1d/eed31d9f909127fcbb453c5d6b800ab1--animal-illustrations-design-illustrations.jpg)<!-- .element: style="float:right;width:150px" -->

--

### 凸包 Convex Hulls

![](https://miro.medium.com/max/1354/1*F4IUmOJbbLMJiTgHxpoc7Q.png)

![](https://i.stack.imgur.com/OvZiN.png)<!-- .element: style="float:right;width:200px" -->

--

### 凸包的若干算法

* [賈維斯散步 Jarvis' March](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm)
* [葛拉罕掃描法 Graham's Scan](https://en.wikipedia.org/wiki/Graham_scan)
* 上包和下包法 (Double Hull)
* [橡皮筋縮放法(物理)](https://www.cs.auckland.ac.nz/~rklette/talks/07_Kolkata.pdf)
* 分而治之法 (QuickHull)

![](images/rubberband.png) <!-- .element: style="float:right;width:200px" -->