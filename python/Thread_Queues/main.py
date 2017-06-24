from Queue import Queue
import threading
import time, os

NUM_THREADS = 2
print_lock = threading.Lock()
q = Queue()

def process(job):
    count = 0
    while count < 10:
        time.sleep(0.5)
        count += 1
        with print_lock:
            print("{} - {} - {}".format(threading.current_thread().name, job, count))
    with print_lock:
        print("{} finished".format(job))

def threader():
    while True:
        job = q.get()
        process(job)
        q.task_done()

def main():
    q.put("job1")
    q.put("job2")
    q.put("job3")

    for x in range(NUM_THREADS):
        t = threading.Thread( target = threader )
        t.start()

    start = time.time()    
    
    q.join()

    print("Queue processed in {} seconds.".format(time.time()-start))

if __name__ == "__main__":
    main()