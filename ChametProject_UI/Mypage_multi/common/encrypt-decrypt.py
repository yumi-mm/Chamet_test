import base64
from Cryptodome.Cipher import DES


# PKCS5填充的函数
# 作用是在数据末尾添加指定数量的填充字节，以满足加密算法对数据长度的要求。
def _pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data + padding


class MyDESCrypt:  # 自己实现的DES加密类
    # 构造方法 可以指定加密key 或使用默认key 并指定了加密模式为DES.MODE_ECB 后面可以自己改
    def __init__(self, key=''):
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
        # 构造解密对象
        des_key = DES.new(self.key, self.mode)
        # 将需要解密的数据先base64解密
        encrypted_data = base64.b64decode(data)
        # 将base64解密的数据使用解密对象再解密
        decrypted_data = des_key.decrypt(encrypted_data)
        # 将得到的byte数组转为字符串返回
        return decrypted_data.decode('utf-8')


if __name__ == '__main__':
    des = MyDESCrypt("")
    e = des.encrypt("123")
    d = des.decrypt(e)
    print("加密123后得到" + e)
    print("解密后得到" + d)
