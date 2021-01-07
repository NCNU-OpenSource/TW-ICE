# TW-ICE 
# 概念敘述
常常將食物放在冰箱裡就忘記了，不知不覺就放到過期，導致食物的浪費，TW ICE 想到透過樹梅派與Web Cam搭配自製QR Code條碼，將食物放入冰箱前先貼上貼紙掃描後，便可以記錄冰箱中各食材的存放時間，並在快過期時推播訊息提醒使用者。
# Pi 4 Ubuntu 18.04
## 安裝 python pip install(可以直接在pi下pip install or pip3 install)
```shell
  sudo apt update
  sudo apt install python-pip
  sudo apt install python3-pip
```
# Camera 使用套件安裝、參考網站
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
  pip install mysql-connector-python
```
