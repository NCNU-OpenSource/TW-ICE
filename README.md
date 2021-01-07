# 概念敘述
常常將食物放在冰箱裡就忘記了，不知不覺就放到過期，導致食物的浪費，TW ICE 想到透過樹梅派與Web Cam搭配自製QR Code條碼，將食物放入冰箱前先貼上貼紙掃描後，便可以記錄冰箱中各食材的存放時間，並在快過期時推播訊息提醒使用者。
# 所需設備
- Raspberry pi 4 一台(需先安裝好Ubuntu 18.04)
- Webcam 一台
# Pi 4 安裝套件
## 安裝 python pip install
```shell
  sudo apt update
  sudo apt install python-pip
  sudo apt install python3-pip
```
## 檢查是否有 webcam
```shell
  ls -l /dev/video*
```
## 安裝拍照套件 fswebcam
```shell
  sudo apt-get install fswebcam
```
## 安裝查看照片套件
```shell
  sudo apt-get install fbi
```
## 安裝OpenCV
```shell
  sudo apt-get update
  sudo apt-get install python3-opencv
  sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y
  pip3 install opencv-contrib-python==4.1.0.25
```
## 安裝 python 讀取 QR Code 套件
```shell
  pip3 install pyzbar
```
## 安裝 telegram bot 套件
```shell
  pip install telepot
```
## 安裝 MariaDB
```shell
  sudo apt-get install mariadb-server
```
## 安裝 SQL connector
```shell
  pip3 install mysql-connector-python
```
## Telegram 申請 Bot token
### 建立自己的telegram bot
- 在telegram 中找到@BotFather 發送/newbot指令。
- 為機器人命名(需要以_bot結尾)取得機器人的token(擁有token就能操控機器人,所以不要隨意上傳到網路上!)。
- clone專案到pi上後建立token.txt, 將從@BotFather那邊拿到的token填入後存檔。
## 建立一個database讓telebot使用
先進入 sql。
```shell
  sudo mysql -u root
```
安全設定，建議全部填Y即可，想要了解內容可以細讀。
```shell
  sudo mysql_secure_installation
```
倘若需要從外部讀取資料，可以先建立一個 user，名稱為 TW_ICE_telebot，這樣可以從外部讀取資料庫內容。
```sql
  CREATE USER 'TW_ICE_telebot'@'%.%.%.%' IDENTIFIED BY 'yourpassword';
```
在sql內建立一個database，名稱為 telebot。
```sql
  CREATE DATABASE telebot;
  -- 給予TW_ICE_telebot權限更改資料庫內容
  GRANT ALL PRIVILEGES ON *.* TO 'TW_ICE_telebot'@'%.%.%.%' IDENTIFIED BY 'yourpassword' ;
  FLUSH PRIVILEGES;
  EXIT
```
## 從GitHub下載資料
先下載git。
```shell
  sudo apt-get install git
```
clone檔案。
```shell
  git clone https://github.com/peter6098790/TW-ICE.git
```
之後進入TW_ICE資料庫內，並建立一個資料夾 picture，待會要放食品照片用。
```shell
  cd ./TW_ICE
  mkdir picture
```
在同一個資料夾下方新增 token.txt，把 Telegram bot 的 token 寫入 token.txt
```shell
  vi token.txt
  1234679000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
## 建立資料表
需要手動建立資料表，先移至TW_ICE資料夾下。
```shell
  vim DB_CRUD.py
```
輸入資料表的名稱 table_name = 'your table name' ， 並且將最下面create_new_table()註解拿掉。
```python
  import mysql.connector
  from mysql.connector import Error
  import time, os
  import datetime
  BASE_DIR = os.path.dirname(os.path.realpath(__file__))
  table_name = ''
  ...
  ...
  ...
  # create_new_table()  建立新資料表
```
執行 DB_CRUD.py。
```shell
  python3 DB_CRUD.py
```
執行結束後將 create_new_table() 註解即可，資料表 table_name = 'your table name' 必須留著。
## 執行程式
接上 Web camera 之後之後開始執行bot.py這個程式。
```shell
  python3 bot.py
```
此時pi上顯示I'm listening... ， Telebot就可以開始執行了。
## Telebot測試
- 在Telegram上搜尋 : @tw_ice_bot
- /help 列出所有按鈕
- /show 冰箱中所有食物列表
- /update 更新食品內容
- /immediate_item 即將過期的食品列表
- /expiring_item 已過期食品列表
