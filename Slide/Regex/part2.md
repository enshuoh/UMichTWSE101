## 擴充語法 II
### Extended Regular Expression

目的：字串的**搜尋**與**取代**

--

## 常用形式

* 用 `/` 把正規表達式圍起來

```
/regex/flags
```

--

## 好用小工具

* [Regular Expressions 101](https://regex101.com/)

--

## Capture Groups

* 把找到的 pattern 分成好幾組，以便取用。
* 在擴充使用的方法中，甚至可以把找到的 capture group 當做 pattern！

```
([abc])\1
```

--

## 列首、列尾

* `^` - begin of the line.
* `$` - end of the line.

--

## 跳脫字元 Escaped Characters

* `\.`
* `\(`, `\)`
* `\/`, `\\`
* `\^`, `\$`

--

## 方便的表示法

* `\w` - word characters
* `\d` - 數字字元
* `\s` - 泛空白字元

--

## 選項 Flags

* `g` - global
* `i` - Case insensitive

--

## Grep

* ed: 簡易文字編輯器
* g/re/p (globally search a regular expression and print)

```
$ grep -i "python" -r .
```

--

## Shell Tools

* sed
* awk


--

## Challenges

* [Regular Expression Crosswords](https://regexcrossword.com/)
* [Regular Tuesday Challenges](http://callumacrae.github.io/regex-tuesday/)



--

## 判斷質數

* 判斷字串是否由質數個 1 所組成。

http://stackoverflow.com/questions/3296050/how-does-this-regex-find-primes


--

## 自產生程式碼 Quine

* [Quine](https://en.wikipedia.org/wiki/Quine_(computing))
* [self-matched regex](http://codegolf.stackexchange.com/questions/6798/self-matching-regex)
