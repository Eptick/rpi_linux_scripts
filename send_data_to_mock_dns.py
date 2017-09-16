import urllib
import urllib2
from subprocess import *
data = check_output(["ifconfig wlan0 | grep HWaddr"], stderr=STDOUT, shell=True)
data_array = data.split(" ")
mac_addr = ""
for i in range(0, len(data_array) ):
	if(data_array[i] == "HWaddr"):
		mac_addr = data_array[i+1]
		break
data = check_output(["hostname -I"], stderr=STDOUT, shell=True)
ip = data.strip()
data = check_output(["iwgetid -r"], stderr=STDOUT, shell=True)
wlan_name = data.strip()
dns_ip = "http://raspberry-dns.herokuapp.com"
url = dns_ip
values = {'mac' : mac_addr,
          'ip' : ip,
          'ssid' : wlan_name }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print(the_page)
