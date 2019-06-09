'''
Author : Sadik Erisen
Date : Feb 2 2018
Purpose : This module creates a user by manual entry.
'''
import sys, random
import data_pack as dp

def create_user():

    print ('Gender : ')
    gender = input()
    print ('Date of Birth : ')
    dob = input()
    print ('Social Security Number : ')
    ssid = input()
    print ('Yearly Income : ')
    y_i = input()
    print ('Avg. Yearly Expense  : ')
    a_e = input()
    print ('Credit Score : ')
    c_c_s = input()
    print ('Loan Term : ')
    l_t = input()

    data = dp.data_package(gender, ssid ,dob,y_i, a_e, c_c_s, l_t)
    return data.user_info
