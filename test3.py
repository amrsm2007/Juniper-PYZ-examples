from jnpr.junos import Device # (1)
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import multiprocessing
import time
NUM_PROCESSES = 1 # (2)
host="127.0.0.1"
USER = "root"
PASSWD = "root123"
PORTS = [
 "11",
 "12",
 "13",

]
DIRECTORY = "/var/tmp/"
def check_directory_usage(port): # (3)

 try:

     with Device(host=host, user=USER, password=PASSWD,mode="telnet",port=port) as dev:

         fs = FS(dev) # (4)
         print("Checking %s: " % port,)
         print(fs.directory_usage(DIRECTORY)) # (5)
 except ConnectRefusedError: # (6)
     print("%s: Error - Device connection refused!" % port)
 except ConnectTimeoutError:
     print("%s: Error - Device connection timed out!" % port)
 except ConnectAuthError:
     print("%s: Error - Authentication failure!" % port)
def main(): # (7)

    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool: # (8)
        process_pool.map(check_directory_usage, PORTS) # (9)
        process_pool.close() # (10)
        process_pool.join()
        print("Finished in %f sec." % (time.time() - time_start)) # (11)
if __name__ == "__main__": # (12)

  main()