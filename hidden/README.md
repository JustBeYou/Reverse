Break on main. The target function is 0x400599. Set the RIP and the arguments in GDB.
```
gef➤  set $rip=0x400599
gef➤  set $rdi=20035
gef➤  set $rsi=17235
gef➤  set $rdx=55274-17235-20035
gef➤  set $rcx=0x601144
gef➤  c
Continuing.
CNS_CTF{The_zombies_were_having_fun_the_party_had_just_begun}
```
