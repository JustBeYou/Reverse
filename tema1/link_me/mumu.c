void string_xor_with_key(unsigned char * s, int n, unsigned char key) {
    for (int i = 0; i < n; i++) {
        s[i] ^= key;
    }
}

unsigned int array_sum(unsigned int *arr, int n) {
    unsigned int s = 0;
    for (int i = 0; i < n; i++) {
        s += arr[i];
    }
    return s;
}

