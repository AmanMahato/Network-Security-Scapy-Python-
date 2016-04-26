import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
ip=raw_input("Enter the IP address of the target: ")
closed=0
closep=[]
openp=[]
filterp=[]
def is_up(ip):
	