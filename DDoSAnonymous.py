import os
import platform
print ("Anonymous Haker Alon Darker")
print ("DoS Attack")
print ("Facebook:https://www.facebook.com/alonkreker.hacker ")
print ("Facebook:https://www.facebook.com/AlonKreker ")
print ("Instagram:https://www.instagram.com/hacktoni10/ ")
print ("E-mail:anonyusdarker0@protonmail.com ")
print ("GitHub:https://github.com/Anonimus-Haker-Alon-Kreker-Darker?after=Y3Vyc29yOnYyOpK0MjAyMS0xMi0wOVQxNjo0MToxOFrOGgdZKA%3D%3D&tab=repositories ")
print ("YouTube:https://www.youtube.com/channel/UCWr7FLzT4LDkusCVIB61GeQ ")
from datetime import datetime
net = input("Enter the Network Address: ")
net1= net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
oper = platform.system()

if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "
t1 = datetime.now()
print ("Scanning in Progress:")

for ip in range(st1,en1):
   addr = net2 + str(ip)
   comm = ping1 + addr
   response = os.popen(comm)
   
   for line in response.readlines():
      if(line.count("TTL")):
         break
      if (line.count("TTL")):
         print (addr, "--> Live")
         
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: ",total)