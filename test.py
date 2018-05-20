from jnpr.junos import Device
from getpass import getpass
import sys

hostname = raw_input("Device hostname: ")
username = raw_input("Device username: ")
password = raw_input ("Device password: ")

# Telnet connection
dev = Device(host=hostname, user=username, passwd=password, mode='telnet',port='13')

try:
  dev.open()
except Exception as err:
  print (err)
  sys.exit(1)
print (dev.facts.get("hostname"))
dev.close()