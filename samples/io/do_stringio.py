from io import StringIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())

f2 = StringIO('风急天高猿啸哀，\n渚清沙白鸟飞回。\n无边落木萧萧下，\n不尽长江滚滚来。')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())