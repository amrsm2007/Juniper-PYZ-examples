from jnpr.junos import Device
import time
from pprint import pprint
from lxml import etree
time_start = time.time()

devices="C:\\Users\Amr Ali\PycharmProjects\Juniper-PYZ\devices.txt"
out=open("C:\\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt",'w')
with open(devices,'r')as f:
     ports=f.readlines()
     ports=[x.strip() for x in ports]

pprint (ports)
for port in ports :

    with Device(host="127.0.0.1",user="root",passwd="root123",mode="telnet",port=port) as dev:
     #print (dev.facts)
     facts=dev.facts["hostname"]+" "+dev.facts["version"]
     #host=dev.rpc.get_isis_adjacency_information()
     #host_xml=etree.tostring(host, pretty_print=True, encoding='unicode')
     #print(host_xml)
     isis=dev.cli("show configuration protocols isis | display set")
     isis_adj=dev.rpc.get_isis_adjacency_information({"format": "text"}).text

     out.write(facts)
     out.write(isis_adj)
     out.write(isis)

out.close()
print("Finished in %f sec." % (time.time() - time_start))
print (" check data on following path \"C:\\Users\Amr Ali\PycharmProjects\Juniper-PYZ\out.txt\"")

