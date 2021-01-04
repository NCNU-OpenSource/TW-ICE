import telepot
import time
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
    if totalList:
        for item in totalList:
            tmp = item  # tmp[0]: pk, tmp[1]: Bar code, tmp[2]: item name
            # if item without item name
            if tmp[2] == None:
                itemString = itemString + tmp[1] + ' ' + 'None' + '\n'
            else:
                itemString = itemString + tmp[1] + ' ' + tmp[2] + '\n'
    # nothing in the refrigerator
    else:
        itemString =  "There is Nothing in the refrigerator :("
    return itemString

# def updateItem(barcode,itemname,expirationDate)
#     update_data_use_serial_number(1,itemname,barcode)
#     update_data_use_serial_number((5,itemname,barcode))

# wait for the part of web cam
def getNewItem(chat_id_list,barcode,url):
    openurl = BASE_DIR + url
    for i in chat_id_list:
        bot.sendPhoto(i, photo=open(openurl, 'rb'), caption = 'There is a new item: ' + barcode + ' !')

def on_chat_message(msg):
    global itemString,chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    ## 
    inputdata = msg['text'].split() 
    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
        #pprint(msg)
        chat_id = msg['chat']['id']
        print(chat_id)
        from_id = msg['from']['id']
        if inputdata[0] == '/help' :
            replyBtns = [
                    [Btn(text='/show')],
                    [Btn(text='/add'), Btn(text='/updateInfo'), Btn(text='/delete')],
                    [Btn(text='/Immediate item'), Btn(text='/Expiring item')]
                ]
            time.sleep(1)
            bot.sendMessage(chat_id, 'Here\'s all function buttons', reply_markup=ReplyMarkup(keyboard=replyBtns))

        elif inputdata[0] == '/show' :
            test = ''
            test = getItemList()
            print(type(test))
            print(test)
            bot.sendMessage(chat_id, test)
        elif inputdata[0] == '/updateInfo' :
            #if(len(inputdata)<3)
                bot.sendMessage(chat_id, "3")
        elif inputdata[0] == '/add'  :
            bot.sendMessage(chat_id, "3")

if __name__ == '__main__':
    
    BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # catch token
    with open(os.path.join(BASE_DIR, 'token.txt')) as f:
        TELEGRAM_BOT_TOKEN = f.read().strip() # Telegram Bot Token
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    print("I'm listening...")
    testurl = "\\villagerlimits.PNG"
    barcode = 'test0999'
    chat_id_list = {'217724690'} #'781745255',
    getNewItem(chat_id_list,barcode,testurl)

    # global variables
    totalList = db.read_all_data()
    itemString = '條碼號 品名' + '\n'
   
    #MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()
    MessageLoop(bot,on_chat_message).run_as_thread()
    while 1:
        time.sleep(10)




# url = BASE_DIR + "\\villagerlimits.PNG"
            # barcode = 'test0999'
            # bot.sendPhoto(chat_id, photo=open(url, 'rb'), caption = 'There is a new item: ' + barcode + ' !')






