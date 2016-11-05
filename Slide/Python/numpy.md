# Section 3
## Numpy

矩陣操作、數值工具

--

## 預備知識：浮點數

* 在有限的二進位底下，儘可能逼近想要表達的數字。

--

## Arrays（提示篇）

* [題目連結](https://www.hackerrank.com/challenges/np-arrays)
* 給你一個浮點數陣列，請你輸出反過來的陣列。
* 方便的提示：`numpy` 會自動幫你轉換型別！
```python
numpy.array([1, '2', 3.0], float)
# array([ 1.,  2.,  3.])
```
<!-- .element: style="font-size:50%" -->
* 要怎麼把陣列反過來？


--

## Arrays（解答篇）

```Python
A = input().split()
A = numpy.array(A, float)[::-1]
print(A)
```

--

## Shape and Reshape

* [題目連結](https://www.hackerrank.com/challenges/np-shape-reshape)
* 輸入 9 個數字，輸出一個 $3\times 3$ 矩陣。

--

## Shape and Reshape（解答篇）

```python
A = numpy.array(input().split(), int)
print(numpy.reshape(A, (3, 3)))
```

--

## Transpose and Flatten

* [題目連結](https://www.hackerrank.com/challenges/np-transpose-and-flatten)
* 輸入一個 $N\times M$ 矩陣，請輸出其轉置矩陣與攤平（接成一維）後的結果。

--

## Transpose and Flatten（解答篇）

```python
N, M = map(int, input().split())
A = [input().split() for _ in range(N)]
A = numpy.array(A, int)
print(A.transpose())
print(A.flatten())
```

--

## Concatenate

* [題目連結](https://www.hackerrank.com/challenges/np-concatenate)
* 輸入兩個矩陣，大小分別是 $N\times P$ 和 $M\times P$，請把兩個矩陣接起來以後輸出。

--

## Concatenate（解答篇）

```python
N, M, P = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(M)], int)
print(numpy.concatenate([A, B], axis=0))
```
<!-- .element: style="font-size:36%" -->

--

## Zeroes and Ones

* [題目連結](https://www.hackerrank.com/challenges/np-zeros-and-ones)
* 給你一個矩陣的大小（List of dimensions），請輸出一個全 0 矩陣或全 1 矩陣。
  * 記得要用整數形式輸出。

--

## Zeroes and Once（解答篇）

```python
N = list(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))
```

--

## Eye and Identity

* [題目連結](https://www.hackerrank.com/challenges/np-eye-and-identity)
* 輸出一個矩陣，使得主對角線上都是 $1$、其他都是 $0$。

--

## Eye and Identity（解答篇）

```python
N, M = map(int, input().split())
print(numpy.eye(N, M))
```

--

## Array Arithmetics

* [題目連結](https://www.hackerrank.com/challenges/np-array-mathematics)
* 給你兩個相同大小的矩陣，請輸出他們逐項的加、減、乘、除、模、冪等運算。

--

## Array Arithmetics（解答篇）

```python
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
```
<!-- .element: style="font-size:36%" -->

--

## Floor, Ceil and Rint

* [題目連結](https://www.hackerrank.com/challenges/floor-ceil-and-rint)
* 無條件捨去、無條件近位、四捨五入（0.5 取至偶數）。

--

## Floor, Ceil and Rint（解答篇）

```python
A = numpy.array(input().split(), float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
```

--

## Sum and Prod

* [題目連結](https://www.hackerrank.com/challenges/np-sum-and-prod)
* 給你一個 $N\times M$ 矩陣，請你先計算每個直行 (axis = 0) 的總和，然後計算並輸出這些總和的乘積。

--

## Sum and Prod（解答篇）

```python
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.product(numpy.sum(A, axis=0)))
```
<!-- .element: style="font-size:36%" -->

--

## Min and Max

* [題目連結](https://www.hackerrank.com/challenges/np-min-and-max)
* 給你 $N\times M$ 的矩陣，請你計算每一個橫列 (axis = 1) 的最小值、然後計算並輸出這些值的最大值。
  * 要注意的是 axis 預設是 `None`，也就是對整個矩陣的所有元素取 `min()` 或 `max()`。

--

## Min and Max（解答篇）

```python
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.max(numpy.min(A, axis=1)))
```
<!-- .element: style="font-size:36%" -->

--

## Mean, Var, and Std

* [題目連結](https://www.hackerrank.com/challenges/np-mean-var-and-std)

--

## Dot and Cross

* [題目連結](https://www.hackerrank.com/challenges/np-dot-and-cross)
* 矩陣乘法！
* 向量的內積、外積。

--

## Polynomials

* [題目連結](https://www.hackerrank.com/challenges/np-polynomials)
* 多項式的建構、求根、微分、不定積分、代值、回歸（最小平方法）

--

## Linear Algebra

* [題目連結](https://www.hackerrank.com/challenges/np-linear-algebra)
* 行列式值(det)、特徵值(eig)、反矩陣(inv)
