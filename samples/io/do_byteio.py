from io import BytesIO

f = BytesIO()
f.write(b'Hello')
f.write(b' ')
f.write(b'World!')
print(f.getvalue().decode())

data = '万里悲秋常作客，\n百年多病独登台。\n艰难苦恨繁霜鬓，\n潦倒新停浊酒杯。\n'.encode('utf-8')
f2 = BytesIO(data)
print(f2.read().decode())