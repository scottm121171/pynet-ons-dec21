import pyeapi
from getpass import getpass
from rich import print

connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable(["show version", "show ip arp"])
print(output)
