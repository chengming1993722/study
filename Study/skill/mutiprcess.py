import multiprocessing

g_queue = multiprocessing.Queue()
def init_queue():
    print("init g_queue start ")
    while not g_queue.empty():
        g_queue.get()
    for _index in range(10):
        g_queue.put(_index)
    print('init g_queue end')
    return
