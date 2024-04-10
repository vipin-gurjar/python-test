import multiprocessing
import time

def worker_function(name, duration):
    print(f"{name} started")
    time.sleep(duration)
    print(f"{name} finished")

if __name__ == "__main__":
    processes = []

    tasks = [("Task 1", 2), ("Task 2", 3), ("Task 3", 1)]

    for task in tasks:
        p = multiprocessing.Process(target=worker_function, args=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")
