import time
import queue
from codetiming import timer


def task(name, queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:1f}}")
    while not queue.empty():
        delay = queue.get()
        print(f"Task {name} running ")
        timer.start()
        timer.sleep(delay)
        timer.stop()
        yield
def main():
    work_queue = queue.Queue()
    for work in [15,10,5,2]:
        work_queue.put(work)
    tasks = Task(task("One",work_queue), task("Two",work_queue))
    done = False
    