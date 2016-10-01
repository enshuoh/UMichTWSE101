# 機器學習初體驗

---

## 先來裝package
$ git clone https://github.com/whus6207/se101_week1.git

$ cd se101_week1/

$ chmod 755 setup_env.sh

$ ./setup_env.sh

---

<img class="plain" src="http://images-cdn.9gag.com/photo/4138344_700b.jpg" height = 650>

--

### Machine Learning? AI?<br>Data Mining?

--

<img class="plain" src="https://www.analyticsvidhya.com/wp-content/uploads/2015/06/machine-learning.png">

--

- Data Mining: 從data中尋找意義
- Machine Learning: 從data學習，利用所學做預測
- AI: 人工的「智慧」

---

## 為什麼機器能學到東西
圖片及內容來自台大林軒田教授

--

## Terminology
- training
- feature
- model
- prediction

--

### 學習的基礎架構
<img class="plain" src="http://beader.me/imgs/is-learning-feasible/basic_setup_of_the_learning_problem.png" style="width:1700px">

--

## Learning 可行嗎？
<img class="plain" src="http://beader.me/imgs/is-learning-feasible/a_learning_puzzle.png">

--

- A: g(對稱) = +1, g(不對稱) = -1

- B: g(左上角白色) = +1, g(左上角) = -1

誰對？？

--

## 推斷未知的世界
用樣本的統計推斷整體的參數

--

### 複雜版的大數法則
樣本數越大，我們所選 h (看到的誤差) 跟 (實際的誤差) <br>「差很少」的「機率很大」
![](img/PAC.png)

--

### PAC Learnible
Probably Approximately Correct

可能大概正確

--

<img class="plain", src="https://cdn.meme.am/instances/500x/12334653.jpg" width=600>

---

## 三種問題

--

- Regression: 預測連續的值 - 價格、機率...
- Classification: 預測分類 - 好壞、哪種動物...
- Clustering: 把相近的點歸類在一起


--

## 常用模型

--

### 線性回歸 Linear Regression
[fancy demo](http://setosa.io/ev/ordinary-least-squares-regression/)

--

### Naive Bayes
<img class="plain" src="http://www.saedsayad.com/images/Bayes_rule.png" width=800>

--

### 決策樹 Decision Tree
[fancy demo](http://www.r2d3.us/%E5%9C%96%E8%A7%A3%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%AC%AC%E4%B8%80%E7%AB%A0/)

--

### K Means
[影片](https://www.youtube.com/watch?v=gSt4_kcZPxE)

---

## 機器學習的種類
- supervised
- semi-supervised
- unsupervised
- reinforcement learning

--

### Reinforcement Learning
[fancy demo](http://cs.stanford.edu/people/karpathy/convnetjs/demo/rldemo.html)

---

## 實際上常見的問題

--

## P1: Curse of Dimensionality

--

### Sol: Principle Component Analysis(PCA)
<img class="plain" src="http://lazyprogrammer.me/wp-content/uploads/2015/11/PCA.jpg">

--

## P2: Biased Training Data

--

### Sol: Cross Validation
<img class="plain" src="http://sebastianraschka.com/images/faq/evaluate-a-model/k-fold.png" width=800>

--

### 用途: Parameter Tuning
<img class-"plain" src="https://qph.ec.quoracdn.net/main-qimg-2d5918dd335def0b7bb9c5ec3a26d9be?convert_to_webp=true" width=800>

--

## P3: Overfitting
<img class="plain" src="https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg" width=500>

--

### Sol: Stop Early
<img class="plain" src="http://blog.fliptop.com/wp-content/uploads/2015/03/highvariance.png" width=650>


---

# Hands on!

--

## Task: Iris Classification
<img class="plain" src="http://www.plant-world-seeds.com/images/seed_images/IRIS_VERSICOLOR/size2_200x200/IRIS_VERSICOLOR.JPG?1355843115"><img class="plain" src="http://www.plant-world-seeds.com/images/seed_images/IRIS_SETOSA/size2_200x200/IRIS%20SETOSA.JPG?1283789830"><img class = "plain" src="http://www.plant-world-seeds.com/images/seed_images/IRIS_VIRGINICA/size2_200x200/IRIS_VIRGINICA.JPG?1363709343">

--

## 打開 c9.io !

---

# Thinking Challenge

--

## 旅遊網站抓騙子
- 假信用卡
- 從甲飛乙，但在很遠的丙訂旅館
- 盜帳號
- ...

--

## 思考方向
- 需要的data
- 三種問題(classify, regression, clustering)裡的哪一種？
- 怎麼train，怎麼make prediction?
- 客戶隱私
