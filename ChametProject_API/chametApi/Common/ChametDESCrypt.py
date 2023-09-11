import base64
import json
import re
from Crypto.Cipher import DES


# PKCS#5填充的函数
# 作用是在数据末尾添加指定数量的填充字节，以满足加密算法对数据长度的要求。
def _pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data + padding

# 判断字符串是否为json格式
def isJson(s):
    try:
        json_object = json.loads(s)
    except ValueError as e:
        return False
    return True


# 匹配ASCII控制字符的正则表达式
control_char_regex = re.compile(r'[\x00-\x1f\x7f-\x9f]')


class ChametDESCrypt:  # 自己实现的DES加密类
    # 构造方法 可以指定加密key 或使用默认key 并指定了加密模式为DES.MODE_ECB 后面可以自己改
    def __init__(self, key = ''):
        if key != '':
            self.key = key.encode('utf-8')
        else:
            self.key = '37ad9f8e'.encode('utf-8')
        self.mode = DES.MODE_ECB

    def encrypt(self, data):
        if data is None:
            return None
        # 构造加密对象
        des_key = DES.new(self.key, self.mode)
        # PKCS#5填充的函数  在数据末尾添加指定数量的填充字节
        padded_data = _pad(data.encode(), DES.block_size)
        # 使用加密对象加密数据
        encrypted_data = des_key.encrypt(padded_data)
        # 将加密后的数据base64再加密后返回
        return base64.b64encode(encrypted_data).decode()

    def decrypt(self, data):
        if data is None:
            return ""
        # 兼容一下 有的账号服务端返回的是json 有的账号是密文
        if isJson(data):
            return data
        # 构造解密对象
        des_key = DES.new(self.key, self.mode)
        # 将需要解密的数据先base64解密
        encrypted_data = base64.b64decode(data)
        # 将base64解密的数据使用解密对象再解密
        decrypted_data = des_key.decrypt(encrypted_data)
        # # 将得到的byte数组转为字符串返回
        # return decrypted_data.decode('utf-8').rstrip()
        # 去除解密后字符串末尾的空白字符和ASCII控制字符
        cleaned_data = control_char_regex.sub('', decrypted_data.decode('utf-8').rstrip())
        return cleaned_data

# des = ChametDESCrypt('37ad9f8e')
# # e = des.encrypt('12345678')
# d = des.decrypt('qxkLE8CfrPnbUjNQui6iN1HOBwdYWhC59QroDrMr/mu2RHzrTOmqNtVN5M3ZGstK')
# # print(e)
# print(d)

# {
#   "msg": "success",
#   "result": 1000,
#   "info": {
#     "needBindPhone": 0,
#     "sessionKey": "2FE9474242AE8C83ECDC74819992BA8C",
#     "ryUserId": "try2011074",
#     "sex": 1,
#     "loginToken": "b6aac8165fa348158c9d343058121d35",
#     "ryLoginToken": "mr2Pbs1FY3mjd7uU4yMOMPTPsmo2hOBlMI7qbtmbktQ\u003d@n1ls.sg.rongnav.com;n1ls.sg.rongcfg.com",
#     "imType": 1,
#     "userid": 2011074,
#     "defaultNav": 2,
#     "totalFuncFlag": 1,
#     "yxLoginToken": "dc9bdf6626b7a9f079fd53c0ff1826f7",
#     "defaultLive": 2,
#     "openLiveRoom": 1,
#     "yxAccount": "tac2011074"
#   }
# }
# s = '{"identification":"2123123121","loginToken":"f788aec2bd4c46b5b44c0d831c7e1e21","sign":"1111","userid":2000004}'
# print(des.encrypt(s))
