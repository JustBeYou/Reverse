If you take a look in `_start` stub, you'll see that the first argument to `__libc_start_main()` is address of `dummy()` instead of `main()`. Change the instruction `mov rdi, &dummy` to `mov rdi, &main` and you've got the flag.

CNS_CTF{They're_coming_to_take_me_away_ha_ha}
