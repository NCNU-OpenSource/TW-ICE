import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup as InlineMarkup
from telepot.namedtuple import InlineKeyboardButton as InlineBtn
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

# def getNewItem():
#     url = BASE_DIR + "\\villagerlimits.PNG"
#     inlineBtns = [
#                     [[InlineKeyboardButton(text="btn1",callback_data='I have Nothing To do'), InlineKeyboardButton(text="btn2",callback_data='0'),InlineKeyboardButton(text="btn3",callback_data='0'), InlineKeyboardButton(text="btn4",callback_data='0')]
#                 ]
#     bot.sendPhoto("781745255", photo=open(url, 'rb'), reply_markup = InlineKeyboardMarkup(inline_keyboard= inlineBtns))

def on_chat_message(msg):
    global itemString,chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
        pprint(msg)
        chat_id = msg['chat']['id']
        print(chat_id)
        from_id = msg['from']['id']
        if msg['text'] == '/help' :
            replyBtns = [
                    [Btn(text='/show')],
                    [Btn(text='/add'), Btn(text='/update'), Btn(text='/vol_up')],
                ]
            time.sleep(1)
            bot.sendMessage(chat_id, 'Here\'s all function buttons', reply_markup=ReplyMarkup(keyboard=replyBtns))

        elif msg['text'] == '/show' :
            test = ''
            test = getItemList()
            print(type(test))
            print(test)
            bot.sendMessage(chat_id, test)
        elif msg['text'] == '/update' :
            url = BASE_DIR + "\\villagerlimits.PNG"
            bot.sendPhoto(chat_id, photo=open(url, 'rb'))
        elif msg['text'] == '/add'  :
            bot.sendMessage(chat_id, "3")

if __name__ == '__main__':
    
    BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # catch token
    with open(os.path.join(BASE_DIR, 'token.txt')) as f:
        TELEGRAM_BOT_TOKEN = f.read().strip() # Telegram Bot Token
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    #bot.sendMessage("781745255", "hello")
    print("I'm listening...")

    # global variables
    totalList = db.read_all_data()
    #print(totalList)
    itemString = '條碼號 品名' + '\n'
    chat_id=''
    getNewItem()
    MessageLoop(bot,on_chat_message).run_as_thread()
    while 1:
        time.sleep(10)



# def updateItemName()

# def updateItemExpirationDate()

    #text = msg['text']
    #bot.sendMessage(chat_id, text)

    #photo = 'https://imgur.com/gallery/UoGUPux'
    #bot.sendPhoto(chat_id, photo)








