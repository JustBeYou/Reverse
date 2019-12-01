Again, there is a place filled with nops before the `main()` function ends. This time `call_me(int a1, char *a2)` has 2 requirements:
- a1 == 0x1337
- strncmp(a2, "CNS", 3) == 0

*image attached*

Patched with IDA and got the flag.

CNS_CTF{Asta-i_tuica_de_Tulcea}
