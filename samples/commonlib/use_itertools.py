import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

import itertools

def pi_1(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_numbers = itertools.count(1, 2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_numbers_n = itertools.islice(odd_numbers, 0, N)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    pi_item_iter = (4/x if i%2==0 else -4/x for i, x in enumerate(odd_numbers_n))

    # step 4: 求和:
    return sum(pi_item_iter)

def pi(N):
    sum_pi = 0  # 初始化求和结果
    for k in range(N):
        sum_pi += ((-1)**k) / (2 * k + 1)  # 每一项的计算并累加
    return 4 * sum_pi  # 返回 π 的近似值，不要忘记乘以 4

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')