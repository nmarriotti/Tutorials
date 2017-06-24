import time
from threading import Thread

def print_stuff(threadName, delay):
    count = 0
    while count<10:
        time.sleep(delay)
        count += 1
        print("{} count is {}".format(threadName, count))
    print("{} completed".format(threadName))

def main():
    t = Thread(target=print_stuff, args=("Thread-1", 2))
    t.start()
    t1 = Thread(target=print_stuff, args=("Thread-2", 4))
    t1.start()


if __name__ == "__main__":
    main()