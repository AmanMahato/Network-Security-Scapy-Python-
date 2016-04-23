import sys
from scapy.all import *
#Ask destination address from the user and store in the variable address
address=raw_input("Please Enter the destination IP address: "); 
#construct the packet with the destination address taken from the user
p=IP(dst=address)/ICMP();
# used to show the content of the packet.
p.show()
# sr() functio is used to send the packet and receive the answers.
# sr1() is the variant of sr() that only return one packet that answered the packet.
reply=sr1(p);
reply.show()
