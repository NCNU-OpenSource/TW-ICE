import time, os,datetime
import DB_CRUD as db
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
def take_out(qrcode_number):
    t = time.localtime()
    take_out_status = '0'
    result = time.strftime('%Y-%m-%d %H:%M:%S', t)
    db.update_data_use_serial_number(4,result,qrcode_number)
    db.update_data_use_serial_number(7,take_out_status,qrcode_number)
def put_in_again(qrcode_number):
    t = time.localtime()
    put_in_status = '1'
    result = time.strftime('%Y-%m-%d %H:%M:%S', t)
    db.update_data_use_serial_number(3,result,qrcode_number)
    db.update_data_use_serial_number(7,put_in_status,qrcode_number)
def check_data(qrcode_number):
    if db.read_specified_data_use_serial_number(qrcode_number): # data is exist
        if db.read_specified_data_use_serial_number(qrcode_number)[0][8] == 1:
            take_out(qrcode_number)
            return int(2)
        elif db.read_specified_data_use_serial_number(qrcode_number)[0][8] == 0:
            put_in_again(qrcode_number)
            return int(3)
    else: # data is not exist
        photoURL = BASE_DIR + '\\photo\\' + qrcode_number
        exptime = 0
        if qrcode_number[0] == 'A':
            exptime = datetime.timedelta(hours=8)
        elif qrcode_number[0] == 'B':
            exptime = datetime.timedelta(hours=16)
        elif qrcode_number[0] == 'C':
            exptime = datetime.timedelta(hours=24)
        elif qrcode_number[0] == 'D':
            exptime = datetime.timedelta(hours=36)
        elif qrcode_number[0] == 'E':
            exptime = datetime.timedelta(hours=48)
        else:
            print('data format error')
            return 0
        db.create_new_data_with_qrcode(qrcode_number, exptime, photoURL)
        return int(1)

# a = 'B002'
# b = check_data(a)
# if b == 1:
#     print('new data')
# elif b == 2:
#     print('take out')
# elif b == 3:
#     print('put in')
# else:
#     print('error')
