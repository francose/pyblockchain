'''
Author : Sadik F. Erisen
Date : January 31th 2018
Purpose :
To be able to demonstrate object base data storage on different nodes.
Also be able to immitade the blockchain concept.

'''

#system files
import sys, random

# Modules
import create as c
import test as t
import data_pack as dp
import block
import block_params
import blockChain as BC


# Note when it creates the object it should also be store with hash number.
# Questions should be breaking apart in the dictionary.
# those max and min s should be our constant according to acculate.

def main():

    print ("Please select an option below: \n 1) Create test user\n 2) create user \n 0) Quit\n")
    user_input = input()
    print (user_input)

    if (user_input == '1'):
        test_case = BC()
        # print(test_case)
    elif (user_input == '2'):
        create = c.create_user()
    else:
        print("Exiting......\n")



if __name__ == '__main__':
    main()
