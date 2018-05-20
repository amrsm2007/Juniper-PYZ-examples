from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import multiprocessing
import time
NUM_PROCESSES = 2 # (2)
host="127.0.0.1"
USER = "root"
PASSWD = "root123"
PORTS = [
 "11",
 "12",
 "13",

]
DIRECTORY = "/var/tmp/"

out=open("C:\\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt",'w')

DIRECTORY = "/var/tmp/"
def check_directory_usage(port):




     with Device(host=host,user=USER,passwd=PASSWD,mode="telnet",port=port) as dev:
         fs = FS(dev)
         print("Checking %s: " % port,)
         print(fs.directory_usage(DIRECTORY))
         facts=dev.facts["hostname"]+" "+dev.facts["version"]
         isis=dev.cli("show configuration protocols isis | display set")
         out.write(facts)
         out.write(isis)


def main(): # (7)

    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool: # (8)
        process_pool.map(check_directory_usage, PORTS) # (9)
        process_pool.close() # (10)
        process_pool.join()
        out.close()
        print(" check data on following path \"C:\\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt\"")
        print("Finished in %f sec." % (time.time() - time_start)) # (11)
if __name__ == "__main__": # (12)

   main()


#out.close()

