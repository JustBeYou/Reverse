Classic buffer overflow vulnerability and there is a "win" function too. The offset from the input buffer to the saved RIP is 40 bytes. As there is no PIE protection or stack canary, we can simply set the saved RIP to another address from the binary. So, we'll send `"A" * 40 + address of make_it_easy`.

Solving script attached.
