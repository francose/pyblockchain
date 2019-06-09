'''
Author : Sadik Erisen
Date : Feb 2 2018
Purpose : This module creates a test_user and fills out data points .
'''

import sys, random
import data_pack as dp


def create_test_users():

    #for random dob
    for i in range(0,10):
        randomId = random.randint(10000,90000)
        date = random.randint(1,31)
        month = random.randint(1,12)
        year = random.randint(1930,2017)
        newDob = "%s, %s, %s" % (date, month, year)

    #for random ssid
    for i in range(0,11):
        randomId = random.randint(10000,90000)
        first = random.randint(100,999)
        second = random.randint(10,99)
        third = random.randint(0,10000)
        ssid = "%s, %s, %s" % (first, second, third)

    #for random gender
    g = ['male', 'female']
    for x in range(0,2):
        test = random.randint(0,2)
        for y in range(0,test):
            gender = g[y]

    #for random weeks
    for week in range(0,7):
        ran_week = random.randint(1,5)

    for inc in range(0,15):
        _newinc = random.randint(3000,100000)

    for score in range(0,15):
        _newscore = random.randint(400,1500)

    for expense in range(0,15):

        _newexp = random.randint(1000,55000)

    testing_data = dp.data_package(gender, ssid ,newDob,_newinc, _newexp, _newscore, ran_week)
    details = dp.data_package.user_info(testing_data)
    return details
