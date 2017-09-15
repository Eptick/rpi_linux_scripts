from subprocess import *
data = check_output(["ifconfig wlan0 | grep HWaddr"], stderr=STDOUT, shell=True)
data_array = data.split(" ")
mac_addr = ""
for i in range(0, len(data_array) ):
	if(data_array[i] == "HWaddr"):
		mac_addr = data_array[i+1]
		break
print(mac_addr)
data = check_output(["hostname -I"], stderr=STDOUT, shell=True)
print(data)
ip = data
