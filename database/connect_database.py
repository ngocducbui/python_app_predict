import config
import json
import os
import mysql.connector
from mysql.connector import errorcode
import numpy
from datetime import datetime
import re
import common as cm

DATABASE_CONFIG_PATH = '../config/database_config.json'
data_config = cm.load_config(DATABASE_CONFIG_PATH)
try:
    cnx = mysql.connector.connect(
        host=data_config['host'],
        user=data_config['user'],
        password=data_config['password'],
        port=data_config['port'],
        database=data_config['database']
    )
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("data does not exist")
    else:
        print(err)
else:
    print("Connection database successfully")


def add_user(username, role):
    query = "UPDATE final_project.`user` " \
            f"SET role= '{role}' WHERE username='{username}';"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def login(username, password):
    try:
        query = f"select * from final_project.`user` where username ='{username}' and password ='{password}'"
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def login_2(username, password):
    try:
        query = f"select role from final_project.`user` where username ='{username}' and password ='{password}'"
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def login_3(username, password):
    try:
        query = f"select role,name,id from final_project.`user` where username ='{username}' and password ='{password}'"
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def register(name, dob, phone, email, address, username, password, role, BinaryData):
    query = "INSERT INTO final_project.user (name, `date-of-birth`, phone, email, Address, username, password, `role`, image) " \
            " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = (name, dob, phone, email, address, username, password, role, BinaryData)
    try:
        cursor.execute(query,args)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def select_id_to_reset_password(name, username, phone, email):
    query = f"select id from final_project.`user` where name='{name}' and phone='{phone}' and email ='{email}' and username='{username}'"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def reset_password(id, new_pass):
    query = f"UPDATE final_project.`user` SET password='{new_pass}' WHERE id={id}"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def select_data_user():
    query = "select * from final_project.user"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def edit_admin(id, name, dob, email, address, username):
    query = "UPDATE final_project.`user` " \
            f"SET name='{name}', `date-of-birth`='{dob}', email='{email}', Address='{address}', username='{username}' WHERE id={id};"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def delete_data(id):
    query = f"DELETE FROM final_project.`user` WHERE id={id};"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def search_user(name):
    query = f"select *  from final_project.`user`  where name like '%{name}%'"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def count_number():
    query = "select count(id) from final_project.`user`"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def select_user_by_id(id):
    query = f"select * from final_project.user where id={id}"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        result = numpy.array(data)
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
    return result


def change_password(id, password):
    query = f"UPDATE final_project.`user` SET  password='{password}' WHERE id={id};"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False


def update_profile(id, name, phone, email, address, username, password, dob):
    query = "UPDATE final_project.`user` " \
            f"SET name='{name}', `date-of-birth`='{dob}', phone='{phone}', email='{email}', Address='{address}', username='{username}', password='{password}' " \
            f"WHERE id={id};"
    try:
        cursor.execute(query)
        cnx.commit()
        return True
    except mysql.connector.Error as err1:
        print("Fail: {}".format(err1))
        return False
