break main
break *0x400596
break *0x400589
r
set {char [8]} 0x0601300 = "rc4"
x/s 0x0601300
set $rip=0x400546
set $rdi=0x0601300
set $rsi=3
c
ni
set $rsi=0x6010E0
c
x/s 0x6010E0
