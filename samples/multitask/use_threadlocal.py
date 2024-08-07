import threading

local_school = threading.local()

def process_thread(name: str):
    local_school.student = name
    process_student()

def process_student():
    std = local_school.student
    print(f"Welcome {std}! (from {threading.current_thread().name})")

t1 = threading.Thread(target=process_thread, name='Thread-One', args=('Alice', ))
t2 = threading.Thread(target=process_thread, name='Thread-Two', args=('Bob', ))

t1.start()
t2.start()

t1.join()
t2.join()