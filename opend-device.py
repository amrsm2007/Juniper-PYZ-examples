from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from getpass import getpass
import sys

out=open("C:\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt",'w')
x=11
while x<=13:

     dev=Device(host="127.0.0.1",user="root",passwd="root123",mode="telnet",port=str(x))
     dev.open()
     print dev.facts
     print type(dev.facts)
     facts=dev.facts["hostname"]+" "+dev.facts["version"]
     isis=dev.cli("show configuration protocols isis | display set")
     out.write(facts)
     out.write(isis)


     #print dev.rpc.get_isis_adjacency_information()
     dev.close()
     x+=1
out.close()
print " check data on following path \"C:\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt\""

