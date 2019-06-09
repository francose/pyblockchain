'''
Author : Sadik Erisen
Date : Feb 2 2018
Purpose : This module creates a user object and data points .
'''

import sys


class data_package(object):

    def __init__(self ,gender, ssid, dob, income, annual_expense, current_credit_score, loan_term):
        self.dob = dob
        self.gender = gender
        self.ssid = ssid
        self.income = income
        self.annual_expense = annual_expense
        self.current_credit_score = current_credit_score
        self.loan_term = loan_term
        print ("object created \n")

    def user_info(self):
        print ('Gender : ', self.gender)
        print ('Date of Birth : ', self.dob)
        print ('Social Security Number : ', self.ssid)
        print ('Yearly Income : ', self.income)
        print ('Avg. Yearly Expense  : ', self.annual_expense)
        print ('Credit Score : ', self.current_credit_score)
        print ('Loan Term : ', self.loan_term)
