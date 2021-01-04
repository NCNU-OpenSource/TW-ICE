import mysql.connector
from mysql.connector import Error
import time, os
# -*- coding: utf-8 -*-
#TODO:輸出格式的規格化
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#目前只使用一個table,方便管理將名字打在這邊,倘若未來有所擴增table可直接帶入其他名稱。
table_name = 'test_proudct'

def connector():
    try:
        # 連接 MySQL/MariaDB 資料庫
        connection = mysql.connector.connect(
            host='10.33.20.8',  # 主機名稱
            database='telebot', # 資料庫名稱
            user='TW_ICE_telebot', # 帳號
            password='lsa4')  # 密碼

        if connection.is_connected():
            print("已連接上資料庫")
            return connection

    except Error as e:
        print("資料庫連接失敗：", e)

def create_new_table():
    
    #連線SQL
    connection = connector()
    mycursor = connection.cursor()
    sql = "CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, serial_number VARCHAR(255), name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL, first_time DATETIME, recent_input_time DATETIME NULL, recent_output_time DATETIME NULL, expiration_date DATETIME NULL);"
    mycursor.execute( sql.format(table_name) )
    #mycursor.execute("CREATE TABLE test_proudct (id INT AUTO_INCREMENT PRIMARY KEY, serial_number VARCHAR(255), name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL, first_time DATETIME, recent_input_time DATETIME NULL, recent_output_time DATETIME NULL, expiration_date DATETIME NULL)")

    if (connection.is_connected()):
        mycursor.close()
        connection.close()
        print("資料庫連線已關閉")

def create_new_data_with_qrcode(qrcode_number):
    
    # 取得本地時間&輸入時間格式
    t = time.localtime()
    result = time.strftime('%Y-%m-%d %H:%M:%S',t)

    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()

    # 第一次進入只會有 流水號、第一次放入時間、最近一次放入時間被登入
    sql = "INSERT INTO {} (serial_number, first_time, recent_input_time) VALUES (%s, %s, %s);"
    new_data = (str(qrcode_number), result, result)
    mycursor.execute(sql.format(table_name), new_data)

    # 確認資料有存入資料庫
    connection.commit()

def read_all_data():
    
    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()
    sql = "SELECT * FROM {}"
    mycursor.execute(sql.format(table_name))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def read_specified_data_use_serial_number(serial_number):
    
    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()

    sql = "SELECT * FROM {} WHERE serial_number = %s"
    number = (str(serial_number),)
    mycursor.execute(sql.format(table_name), number)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def read_specified_data_use_name(name):
    
    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()

    sql = "SELECT * FROM {} WHERE name = %s"
    number = (str(name),)
    mycursor.execute(sql.format(table_name), number)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def update_data_use_serial_number(update_type,update_data,serial_number):
    
    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()
    if update_type == 1: # type 1 更新name
        sql = "UPDATE {} SET name = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 2: # type 2 更新first_time
        sql = "UPDATE {} SET first_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 3: # type 3 更新recent_input_time
        sql = "UPDATE {} SET recent_input_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 4: # type 4 更新recent_output_time
        sql = "UPDATE {} SET recent_output_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 5: # type 5 更新expiration_date
        sql = "UPDATE {} SET expiration_date = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    else:
        print("None type is {} , please choose again.".format(update_type))
        return 0

    mycursor.execute(sql.format(table_name), val)

    # 確認資料有存入資料庫
    connection.commit()

def delete_data_use_serial_number(serial_number):

    # 連線SQL
    connection = connector()
    mycursor = connection.cursor()

    sql = "DELETE FROM {} WHERE serial_number = %s"
    number = (str(serial_number),)
    mycursor.execute(sql.format(table_name), number)

    # 確認資料有存入資料庫
    connection.commit()
