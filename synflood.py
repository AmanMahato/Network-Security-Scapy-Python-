import sys
from scapy.all import*
address=raw_input("Enter the IP address of the target: ")
pot=input("Enter the destination port of the target machine: ")
p=IP(dst=address,id=1111,ttl=99)/TCP(sport=RandShort(),dport=pot,seq=12345,ack=1000,window=1000,flags="S")
ans,unans=srloop(p,inter=0.1,retry=2,timeout=4)
ans.summary()
unans.summary()
ans.make_table(lambda(s,r):((s.dst,s.dport,r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%"))))


