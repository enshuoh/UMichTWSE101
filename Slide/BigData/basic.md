# Big Data

--

<img src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQD9YVOZfN6VMhZqPFMwUn2xcuf4XwH_ifAd39-jcZL4AEByszkrQ" width=400><img src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ6nMQkwYul6rfQgjYciCfT043CXcd4A3QQpcUn3N5W1oqffFX6Og" width=400><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN06wSGs3fkBCE0TCyv18efeYWBlN50AF-rw2oLL4p5OPFVKj2" width=600>

--

### 什麼是Big Data

- 繼「Cloud Computing」後的新Buzz Word
- “Big data is data that exceeds the processing capacity of conventional database systems.”

--

### 為什麼現在Big Data這麼紅

- Data Scientist: the sexiest job of 21st century
- 大量的(自動化)可得資訊
- 帶來新的決策方式
  - 金融、行銷、廣告、教育、醫療、政策

<img src="http://www.jobscience.com/wp-content/uploads/2013/08/c-3.jpeg" width=300>


--

## 對SE來說，所面臨的挑戰是？

- Big Data造成的挑戰通常分類為4V
  - Volume - Scale of data
  - Velocity - Analysis of streaming data
  - Variety - Different forms of data
  - Veracity - Uncertainty of data
  - 大、快、雜、疑

--

### Volume 資料量
[一些數據](https://www.inside.com.tw/2015/05/06/25-eye-opening-facts-about-big-data-you-should-know)

||以前|現在|
|:-----:||:---:|:----:|
|來源|由員工負責產生資料|在各類系統(如社群網路)中機器、網路或人的互動產生的資料|
|量級|300 exabytes(2007)| 4.4 zetabytes(2013)|
|儲存|單台強大的伺服器|必定需要多台電腦來儲存|

- GB TB PB EB ZB YB
- 提一些喜歡的例子
- 算是4V中最容易處理的部份

--

### Velocity 資料輸入輸出速度
- 產生資料的速度 > 消化資料的速度
  - 更多sensor
  - 網路資料
  - 交易資料
- 資料需要在某個時效內處理完
  - 例如大選資料的分析要在大選開始前完成
- 需要的技術
  - 平行運算
  - 演算法改進
    - 平行化
    - 用估計取代準確值

--

### Variety 資料多樣性
- 除了文本資料，開始出現其他種
  - 視訊
  - 音樂
  - 圖片
- 資料來源不同，導致格式可能不同
  - 結構化
  - 非結構化
- NoSQL的產生
  - SQL: Structured Query Language

--

### Veracity 資料真實性
- 資料偏差
  - 雜訊
  - 人為篩選
- 資料異常
  - 機器錯誤
- 偽造資料
  - 垃圾訊息
  - search engine optimization(SEO)
  - 機器人帳號
- 如何過濾錯誤、異常的資料
- 如何保證系統在發生錯誤時可以正常運作

---

# 一些有用的觀念

--

## Distributed System

--

### 分散式系統
- 一群分散在以網路連接、互相通訊的計算單元
    - cluster: 叢集
    - node: 節點
- 有一個共同的目標

--

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Distributed-parallel.svg" width=450>

--

### pros & cons
- 好處
  - concurrency
  - fault tolerant
  - resource sharing
  - scalability
- 壞處
  - overhead
  - complexity
  - security

--

### 常見架構
- master-worker: 單純，master可能是bottleneck
- multi-tier: 好維護(deploymeny, testing, security...)
- peer-to-peer: low cost, reliable，難維護

--

## Map-Reduce

--

### What is Map-Reduce
- Google提出的programming model，來自functional language
- 讓平行運算更簡單優雅

--

### 複習Map, Reduce

- map: 對每一個元素進行處理
```python
F = list(map(lambda x: (float(9)/5)*x + 32, C))
```
- reduce: 把結果合併起來
```python
fib = lambda n:reduce(
        lambda x,n:[x[1],x[0]+x[1]],
        range(n),[0,1])[0]
```

--

### Example: WordCount
```
echo "jimmy watch football bad bad" 
  | python mapper.py | sort -k 1 
  | python reducer.py

```

--

<img src="http://image.slidesharecdn.com/bigdataseminarbymants-131224083456-phpapp02/95/bigdata-survey-on-scheduling-methods-in-hadoop-mapreduce-13-638.jpg?cb=1387874235" width=800>

--

### 小練習

- 用MapReduce找Facebook共同好友數
- input
```
A -> B C D
B -> A C D E
C -> A B D E
D -> A B C E
E -> B C D
```
- 重點：怎麼map?

--

### 解答

```
map(A -> B C D) :
(A B) -> B C D
(A C) -> B C D
(A D) -> B C 

map(B -> A C D E) :
(A B) -> A C D E
(B C) -> A C D E
(B D) -> A C D E
(B E) -> A C D E
...
```

---

# 常見Framework

--

## Big Data Computation

--

## Hadoop
<img src="http://saphanatutorial.com/wp-content/uploads/2014/01/What-is-Hadoop-1.jpg">
- open source Java-based programming framework
- 分散式系統上處理大量資料運算
- MapReduce, HDFS

--

### Hadoop components
<img src="https://s3.amazonaws.com/files.dezyre.com/images/blog/Hadoop_2.0_and_YARN_Advantages_over_Hadoop_1.0_2.png" width=800>

--

## Hadoop YARN
- 把 資源管理 與 工作分派/監督 分開
<img src="http://hadoop.apache.org/docs/stable2/hadoop-yarn/hadoop-yarn-site/yarn_architecture.gif" width=800>

--

## Hadoop File System (HDFS)
- inspired by Google File System

--

### HDFS怎麼運作？

- 資料被拆成blocks，分散在cluster中
  - 專為Map-Reduce設計
- 備份在其他node中
  - fault tolerant 
  - data locality: 減少network overhead

--

<img src="http://sls.weco.net/files/u763/HDFSArch.JPG">

--
### pros & cons

- pros:
  - scalable
  - flexible(any type of data)
  - fault tolerant
  - cost efficient
- cons:
  - 不是所有問題都適合MapReduce
  - security
  - too many disk IO


--

## Spoch
<img src="http://img.ltn.com.tw/Upload/ent/page/800/2015/02/28/phpezBeMz.jpg">

--

## Spark
<img src = "http://www.ictbusiness.it/files/2015/02/immagini_contenuti/34073/logo-spark_t.png" width=200>
- 10x faster than Hadoop MapReduce
  - Hadoop: (讀檔->map->寫回)*n->(讀檔->reduce->寫回)*n
  - Spark: 讀檔->(map->->reduce)*n->寫回
  - in-memory compuation
- 可以跑在Hadoop cluster上

--

## Flink
<img src="http://10minbasics.com/wp-content/uploads/2015/10/flink.png">
- 分散式串流資料處理
  - low latency
- 可以跑在 Hadoop cluster上
- 支援 Streaming & Batch processing

--

### Throuput vs Latency
- throughput: operation per sec
- latency: response time per request

--

### Batch vs Streaming
- 一次通通來
  - 重點：high throuput
- 一個一個一直來
  - 重點：low latency

--

### Operator Level Control
<img src="https://ci.apache.org/projects/flink/flink-docs-release-1.0/concepts/fig/parallel_dataflow.svg">

--

### Master-worker Arch
<img src="https://ci.apache.org/projects/flink/flink-docs-release-1.0/concepts/fig/processes.svg" width=700>

--

### Resource Management
<img src="https://ci.apache.org/projects/flink/flink-docs-release-1.0/concepts/fig/slot_sharing.svg">

--

### Fault Tolerance
<img src="https://ci.apache.org/projects/flink/flink-docs-release-1.0/concepts/fig/checkpoints.svg">

--

# Storage

--

## NoSQL
- why?
  - 大量資料
    - 可擴充
  - 要很快很快
  - 要彈性
- Relational Database
  - ACID(Atomicity, Consistency, Isolation, Durability)

--

## MongoDB
<img src="https://cdn.vidyard.com/thumbnails/custom/IbIp11o3ZFbPI4xxwGsPUw">

--

## MongoDB
- Document-based storage: JSON formatted
- master-slave
- NoSQL
  - 彈性
  - 可擴充性、快速(ACID rules byebye)
- 免費，小公司首選

--

### JSON(Javascript Object Notation)
```
{
    _id: 1234,
    author: { name: "Bob Davis", email : "bob@bob.com" },
    rating: 2.2,
    comments: [
       { user: "jgs32@hotmail.com",
         text: "Great point! I agree" },
       { user: "holly.davidson@gmail.com",
         text: "You are a moron" }
    ],
    tags: [ "Politics", "Virginia" ]
 }

```

--

## Cassandra
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/220px-Cassandra_logo.svg.png">
- fully distributed (vs Hadoop, MongoDB): no bottleneck
- fault tolerant
- log-structured storage engine
  - no conflict

--

## Redis
<img src="https://www.hostbridge.com/images/redis-300dpi.png" width=400>
- in-memory data structure store
  - 可以用作database、cache
  - 很快
- 支援geo-location

--

# 其他

--

## 下次再說

