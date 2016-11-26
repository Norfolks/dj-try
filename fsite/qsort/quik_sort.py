from queue import Queue
import threading
import random
import copy
import time

n = 0
lock_n = threading.Lock()

def sort_worker(queue, arr):
    global n
    while True:
        r = queue.get()
        if r is None:
            return
        start, end = r
        element = arr[int((start + end)/2)]
        low = start
        high = end
        while low < high:
            while arr[low] < element:
                low += 1
            while arr[high] > element:
                high -= 1
            if low <= high:
                temp = arr[high]
                arr[high] = arr[low]
                arr[low] = temp
                low += 1
                high -= 1

        if high - start > 0:
            n += 1
            queue.put_nowait([start, high])
        if end - low > 0:
            n += 1
            queue.put_nowait([low, end])
        n -= 1
        if n == -1:
            queue.put_nowait(None)
            return


def parallel_quik_sort(arr_p_s, threads_number = 2):
    global n
    n = 0
    queue = Queue()
    threads = []
    for i in range(threads_number):
        threads.append(threading.Thread(target=sort_worker, args=(queue, arr_p_s,)))
        threads[-1].start()
    queue.put_nowait([0, len(arr_p_s) - 1])
    for thread in threads:
        thread.join()

def quik_sort(arr, start = 0, end = None):
    if end is None:
       end = len(arr) - 1
    element = arr[int((start + end) / 2)]
    low = start
    high = end
    while low < high:
        while arr[low] < element:
            low = low + 1
        while arr[high] > element:
            high = high - 1
        if low <= high:
            temp = arr[high]
            arr[high] = arr[low]
            arr[low] = temp
            low = low + 1
            high = high - 1
    if high - start > 0:
       quik_sort(arr, start, high)
    if end - low > 0:
        quik_sort(arr, low, end)



def count_sort_time(arr_check, sort_func):
    min_time = 2**32 - 1
    for _ in range(10):
        check_arr = copy.deepcopy(arr_s)
        start_time = time.time()
        sort_func(check_arr)
        end_time = time.time()
        if end_time - start_time < min_time:
            min_time = end_time - start_time
    return min_time

# length = 50000
# arr_s = list((random.randint(0, 1000) for _ in range(length)))
# print('start')
# print("Simple sort time: " + str(count_sort_time(arr_s, quik_sort)))
# print("Parallel sort time: " + str(count_sort_time(arr_s, parallel_quik_sort)))



