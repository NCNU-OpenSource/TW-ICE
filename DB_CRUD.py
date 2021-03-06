import mysql.connector
from mysql.connector import Error
import time, os
import datetime
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
table_name = 'test_proudct'

def connector():
    try:
        # connect to SQL
        connection = mysql.connector.connect(
            host='127.0.0.1',  # host ip address
            database='telebot', # database name
            user='TW_ICE_telebot', 
            password='your_password')

        if connection.is_connected():
            #print("already connected to database")
            return connection

    except Error as e:
        print("Connect failed : ", e)

def create_new_table():
    # connect database
    connection = connector()
    mycursor = connection.cursor()
    sql = "CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, serial_number VARCHAR(255), name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL, first_time DATETIME, recent_input_time DATETIME NULL, recent_output_time DATETIME NULL, expiration_date DATETIME NULL, photo_url VARCHAR(255), product_status BOOLEAN);"
    mycursor.execute( sql.format(table_name) )

    if (connection.is_connected()):
        mycursor.close()
        connection.close()
        #print("Database connect closed.")

def create_new_data_with_qrcode(qrcode_number, exp, URL):
    # Get time
    t = time.localtime()
    result = time.strftime('%Y-%m-%d %H:%M:%S', t)
    exp_time = datetime.datetime.now()+exp
    # connect SQL
    connection = connector()
    mycursor = connection.cursor()

    sql = "INSERT INTO {table} (serial_number, first_time, recent_input_time, expiration_date, photo_url, product_status) VALUES (%s, %s, %s, %s, %s, 1);"
    new_data = (str(qrcode_number), result, result, exp_time, URL)
    mycursor.execute(sql.format(table=table_name), new_data)
    connection.commit()

def read_all_data():
    connection = connector()
    mycursor = connection.cursor()
    sql = "SELECT * FROM {}"
    mycursor.execute(sql.format(table_name))
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return myresult

def read_data_in_ref():
    connection = connector()
    mycursor = connection.cursor()
    sql = "SELECT * FROM {} WHERE product_status = 1"
    mycursor.execute(sql.format(table_name))
    myresult = mycursor.fetchall()
    return myresult

def read_data_not_in_ref():
    connection = connector()
    mycursor = connection.cursor()
    sql = "SELECT * FROM {} WHERE product_status = 0"
    mycursor.execute(sql.format(table_name))
    myresult = mycursor.fetchall()
    return myresult

def read_specified_data_use_serial_number(serial_number):
    connection = connector()
    mycursor = connection.cursor()

    sql = "SELECT * FROM {} WHERE serial_number = %s"
    number = (str(serial_number),)
    mycursor.execute(sql.format(table_name), number)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return myresult

def read_specified_data_use_name(name):
    connection = connector()
    mycursor = connection.cursor()

    sql = "SELECT * FROM {} WHERE name = %s"
    number = (str(name),)
    mycursor.execute(sql.format(table_name), number)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return myresult

def update_data_use_serial_number(update_type,update_data,serial_number):
    connection = connector()
    mycursor = connection.cursor()
    if update_type == 1: # type 1 update name
        sql = "UPDATE {} SET name = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 2: # type 2 update first_time
        sql = "UPDATE {} SET first_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 3: # type 3 update recent_input_time
        sql = "UPDATE {} SET recent_input_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 4: # type 4 update recent_output_time
        sql = "UPDATE {} SET recent_output_time = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 5: # type 5 update expiration_date
        sql = "UPDATE {} SET expiration_date = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 6: # type 6 update photo_url
        sql = "UPDATE {} SET photo_url = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    elif update_type == 7: # type 7 update product_status
        sql = "UPDATE {} SET product_status = %s WHERE serial_number = %s"
        val = (update_data, serial_number)
    else:
        print("None type is {} , please choose again.".format(update_type))
        return 0

    mycursor.execute(sql.format(table_name), val)
    connection.commit()
        
def calculate_exp_notified_time():
    datalist = read_data_in_ref()
    exp_notify_list = []
    limit_time = datetime.timedelta(hours=8)
    limit_time2 = datetime.timedelta(hours=0)
    for item in datalist:
        if item[6]-datetime.datetime.now() < limit_time:
            if item[6]-datetime.datetime.now() > limit_time2:
                tmp = []
                tmp.append(item[1])
                tmp.append(str(item[6]-datetime.datetime.now()))
                tmp.append(item[7])
                exp_notify_list.append(tmp)
    return exp_notify_list

def calculate_exped_notified_time():
    datalist = read_data_in_ref()
    exped_notify_list = []
    limit_time = datetime.timedelta(hours=0)
    for item in datalist:
        if item[6]-datetime.datetime.now() < limit_time:
            tmp = []
            tmp.append(item[1])
            tmp.append(str(item[6]-datetime.datetime.now()))
            tmp.append(item[7])
            exped_notify_list.append(tmp)
    return exped_notify_list

def delete_data_use_serial_number(serial_number):
    connection = connector()
    mycursor = connection.cursor()
    delete_photo_url = BASE_DIR + "/picture/" + serial_number + ".jpg"
    os.remove(delete_photo_url)
    sql = "DELETE FROM {} WHERE serial_number = %s"
    number = (str(serial_number),)
    mycursor.execute(sql.format(table_name), number)
    connection.commit()
# create_new_table()  建立新資料表
