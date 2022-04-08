import base64
import sys
print("Please input your table")
base1=input()
base2="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
if len(base1)!=64:
    print("Wrong table")
    sys.sleep(5)
    sys.exit(1)
print("PLease input your flag")
str=list(input())
flag=""
dec = ""
for i in range(len(str)):
    dec += base2[base1.find(str[i])]
print(base64.b64decode(dec))
sys.sleep(15)
sys.exit(0)