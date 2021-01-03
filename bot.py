import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup as InlineMarkup
from telepot.namedtuple import InlineKeyboardButton as InlineBtn
from telepot.namedtuple import ReplyKeyboardMarkup as ReplyMarkup
from telepot.namedtuple import KeyboardButton as Btn

import mysql.connector ,time ,os
from mysql.connector import Error

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) #抓取當前的位置，用於抓取token碼

try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='10.33.20.8',          # 主機名稱
        database='telebot', # 資料庫名稱
        user='TW_ICE_telebot',        # 帳號
        password='lsa4')  # 密碼

    if connection.is_connected():

            # 查詢資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT user FROM mysql.user;")

        # 取回全部的資料
        records = cursor.fetchall()
        print("資料筆數：", cursor.rowcount)

        # 列出查詢的資料
        for user in records:
            print("Name: %s" % user)

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")

with open(os.path.join(BASE_DIR, 'token.txt')) as f:
    TELEGRAM_BOT_TOKEN = f.read().strip() # Telegram Bot Token
bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

#MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()
print("I'm listening...")

## 列出冰箱內物品清單
# def getItemList()
#     global itemDict
#     for i in range(len(資料庫資料where status == 正在冰)) # 因為那時討論說就算拿出來資料仍要保留幾天,所以不是全部都要顯示
#         itemDict[i] = {}

#     return itemDict

## 檢查保存期限 (設timer 每小時執行一次 / 提供一個function查看 / 小於3hr提示快要過期)
# def checkExpirationDate()
#        需要pip datatime
#        time = data.time.now()
#        跟資料庫中的放入時間+保存期限相減
#        return XXX



## 修改食材品項
# def updateItemName()




## 修改保存期限
# def updateItemExpirationDate()





def on_chat_message(msg):
    global itemString
    content_type, chat_type, chat_id = telepot.glance(msg)
    # 檢查接收到的是否為文字訊息
    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
        pprint(msg)
        chat_id = msg['chat']['id']
        from_id = msg['from']['id']
        if msg['text'] == '/help' :
            replyBtns = [
                    [Btn(text='/show')],
                    [Btn(text='/add'), Btn(text='/update'), Btn(text='/vol_up')],
                    [Btn(text='/add_from_plist'), Btn(text='/play_all_plist')],
                    [Btn(text='/edit_plist'), Btn(text='/create_plist')],
                    [Btn(text='/broadcast')]
                ]
            time.sleep(1)
            bot.sendMessage(chat_id, 'Here\'s all function buttons', reply_markup=ReplyMarkup(keyboard=replyBtns))
        
        elif msg['text'] == 'show' :
            bot.sendMessage(chat_id, itemString)
        elif msg['text'] == '/update' :
            bot.sendMessage(chat_id, "2")
        #
        elif msg['text'] == '/add'  :
            bot.sendMessage(chat_id, "3")



    # 傳文字
    #text = msg['text']
    #bot.sendMessage(chat_id, text)

    # 傳圖片
    #photo = 'https://imgur.com/gallery/UoGUPux'
    #bot.sendPhoto(chat_id, photo)

# global variables
itemList = {}
itenString = 'ABCS'

MessageLoop(bot,on_chat_message).run_as_thread()
while 1:
    time.sleep(10)