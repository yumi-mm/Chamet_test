# print('\ufffd')
# print('bgfbf'+'\u2006'+'dewfre')
# print('\U0001f1e8')
# 28,216[diamond]
# print(int(216)<int(2,000))
import re
#
# text = "28,216[diamond]"
# result = re.findall("\d+", text)
# print(result)  # 输出：['123']
# print(type(result))
# print(len(result))
# print(result[0])
# num=''.join(result)
# print(num)
# print(type(num))
# login_phone='8618****0000'
# login_phone_num = login_phone.replace('*', '')
# print(login_phone_num)

# my_Tasks_entryTwoText1 ='1,060 [points]'
# my_Tasks_entryTwoText=my_Tasks_entryTwoText1.replace(',','')
# print(my_Tasks_entryTwoText)

# 我的背包
'''ccc='进场效果(1)'
# aaa=re.search("\d+", ccc)
aaa=int(re.findall("\d+", ccc)[0])

print(aaa)
# print(aaa[0])
# print(type(aaa[0]))

ccc1='头像框(3)'
# aaa=re.search("\d+", ccc)
aaa1=int(re.findall("\d+", ccc1)[0])
print(aaa1)
# print(aaa1[0])
# print(type(aaa1[0]))
c=int(aaa)+int(aaa1)
print(c)'''

# 我的任务
'''
my_Tasks_entryTwoText='2,725 [points]'
aaa1 = re.findall("\d+", my_Tasks_entryTwoText)
num = ''.join(aaa1)
print(num)
my_Tasks_entryTwoText11='{}''\x20''[points]'.format(num)
print(my_Tasks_entryTwoText11)
'2725 [points]'
# ccc1='2,725 [points]'
# aaa1=re.findall("\d+", ccc1)
# num=''.join(aaa1)
# print(num)'''