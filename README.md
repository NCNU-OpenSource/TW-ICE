# TW-ICE
##概念敘述
常常將食物放在冰箱裡就忘記了，不知不覺就放到過期，導致食物的浪費，TW ICE 想到透過樹梅派與Web Cam搭配自製QR Code條碼，將食物放入冰箱前先貼上貼紙掃描後，便可以記錄冰箱中各食材的存放時間，並在快過期時推播訊息提醒使用者。
##Camera 使用套件安裝、參考網站
檢查是否有 webcam
## connector():
連接Database。
## create_new_table():
用於新增新的table。
## create_new_data_with_qrcode(qrcode_number):
每當掃描到新的物件時產生新的資料放入database。
## read_all_data():
讀取table裡所有的資料，可做為list使用(目前輸出格式還未定案)。
## read_specified_data_use_serial_number(serial_number):
讀取table裡指定流水號的資料(目前輸出格式還未定案)。
## read_specified_data_use_name(name):
讀取table裡指定名稱的資料，可以有多筆(目前輸出格式還未定案)。
## update_data_use_serial_number(update_type,update_data,serial_number):
* Update type 1 :
更新食品名稱
* Update type 2 :
更新第一次入庫時間
* Update type 3 :
更新最近一次入庫時間
* Update type 4 :
更新最近一次出庫時間
* Update type 5 :
更新食品保存期限
## delete_data_use_serial_number(serial_number):
刪除table裡指定流水號的資料。
