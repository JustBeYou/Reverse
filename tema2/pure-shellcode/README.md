Buffer overflow, stack based. No protections, stack is executable. Leak the stack and return to main, then jump to RSP and execute shellcode.
