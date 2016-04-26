import sys
from scapy.all import*
dst_ip=raw_input("Enter the IP address: ")
scr_port=RandShort()
ports=range(0,101)
openports=[]
closedports=[]
filteredports=[]
openport=[]
closedport=[]
openfilteredpo=[]
filteredport=[]
openfilteredport=[]
openfilteredports=[]
openfilteredpor=[]
#section 1
for port in ports:
	conf.verb=0
	scan=sr1(IP(dst=dst_ip)/UDP(dport=port),timeout=10)
	if str(type(scan))=="<type 'NoneType'>":
		openfilteredports.append(port)
		continue
	elif scan.haslayer(ICMP):
		if str(scan.getlayer(ICMP).type)=='3' and str(scan.getlayer(ICMP).code)=='3':
			closedports.append(port)
#section 2
temp=openfilteredports
for por in temp:
	conf.verb=0
	scan=sr1(IP(dst=dst_ip)/UDP(dport=por),timeout=20)
	if str(type(scan))=="<type 'NoneType'>":
		openfilteredport.append(por)
		continue
#section 3
temp1=openfilteredport
for po in temp1:
	conf.verb=0
	scan=sr1(IP(dst=dst_ip)/UDP(dport=po),timeout=20)
	if str(type(scan))=="<type 'NoneType'>":
		openfilteredpor.append(po)
		continue	
#section 4w
temp2=openfilteredpor
for p in temp2:
	conf.verb=0
	scan=sr1(IP(dst=dst_ip)/UDP(dport=p),timeout=30)
	if str(type(scan))=="<type 'NoneType'>":
		openfilteredpo.append(p)
		continue
	elif scan.haslayer(UDP):
		openport.append(p)
	elif scan.haslayer(ICMP):
		if str(scan.getlayer(ICMP).type)=='3' and str(scan.getlayer(ICMP).code) in ['0','1','2','9','10','13']:
			filteredport.append(p)

print "OPEN PORTS: \n",openport
print "CLOSED PORTS: \n",closedports
print "FILTERED PORTS: \n",filteredport
print "OPEN/FILTERED PORTS: \n",openfilteredpo



