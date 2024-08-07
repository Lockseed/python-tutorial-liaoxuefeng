import re

s = '010-12345'
m = re.match(r'^(\d{3})-(\d{3,8})$', s)
print(f"Test: {s}")
print(m.group(1), m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(f"Test: {t}")
print(m.groups())

def is_valid_email(addr: str):
    if re.match(r'^[a-zA-Z0-9\.\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+$', addr):
        return True
    return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

import re

def name_of_email(addr):
    m = re.match(r'^\<(\w+\s?\w+)\>\s?[a-zA-Z0-9\.\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+$', addr)
    if m:
        return m.group(1)
    m = re.match(r'^([a-zA-Z0-9\.\_]+)\@[a-zA-Z0-9]+\.[a-zA-Z]+$', addr)
    if m:
        return m.group(1)
    return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')