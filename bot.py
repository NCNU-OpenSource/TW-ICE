import telepot
import time
import datetime
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup 
from telepot.namedtuple import InlineKeyboardButton 
from telepot.namedtuple import ReplyKeyboardMarkup as ReplyMarkup
from telepot.namedtuple import KeyboardButton as Btn
import DB_CRUD as db
import mysql.connector ,time ,os
from mysql.connector import Error
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# show all items in the refrigerator
def getItemList():
    global totalList, itemString
    totalList = db.read_data_in_ref()
    itemString = 'qrcode  name  expire_date' + '\n'
    if totalList:
        for item in totalList:
            #tmp = item  # tmp[0]: pk, tmp[1]: qrcode, tmp[2]: item name, tmp[6]: expire_date
            #print(tmp)
            # if item without item name
            if item[2] == None:
                itemString = itemString + item[1] + '\t' + 'None ' + '\t' + str(item[6]) + '\n'
            else:
                itemString = itemString + item[1] + '\t' + item[2]  + '\t' + str(item[6]) + '\n'
            print(item[6])
            print(type(item[6]))
    # nothing in the refrigerator
    else:
        itemString =  "There is Nothing in the refrigerator :("
    return itemString

def updateItem(qrcode,itemname,expirationDate):
    db.update_data_use_serial_number(1,itemname,qrcode)
    db.update_data_use_serial_number(5,expirationDate,qrcode)

# wait for the part of web cam
def takeOffItem(chat_id_list,qrcode,url):
    openurl = BASE_DIR + url
    for i in chat_id_list:
        bot.sendPhoto(i, photo=open(openurl, 'rb'), caption = qrcode + ' has been took off!')

# wait for the part of web cam
def getNewItem(chat_id_list,qrcode,url):
    openurl = BASE_DIR + url
    for i in chat_id_list:
        bot.sendPhoto(i, photo=open(openurl, 'rb'), caption = 'There is a new item: ' + qrcode + ' !')

def on_chat_message(msg):
    global itemString,chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    ## 
    inputdata = msg['text'].split() 
    print(inputdata)
    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])
        pprint(msg)
        chat_id = msg['chat']['id']
        from_id = msg['from']['id']
        # demo用途,把不在清單內的用戶加入清單,新食品進入時一起推播
        if chat_id not in chat_id_list :
            chat_id_list.append(chat_id)
        #print(chat_id)
        # reply photo to set item name and expire_date
        # if msg['reply_to_message']:
        #     tmp = msg['reply_to_message']['caption'].split()
        #     qrcode_number = tmp[5]
        #     item_name = inputdata[0]
        #     expire_date = inputdata[1]
        #     print(item_name,expire_date)
        if inputdata[0] == '/help' :
            replyBtns = [
                    [Btn(text='/show')],
                    [Btn(text='/updateInfo')],
                    [Btn(text='/Immediate item'), Btn(text='/Expiring item')]
                ]
            bot.sendMessage(chat_id, 'Here\'s all function buttons', reply_markup=ReplyMarkup(keyboard=replyBtns))
        elif inputdata[0] == '/show' :
            show = ''
            show = getItemList()
            bot.sendMessage(chat_id, show)
        elif inputdata[0] == '/updateInfo' :
            # qrcode is illegal
            if len(inputdata)==4 :
                date = inputdata[3].split('/')
                if len(date)==4 :
                    t = datetime.datetime(year=int(date[0]), month = int(date[1]), day = int(date[2]), hour = int(date[3]))
                    updateItem(inputdata[1],inputdata[2],t)
                    bot.sendMessage(chat_id,  msg['text'] + '\n' + 'Success!')
                elif len(date)==3 :
                    t = datetime.datetime(year=int(date[0]), month = int(date[1]), day = int(date[2]))
                    updateItem(inputdata[1],inputdata[2],t)
                    bot.sendMessage(chat_id,  msg['text']+ '\n' + 'Success!')
                else :
                    bot.sendMessage(chat_id, 'Usage:' + '\n' + '/updateInfo <qrcode> <item_name> <Year/Month/Day/Hour>' + '\n' + 'Example:' + '\n'+ '/updateInfo AXXXXX apple 2021/8/22/17')
            else: 
                bot.sendMessage(chat_id, 'Usage:' + '\n' + '/updateInfo <qrcode> <item_name> <Year/Month/Day/Hour>' + '\n' + 'Example:' + '\n'+ '/updateInfo AXXXXX apple 2021/8/22/17')
        elif inputdata[0] == '/Immediate item'  :
            bot.sendMessage(chat_id, '')
        elif inputdata[0] == '/Expiring item'  :
            bot.sendMessage(chat_id, '')


if __name__ == '__main__':
    
    BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # catch token
    with open(os.path.join(BASE_DIR, 'token.txt')) as f:
        TELEGRAM_BOT_TOKEN = f.read().strip() # Telegram Bot Token
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    print("I'm listening...")
    testurl = "\\villagerlimits.PNG"
    qrcode = 'test0999'
    chat_id_list = [] #'217724690','781745255',
    
    #getNewItem(chat_id_list,qrcode,testurl)
    #takeOffItem(chat_id_list,qrcode,testurl)
    # global variables
    itemString = ''
    totalList = []
    MessageLoop(bot,on_chat_message).run_as_thread()
    while 1:
        time.sleep(10)

