The service is vulnerable to a buffer overflow and the binary has no protections at all, there is no PIE, no stack canary and the stack is executable, so no NX. We need to exploit it in two stages.

1. Leak the stack
As we can see, there is a write at the end of `_start` function that prints the whole input buffer. So we can print garbage data from the stack. At offset 80 in the input buffer there is a stack address (check it in gdb). The problem is that the program will exit after the input is printed, but we can overcome that by using the buffer overflow vulnerability. The saved RIP is at offset 72 from our input buffer. We can simply replace the saved RIP with the address of `_start` and execute the program again. 

So, for the first stage we'll send `"A" * 72 + address of _start`, then we'll receive the stack content, containing pointers to the stack. Our leak is done.

2. Gaining shell
We just need to do the classic `jump to esp` exploit. We replace the saved RIP with the address of our buffer and we place a shellcode in it. We have 72 bytes of space for the shellcode and that's a lot. I used the `shellcraft` module from `pwntools` to automatically generate it.

Exploit script attached.
