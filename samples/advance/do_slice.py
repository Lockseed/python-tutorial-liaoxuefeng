
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3]) # 从索引0开始取，直到索引3为止，但不包括索引3
print('L[:3] =', L[:3]) # 如果第一个索引是0，还可以省略
print('L[1:3] =', L[1:3]) # 也可以从索引1开始，取出2个元素出来
print('L[-2:] =', L[-2:]) # 取倒数两个元素

R = list(range(100))
print('R[:10] =', R[:10]) # 取前10个数
print('R[-10:] =', R[-10:]) # 取后10个数
print('R[10:20] =', R[10:20]) # 取前11-20个数
print('R[:10:2] =', R[:10:2]) # 前10个数，每两个取一个
print('R[::5] =', R[::5]) # 所有数，每5个取一个

def trim(s):
    if not s:
        return s
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')