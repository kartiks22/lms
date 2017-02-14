import requests
from bs4 import BeautifulSoup
from getpass import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning

a=raw_input("username : ")
b=getpass("password : ")

data={"username":a,"password":b}
url="https://lms.iiitb.ac.in/moodle/login/"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
r=requests.post(url,data=data,verify=False)
page = BeautifulSoup(r.content,"html.parser")
g_data = page.find_all("li",{"class":"listentry"})

for item in g_data:
	print item.contents[0].text
	