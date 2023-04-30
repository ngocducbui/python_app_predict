import json
import os
import re
import random
import string
from datetime import datetime as dt
from PyQt5 import QtWidgets


def check_empty(text):
    if len(text) != 0:
        return True
    else:
        return False


def create_folder():
    if os.path.exists('Output'):
        None
    else:
        folder_path = 'Output'
        os.mkdir(folder_path)


def check_phone(string_phone):
    try:
        phone = int(string_phone)
        if re.search('^[0-9]{10}$', string_phone):
            return True
        else:
            return False
    except:
        return False


def check_email(string_email):
    try:
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', string_email):
            return True
        else:
            return False
    except:
        return False


def split_date_time():
    date_time = str(dt.now())
    date_split = date_time.split(' ')
    (h, mi, s) = date_split[1].split(':')
    (y, m, d) = date_split[0].split('-')
    return d, m, y, h, mi, s


def divide_chunks(list_data, number):
    for i in range(0, len(list_data), number):
        yield list_data[i:i + number]


def check_exit_file(file_path):
    if not os.path.exists(file_path):
        print(file_path + " is not exit")
        return False
    else:
        return True


def load_config(config_path):
    data = None
    if check_exit_file(config_path):
        with open(config_path, 'r', encoding='cp932', errors='ignore') as config_file:
            data = json.load(config_file)
        return data
    else:
        return False


def open_note_pad(path):
    cmd_string = 'notepad.exe ' + path
    os.system(cmd_string)


def open_dialog_file(file_type="Excel (*.xlsx );;All Files (*)"):
    QFileDialog = QtWidgets.QFileDialog()
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(QFileDialog, "Select File", os.path.expanduser('.'),
                                              file_type, options=options)
    if fileName:
        print(fileName)
        return fileName
    else:
        return None


def random_password():
    source = string.ascii_lowercase + string.digits
    result = ''.join((random.choice(source) for i in range(6)))
    return result


def divide_chunks(list_data, number):
    for i in range(0, len(list_data), number):
        yield list_data[i:i + number]


def get_path(name):
    filename = str(dt.now())
    filename = re.sub("[-\s:]", '_', filename)
    filename = re.findall("[_\d]+", filename)
    filename = '../Output/' + name + '_' + filename[0] + '.xlsx'
    return filename


def data_to_excel(name, df):
    try:
        if not os.path.exists('../Output'):
            os.mkdir('../Output')
        filename = get_path(name)
        df.to_excel(filename)
        return True
    except:
        print('Error')
        return False

def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata=file.read()
        return binarydata

def createList(number):
    return [item for item in range(1, number+1)]

def compare(lista, listb):
    count=0
    for i in range(len(lista)):
        for j in range(len(listb)):
            if i == j:
                if lista[i] == listb[j]:
                    count += 1
    return count