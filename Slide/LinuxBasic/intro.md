# Linux 基礎
* Linux歷史課、Linux簡介、名詞賞析
* 常用指令介紹與練習

---

## 作業系統
  - Operation System
  - 範例 (順序無特別意義、理性勿戰)
    - Android, iOS
    - OSX, Windows, RedHat, Ubuntu
  - 管理電腦硬體與軟體資源的電腦程式 （Wikipedia)
  - 幫助我們執行程式
  - 幫助我們處理麻煩事情
    - 讀寫記憶體、硬碟
    - 顯示圖像
    - 透過網路傳輸資料
    - 管理檔案系統

--

![OS](https://upload.wikimedia.org/wikipedia/commons/d/d8/Operating_system_architecture.svg)

--

## Linux? Unix?

https://upload.wikimedia.org/wikipedia/commons/7/77/Unix_history-simple.svg

--

![unix-like](https://upload.wikimedia.org/wikipedia/commons/7/77/Unix_history-simple.svg "Unix like")

--

## Linux 結構簡介
* Shell是我們的好朋友
* 萬物皆檔案
* 萬事皆程序

--

## Shell是我們的好朋友
- 什麼是Shell?
  - 為使用者提供使用者介面的軟體(User Interface UI)
    - 命令列介面(Command Line Interface CLI)
    - 圖形化介面(Graphical User Interface GUI)
  - 通常提到Shell時，指的是CLI的版本
    - 讓你的世界變彩色
    - 提示、自動完成
- 使用方式
  - 指令 [參數] [參數] [參數] [很多參數]
  - 指令 Instruction
  - 參數 Argument, parameter
- bash / sh / ksh / csh / zsh

--

## 萬物皆檔案(File)
- 什麼是檔案?
  - 被存在某個地方的一段代碼(字)
- 關於檔案我們需要知道什麼？
  - 內容
  - 擁有者
  - 修改時間
  - 可否讀、寫、執行

--

## 萬物皆檔案(File)
- 資料夾(Directory)?
  - 沒錯，資料夾也是檔案
    - 只是，是特別的檔案
      - 因為改錯內容，問題會很大條
      - 很常使用
    - 故通常
      - OS會把Directory跟非Directory的檔案分開處理
      - 我們說檔案(File) = 非資料夾的檔案
  - 但是還是要記得它是檔案，因為：
    - 很多概念是共通的
    - 例如: 權限、儲存方式

--

## 萬物皆檔案(File)
- ls (List directory content)
  - ls
  - ls -l
- cd
  - cd [target directory]
- 你打了ls、cd，按下Enter的時候究竟發生了什麼？
  - 晚點跟你們講
- 歡迎跟著我一起使用ls, cd看世界

--

## 檔案系統 (File System)
- 樹狀結構
  - 第一個資料夾叫做root(根目錄)
  - 以 "/" 代表
- 你永遠會在某個資料夾裡
  - 以 "." 代表

--

## 檔案系統 (File System)
- 等等..樹狀結構？ 難道...我們回不去了？
  - 以 ".." 代表
- 那有"..."嗎？
  - 別傻了孩子
  - 這種可以用..+..組出來的東西，設計者才懶得弄(?)
- 所有資料夾裡都有自動產生的"."跟".."
  - 哪裡怪怪的？
    - root?
- 補充
  - "~" 代表每個使用者各自的家目錄

--

## 程序(Process)
- 所有在Linux上執行的程式，都是一個程序
- 電腦怎麼知道我們的程式想要做什麼？
  - 從檔案裡讀取代碼(Code)
  - 可執行檔案 (Executable - x)
  - 可執行檔案一定要可讀寫嗎?
- 所以當我們輸入ls的時候?
  - 執行ls，把後面跟著的參數告訴他
  - ls -> 列出對應該參數的結果
- cd?
  - shell可以不提供cd

--
