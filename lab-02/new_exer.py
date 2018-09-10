import multiprocessing
import os


def print_os_info():
    print multiprocessing.cpu_count() 
    print os.uname()
    print os.system('df -h')
    print os.system('uptime')

print_os_info()

