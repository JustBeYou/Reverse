1. The service simply reads a string from the user and stores it in a buffer. There is a little bug that allows you a one byte leak. The string terminator (NUL) is put at the offset `your string length + 1`, that means that the final string will contain one garbage character. 
2. The flag is already in the input buffer at position 12. You can leak it byte by byte sending strings of length `12 + offset`.
3. Flags characters were encrypted using the following expression `flag[i] = flag[i] ^ i`. Knowing the current index is easy to decrypt it.

Solving script attached.
