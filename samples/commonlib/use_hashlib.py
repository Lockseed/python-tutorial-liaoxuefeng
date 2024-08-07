import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sh1 = hashlib.sha1()
sh1.update('how to use md5 '.encode('utf-8'))
sh1.update('in hashlib?'.encode('utf-8'))
print(sh1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user: str, password: str):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if db[user] == md5.hexdigest():
        return True
    return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# db = {}

# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')

import hashlib, random

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = self.get_md5(password + self.salt)

    def get_md5(self, s: str):
        return hashlib.md5(s.encode('utf-8')).hexdigest()

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def get_md5(user: User, pws: str):
    return user.get_md5(pws + user.salt)

def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')