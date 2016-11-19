# Unit 7
## Linked Lists

鏈結串列的練習

--

## 記憶體

* 每一個 byte 都有一個**位址**。
* 我們可以指定一連串的 byte，用來存儲資料。
* 特別強調：在 Python 之類高階語言的世界裡，是不存在指標的觀念的！

```python
>>> x = list(range(10))
>>> hex(id(x))
'0x10f6a04c8'
>>> hex(id(x[0]))
'0x10f39c9d0'
>>> hex(id(x[1]))
'0x10f39c9f0'
>>> hex(id(x[2]))
'0x10f39ca10'
>>> hex(id(x[3]))
'0x10f39ca30'
>>> hex(id(x[4]))
'0x10f39ca50'
>>> hex(id(x[5]))
'0x10f39ca70'
```

--

## 記憶體的 Layout

<img src="https://gabrieletolomei.files.wordpress.com/2013/10/program_in_memory2.png" style="width:600px">

--

## 用物件模擬鏈結串列

* (Singly) Linked List
* Doubly Linked List
* Circular Linked List

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg" style="width:400px;background-color:white">

--

## Reverse Linked List

* [Leetcode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

--

## Reverse Linked List II

* [Leetcode 92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

--

## Linked List Cycle

* [Leetcode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

--

## Linked List Cycle II

* [Leetcode 142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)


--


## Doubly Linked List

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
```

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Doubly-linked-list.svg" style="width:700px;background-color:white">

--

## Doubly Linked List in C

```c
typedef struct ListNode {
  int val;
  ListNode* prev, next;
} ListNode;
```

* 挑戰題：有沒有辦法設計一個很像 Doubly Linked List 但是更節省空間的資料結構？

--

# Have a good weekend!
