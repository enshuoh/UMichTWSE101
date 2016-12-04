# 瀏覽器 Browser

--
<img src="https://my.vinu.edu/documents/2799529/0/browser+icons.png/37554263-d16e-4df3-bf58-e3e286c43496?t=1456854691735" width=600>

--

### 網頁瀏覽器

- 用於檢索並展示全球資訊網(World Wide Web)資訊資源的應用程式。 (Wikipedia)
  - 資訊資源可能有很多種
    - 文字
    - pdf
    - 影像
- http://www.whatbrowser.org/#top

--

### WWW V.S. Internet

- Internet
  - Network of Network
  - 由數個網路以網路協定(TCP/IP protocols)相連所產生的龐大網路
- WWW
  - 基於Hypertext相連的系統
  - 系統中每個東西都被視為一樣資源，由一個Global的URI(Uniform Resource Identifier)標示
    - URI vs URL
- Internet所提供的不只有WWW
  - 電子郵件
  - 檔案分享
  - IP電話

--

### HyperText
- 用來顯示文字與文字相關的內容
  - 其他相關文字
  - 圖片
- 文字包含有可以連接到其他地方的超連結
- WWW的架構以Hypertext的概念定義為基礎
- 非日常生活中的線性文字 -> Nonlinear
- [!Project Xanadu 仙那度計畫](http://reader.roodo.com/loveshow/archives/2678488.html)
- 是一個概念

--

### HTML VS Hypertext?
- HyperText Markup Language
- 建立網頁的標準標示語言
- 電腦讀取程式碼，執行程式
- 瀏覽器讀取HTML，顯示出我們想要看到的內容

--

### CSS
- Cascading Style Sheets 階層式樣式表
- 用於把結構化的文件(HTML, XML)添加樣式的語言
- 優點
  - 增加可讀性
  - 檔案結構靈活
  - 作者、讀者可以自行決定顯示方式
  - 檔案結構簡化
- Style Sheets在HTML被發明時就以各種形式出現
- CSS是第一個有Cascading概念的
  - 樣式由其他的樣式表繼承

--

### Javascript
- 直譯式語言
- 大多數主流瀏覽器都支援
- 不只可以用於網頁
  - PDF
  - 遊戲
  - 電腦應用程式
    - 伺服器 Node.js
    - Editor Atom, Visual Studio Code

--

### HTML5
- 狹義
  - 新的HTML標準
- 廣義
  - HTML+CSS+JS的技術組合
- 希望能夠減少瀏覽器對於Plugin的需求
  - Flash
  - JavaFX
  - Silverlight

--

### 網頁瀏覽器
<img src="http://taligarsiel.com/Projects/layers.png" width=600>

--

### 網頁瀏覽器
- 前端使用者介面
  - 搜尋欄
  - 上、下、首頁
  - ...
- Browser Engine
  - 接收介面傳來的資訊
  - 和後端的Rendering Engine溝通
- Rendering Engine
  - 將得到的Response顯示出來
    - 包括解析HTML、CSS
    - 控制Networking
    - 呼叫JavaScript Interpreter
    - 呼叫UI Backend

--

### Browser Engine
- Webkit
  - Chrome
  - Safari
- Gecko
  - Firefox
- 流程
  - HTML -> DOM Tree
    - 解析HTML的結構
    - 解析Style
  - 產生對應的Rendering Tree
  - 確定Layout
  - 繪製在螢幕上
- 為了使用者體驗，Browser Engine會儘早將內容顯示出來
  - HTML可能還沒完整解析完

--

### DOM
- Document Object Model
- 提供HTML, XHTML, XML等文本，能以樹狀結構操作的程式介面
- W3C制定的標準
- 瀏覽器大戰的產物
  - Netscape VS Microsoft (1998)
    - Javascript, Jscript
    - VBScript, ActiveX, DHTML...

--

### 如何解析HTML、CSS、JS
- 根據W3C、JS的規範
  - HTML parser
  - CSS parser
