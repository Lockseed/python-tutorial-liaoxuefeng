from multiprocessing import Process, Queue
import os, time, random

def write(q: Queue):
    print(f"Process to write: {os.getpid()}")
    for value in ['A', 'B', 'C']:
        print(f"Put {value} to queue...")
        q.put(value)
        time.sleep(random.random())

def read(q: Queue):
    print(f"Process to read: {os.getpid()}")
    while True:
        value = q.get(True)
        print(f"Get {value} from queue...")

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()