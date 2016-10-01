## 常用指令
- man (MANual)
- ls, cd
- cat (Concatenate And prinT)
- chmod (CHange file MODe)
- mkdir (MaKe DIRectory), rmdir(ReMove DIRectory), rm (ReMove)
- others

--

## man
- man: man [-acdfFhkKtwW] [--path] [-m system] [-p string] [-C config_file] [-M pathlist] [-P pager] [-B browser] [-H htmlpager] [-S section_list] [section] name
- [] Optional 選用參數
- ![] 必要參數
- task
  - 查看ls, cd的使用方式

--

## ls, cd
- Task
  - 移動到UMichTWSE101
    - 底下的Material
    - 底下的LinuxBasic
  - 查看genFile.py的檔案大小(?B)
  - 查看現在資料夾內有幾個檔案(不含資料)
  - <a target="blank" href="http://qstn.co/q/fJcvpWQX">投票</a>

--

## ls, cd
- ls
  - -l
    - 以詳細清單顯示(List)
  - -a
    - 顯示全部檔案(All)
  - -R
    - 遇到資料夾繼續往下(遞迴, Recursive)
  - -h
    - 搭配-l使用，將容量轉為人類可讀(Human Readable)
- cd
  - cd -
    - 回到上一個資料夾

--

## cat
- 請先執行
  - sh init.sh
  - cat helloCat.txt

--

## cat
- 請問
  - largeFile.txt最後一行的數字是?
  - largeFile.txt第一行的數字是?
  - largeFile.txt裡面有幾行是10?
  - largeFile.txt裡面有幾行可以被10整除?

--

## head, tail, grep, wc
- head 印出檔案前幾行
- tail 印出檔案後幾行
- grep 抓出檔案內符合要求的行
- wc 數檔案的行數、字數、Bytes數

--

## chmod
- Task
  - 請印出.hiddenFile的內容

--

## chmod
- chmod +r .hiddenFile
  - 設為可讀
- chmod +w .hiddenFile
  - 設為可寫
- chmod +x .hiddenFile
  - 設為可執行
- chmod 777 .hiddenFile
  - 這有點難，man是你的好朋友

--

## mkdir, rm
- Task
  - 請產生一個叫做MyFirstDir的資料夾
  - 請把它刪掉
  - 請把.hiddenFile, largeFile.txt 刪掉
  - 請把.hiddenDir刪掉

--

## mkdir, rmdir, rm
- mkdir MyFirstDir
  - 產生資料夾
- rm .hiddenFile largeFile.txt
  - 刪除多個檔案
- rmdir MyFirstDir (rm -d MayFirstDir)
  - 刪除資料夾
- rm -r .hiddenDir
  - 遞迴刪除資料夾
- 覺得提示很煩
  - -f 是你的好...?朋友

--

## others
- pwd
- clear, echo
- touch, cp, mv
- tar
