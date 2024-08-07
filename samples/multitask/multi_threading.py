import time, threading

def loop():
    print(f"Thread {threading.current_thread().name} is running...")
    
    n = 0
    while n < 5:
        n = n + 1
        print(f"Thread {threading.current_thread().name} >>> {n}")
        time.sleep(1)

    print(f"Thread {threading.current_thread().name} ended.")


print(f"Thread {threading.current_thread().name} is running...")

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()

print(f"Thread {threading.current_thread().name} ended.")