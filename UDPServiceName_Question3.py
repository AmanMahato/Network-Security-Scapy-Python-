import sys
from scapy.all import*
dst_ip=raw_input("Enter the IP address: ")
pckt=sr1(IP(dst=dst_ip)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="router")))
conf.checkIPaddr=False
fam,hw=get_if_raw_hwaddr(conf.iface)
dhcp_discover=Ether(dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0',dst='10.10.111.1')/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
ans,unans=srp(dhcp_discover,multi=True)
print pckt[DNS].summary
ans.summary()



