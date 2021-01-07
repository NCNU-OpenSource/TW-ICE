import DB_CRUD as db
import time
import datetime
import os
def delete_proudct_out_off_time():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    datalist = db.read_data_not_in_ref()
    limit_time = datetime.timedelta(days=3)
    for item in datalist:
        if datetime.datetime.now()-item[5] > limit_time:
            db.delete_data_use_serial_number(item[1])