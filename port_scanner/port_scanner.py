from concurrent.futures import thread
from queue import Queue
import queue
import socket
import threading
from time import sleep

target = "127.0.0.1"
port_queue = Queue()
open_ports = []


def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        port_queue.put(port)


def worker():
    while not port_queue.empty():
        port = port_queue.get()
        if port_scan(port) is True:
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for i in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

for port in open_ports:
    print(f"port {port} is open !!")
