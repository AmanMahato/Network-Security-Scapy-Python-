import sys
from scapy.all import *
import netaddr
network=raw_input("Enter the IP address with subnet mask");
addresses=netaddr.IPNetwork(network);
a=0;
address=[];
for i in addresses:
	address.append(addresses[a]);
	a=a+1
address.remove(addresses.broadcast);
address.remove(addresses.network);	
m=network[-2]+network[-1];
mask=int(m);
p=32-mask;
no_of_host=(2**p)-2;
print "Total Number of host in this network is", no_of_host;
print "The IP address of the host are listed below:"; 
for j in range(0,no_of_host):
	print address[j];
for i in range(0,no_of_host):
	pk=IP(src=address[i])/TCP(dport=[80,53]);
	pk.show();


