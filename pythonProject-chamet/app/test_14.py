import logging


def inputPassword(str):
    strList=['123','234','myp']
    if(str in strList):
        return True
    else:
        return False

def inputPhoneNumber(num):
    strList=['18868104086','18868116055']
    if(num in strList):
        return True
    else:
        return False

try:
    a=input('please input your phone number\n')
    if(inputPhoneNumber(a)):
        judge_in_step1='already zhuce'
    else:
        judge_in_step1='not zhuce'
        temp = input('nuw zhuce?y/n')

except:
    print('error in input phone number !')
    judge_in_step1='phone number error'

try:
    if(judge_in_step1=='already zhuce'):
        a=input('please input your password\n')
        if(inputPassword(a)):
            judge_in_step2='success'
            print('success')
        else:
            judge_in_step2='fail'
            print('failed')
except:
    print('input password error');
    judge_in_step2='input password error'