from typing import Optional
def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s: Optional[str]):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def is_palindrome(n: int):
    n_str = str(n)
    # length = len(n_str)
    # mid_index = length // 2
    # result = True
    # for i in range(mid_index):
    #     if n_str[i] != n_str[length - i - 1]:
    #         result = False
    #         break
    # return result
    '''
    在 [::-1] 中，start 和 stop 都被省略了，表示从开始到结束。
    -1 是 step，表示步长为 -1，也就是从后向前取，因此 n_str[::-1] 就表示反转 n_str。
    '''
    return n_str == n_str[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')