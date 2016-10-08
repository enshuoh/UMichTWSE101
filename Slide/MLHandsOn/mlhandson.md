# 機器學習再體驗

---

## 先來裝package
```
$ git clone git clone https://github.com/jimmy9988/UMichTWSE101.git
$ cd UMichTWSE101/Material/MLHandsOn/
$ chmod 755 setup_env.sh
$ ./setup_env.sh
```

--

### Trouble Shooting
[TesnorFlow如果python3版本不同可能要修正](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html)

---

## 我們來做數字辨識

--

### MNIST dataset
<img class="plain" src="http://simonwinder.com/wp-content/uploads/2015/07/mnistExamples.png" width=800>

--

### 這是哪種問題？
- classification
- regression
- clustering

--

### 這是哪種問題？
- classification: 從已知的label set中選取適當的
- regression: 預測連續的值
- clustering: 根據某些特性將資料分成未知的幾堆

--

## 我們可以用 Decision Tree

--

### 複習一下 Decision Tree
- greedy的用最乾淨的切法把資料分開
- 一直切到徹底乾淨，或者不想再切了(overfitting)
- [好demo值得一看再看](http://www.r2d3.us/%E5%9C%96%E8%A7%A3%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%AC%AC%E4%B8%80%E7%AB%A0/)

---

## 打開 c9.io !

--

## 打開 ipython notebook
```
ipython3 notebook --ip=0.0.0.0 --port=8080 --no-browser
```

--

### import 需要的 library
```
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import numpy as np
```

--

### load data
```
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)

X_train = mnist.train.images
y_train = mnist.train.labels
X_test = mnist.test.images
y_test = mnist.test.labels
```

--

### train model
```
model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)
```

--

### 看看結果
```
y_predict = model.predict(X_test)
print("Train acc: "+str(model.score(X_train, y_train)))
print("Test acc: "+str(model.score(X_test, y_test)))
```

--

### 結果...好像不錯？
每9個數字錯1個

電話幾乎一定是錯的

--

<img class="plain" src="https://s-media-cache-ak0.pinimg.com/564x/3e/4e/01/3e4e01cd218049cde8251ebe27c42583.jpg" width=400>

---

## 怎麼樣更好呢？

--

### 聽說有個很厲害的東西叫 Deep Learning，韓國棋王都被他打敗了
<img class="plain" src="https://i.kinja-img.com/gawker-media/image/upload/s--2sdnK3GG--/c_scale,fl_progressive,q_80,w_800/upwcqiqcwjj9zv55rdvb.jpg">

--

## Convolutional Neural Network <br>卷積類神經網路
<img class="plain" src="https://ai2-s2-public.s3.amazonaws.com/figures/2016-03-25/f5f1beada9e269b2a7faed8dfe936919ac0c2397/1-Figure1-1.png">

--

### Convolution??
<img class="plain" src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif" width=800>

--

### Neural Network?? Neuron??
<img class="plain" src="http://www.cs.nott.ac.uk/~pszgxk/courses/g5aiai/006neuralnetworks/images/actfn001.jpg" width=800>

--

<img class="plain" src="https://i1.read01.com/image.php?url=0CdfD302" width=600><img class="plain" src="https://i2.read01.com/image.php?url=0CdfD303" width=600>

--

### Neural Network 怎麼學 weight?
- random initial weight

--

#### Back Propagation
<img class="plain" src="http://sebastianraschka.com/images/faq/visual-backpropagation/backpropagation.png" width=800>

--

<img class="plain" src="http://brohrer.github.io/images/cnn15.png">

--

#### random weight 讓我們更容易找到 global optimum
<img class="plain" src="http://2.bp.blogspot.com/-f7DSMK9xVZM/UWwU5bLqwsI/AAAAAAAAAUI/1XYF9naNY9o/s1600/6hc.png">

--

### 不負責任 CNN 簡介
詳情請看
- [how cnn works](http://brohrer.github.io/how_convolutional_neural_networks_work.html)
- TensorFlow
    - [MNIST For ML Beginners](https://www.tensorflow.org/versions/r0.11/tutorials/mnist/beginners/index.html)
    - [MNIST For ML Experts](https://www.tensorflow.org/versions/r0.11/tutorials/mnist/pros/index.html)

--

### 辨識OOXX
<img class="plain" src="http://brohrer.github.io/images/cnn1.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn2.png">

--

### 觀察：local feature
<img class="plain" src="http://brohrer.github.io/images/cnn3.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn4.png">

--

### Convolution
<img class="plain" src="http://brohrer.github.io/images/cnn5.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn6.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn7.png">

--

### Pooling
<img class="plain" src="http://brohrer.github.io/images/cnn8.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn9.png">

--

### "Deep" Learning: many layers
<img class="plain" src="http://brohrer.github.io/images/cnn12.png">

--

<img class="plain" src="http://brohrer.github.io/images/cnn18.png">

--

### 一般 Neural Net
<img class="plain" src="http://brohrer.github.io/images/cnn13.png">

--

### The Whole CNN
<img class="plain" src="http://brohrer.github.io/images/cnn14.png">

--

### Training
#### Back Propagation
<img class="plain" src="http://brohrer.github.io/images/cnn15.png" width=500>

---

# Think Like an Engineer

--

## 狀況一
### 旅遊網站抓騙子
- 假信用卡
- 買從New York飛San Francisco的機票，但訂開羅的旅館
- 盜帳號
- ...

--

## 思考方向
- 需要的data
- 三種問題(classify, regression, clustering)裡的哪一種？
- 怎麼train，怎麼make prediction?
- 客戶隱私

--

## 狀況二
### 想用手機監測睡眠品質
- 床墊的振動 => 翻身 => 偵測深眠淺眠

--

- 怎麼拿到夠多的data
- 怎麼得到ground truth
