# Big Data

--

## 什麼是Big Data

https://en.wikipedia.org/wiki/Big_data wiki
http://www.sas.com/en_us/insights/big-data/what-is-big-data.html sas
https://www.ibm.com/big-data/us/en/ ibm
http://www.mckinsey.com/business-functions/digital-mckinsey/our-insights/big-data-the-next-frontier-for-innovation mckinsey
https://www.inside.com.tw/2015/02/06/big-data-1-origin-and-4vs
https://www.youtube.com/watch?v=j-0cUmUyb-Y

--

## 為什麼Big Data重要

--

## 對SE來說，所面臨的挑戰是？
http://www.ibmbigdatahub.com/infographic/four-vs-big-data
- Big Data造成的挑戰通常分類為4V
  - Volume - Scale of data
  - Velocity - Analysis of streaming data
  - Variety - Different forms of data
  - Veracity - Uncertainty of data

--

## Volume 資料量
https://www.inside.com.tw/2015/05/06/25-eye-opening-facts-about-big-data-you-should-know
http://www.ithome.com.tw/article/87190
||以前|現在|
|:-----:||:---:|:----:|
|來源|由員工負責產生資料|在各類系統(如社群網路)中機器、網路或人的互動產生的資料|
|量級|300 exabytes(2007)| 4.4 zetabytes(2013)|
|儲存|單台強大的伺服器|必定需要多台電腦來儲存|

- 提一些喜歡的例子
- 算是4V中最容易處理的部份

--

## Velocity 資料輸入輸出速度
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

## Variety 資料多樣性
- 除了文本資料，開始出現其他種
  - 視訊
  - 音樂
  - 圖片
- 資料來源不同，導致格式可能不同
  - 結構化
  - 非結構化
- NoSQL的產生

--

## Veracity 資料真實性
- 資料偏差
  - 雜訊
- 資料異常
  - 機器錯誤
- 偽造資料
  - 垃圾訊息
  - search engine optimization(SEO)
  - 機器人帳號
- 如何過濾錯誤、異常的資料
- 如何保證系統在發生錯誤時可以正常運作

--

有名的Framework
Computation
Hadoop, Spark, Flink, Storm

Kafka

Database
Cassandra, HBase, MongoDB, Hive, Redis

HDFS, Pig
Lucene, Flume

https://twitter.com/ianhellstrom/status/710917506412716033

http://www.infoworld.com/article/2982429/open-source-tools/bossie-awards-2015-the-best-open-source-big-data-tools.html#slide4

--
## 介紹 Map-Reduce model?

--

## 介紹Framework
