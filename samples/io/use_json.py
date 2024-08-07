import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print(f"json str is {data}")
reborn = json.loads(data)
print(f"reborn is {reborn}")

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "Student object (%s %s %s)" % (self.name, self.age, self.score)
    
s = Student('Bob', 20, 88)
s_dump = json.dumps(s, default=lambda obj: obj.__dict__)
print(f"Dump student: {s_dump}")
rebuild = json.loads(s_dump, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)