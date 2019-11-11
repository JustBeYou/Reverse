After analyzing the algorithm we can conclude it's rc4. We can reuse the existing functions in the binary and just change their arguments.

GDB script for solving the challenge. `solve_bonus.gdb`:
```bash
break main
break *0x400596 # break before the call of 0x400730
break *0x400589 # break before the return of decrypt_flag
r
set {char [8]} 0x0601300 = "rc4" # write the string in some writable area
set $rip=0x400546  # the the RIP to decrypt_flag address
set $rdi=0x0601300 # first argument, the key
set $rsi=3         # second argument, the key's length
c
ni
set $rsi=0x6010E0  # set the decryption target to be "bonus_flag"
c
x/s 0x6010E0       # output the flag
```

Run with `gdb ./hidden -x solve_bonus.gdb`

CNSCTF_{Stream_ciphers_for_the_win}
