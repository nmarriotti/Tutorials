from Queue import Queue
import time


def process(job):
    count = 0
    while count < 10:
        time.sleep(0.5)
        count += 1
        print("processing {}".format(job))
    print("{} finished".format(job))

def main():
    q = Queue()

    q.put("job1")
    q.put("job2")
    q.put("job3")

    start = time.time()
    while not q.empty():
        process(q.get())
    print("Queue processed in {} seconds.".format(time.time()-start))

if __name__ == "__main__":
    main()