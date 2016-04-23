from scapy.all import*
hostname=raw_input("Enter the IP address of the target: ")
print "traceroute to ",hostname, ",","5 hops max."
print "The packets generated in this Process are: "
for j in range(1,5):
	pk=IP(dst=hostname,ttl=j)/TCP()
	ans=sr1(pk,verbose=0)
	ans.show()

for i in range(1,5):
	pkt=IP(dst=hostname,ttl=i)/TCP()
	reply=sr1(pkt,verbose=0)
	if reply is None:
		break
	elif reply.type==3:
		print "%d hops away:  " %i,reply.src
		print "Done!!!"
		break
	else:
		print "%d hops away:  " %i, reply.src
