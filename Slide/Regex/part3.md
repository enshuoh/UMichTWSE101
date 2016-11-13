# Regex in Python

```
import re
re.search('regex', text)
```

https://docs.python.org/3/library/re.html

--

## 擴充語法 III

* Named Groups:
  - 賦予 group 名稱 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```
(?P<name>...)
```
  - 使用 pattern
```
(?P=name)
```
* 舉例：Quotations

--

## 擴充語法 IV

* Non-capturing groups
```
(?:...)
```
* If matched group exists
```
(?(id/name)yes-pattern|no-pattern)
```
<!-- .element: style="left:-50px;min-width:800px" -->
* 後置判斷(如果符合才接受)
```
(?=...)
```
* 後置判斷(如果不符合才接受)
```
(?!...)
```

--

## Valid Number

* [Leetcode 65. Valid Number](https://leetcode.com/problems/valid-number/)

--

## Regular Expression Matching

* [Leetcode 76. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
