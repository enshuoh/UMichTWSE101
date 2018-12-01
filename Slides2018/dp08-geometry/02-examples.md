## 實戰演練

Dynamic Programming Examples

---

### [Leetcode 587. Erect the Fence](https://leetcode.com/problems/erect-the-fence)

* There are some trees, where each tree is represented by $(x,y)$ coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

---

### [GCJ 2010 WF P4. Ninjutsu](https://code.google.com/codejam/contest/801485/dashboard#s=p4)

![](https://code.google.com/codejam/contest/images/?image=ninjutsu1.png&p=323102&c=801485)

* 決定一個繩子長度 $\in[0, R]$，使得順時針晃過去的時候可以轉折到最多的卯釘

---

### [CCHEF BALANPOL. Chef and Balanced Polygons](https://www.codechef.com/problems/BALANPOL)

* You are given a convex polygon consisting of n vertices in 2-D plane. You are also given m points, each colored in either red or blue.
* A convex polygon is called _w00t_, if the number of red and blue colored points inside this (inside or on the boundary) are equal.
* You want to find number of _w00t_ convex polygons whose vertices are a subset of the vertices of the given convex polygon.

---

### [CCHEF KOL16K. Chef and Points](https://www.codechef.com/problems/KOL16K)

* 給平面上 $n$ 個點，問能否找到最大的子集合，使得他們從左到右呈現凹函數？

---

### [SGU 315. The Highway Belt](https://codeforces.com/problemsets/acmsguru/problem/99999/315)

* 給 $50$ 條線段，使用其中的一些變成一個多邊形、且這個多邊形圍住原點 (0, 0)。規定從原點出發的射線只能經過這個多邊形一次。請問該多邊形周長最長為何？

---

### Number of points inside triangles

* 給定平面上 `$n$` 個點，任何三個點不共線。現在有 `$Q$` 個問題：對於每一個問題 `$(p_i, p_j, p_k)$`，請回答 `$\triangle p_ip_jp_k$` 三角形內部有多少個點？
* 目標時間 `$O(n^2 + Q)$`。

---

### Largest Area Triangle

* 給定平面上 `$n$` 個點，請在 `$O(n^2)$` 時間內找出面積最大、以這 `$n$` 個點其中三個為頂點的三角形。

---

### Largest Empty Convex Subset

* 給定平面上 `$n$` 個點，任何三個點不共線。找出一個 subset，使得這個 subset 形成的 Convex Hull 內部為空，且這個 Convex Hull 面積越大越好。