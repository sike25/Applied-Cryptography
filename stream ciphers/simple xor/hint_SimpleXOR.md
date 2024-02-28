Simple XOR cipher
=================

The simple XOR cipher uses some short string as the key, which is repeated as many times as needed to cover the entire plaintext to be encrypted. The repeated key string is then XORed to the plaintext byte-by-byte. Using a periodic string in the XOR operation is a weakness. First, one needs to determine the period length (i.e., the length of the key string) and then the key string itself with which the ciphertext can be decrypted. 

First one should compute the byte statistics (ordered byte frequencies) for the given `ciphertext.txt` by running
```bash
   python3 stat.py -i ciphertext.txt
```
and determine the width W of the byte distribution and the frequency F of the most frequent byte in the ciphertext.

Then, sample the ciphertext bytes by running

```bash
   python3 sample.py -l plength -f 0 -i ciphertext.txt -o ciphertext_plength_0.txt
```

for different values 2, 3, ... of `plength`, and for each of these sampled files compute the byte statistics by running

```bash
   python3 stat.py -i ciphertext_plength_0.txt
```

When `plength` is not the right key length value then the width of the distribution will be close to W and the frequency of the most frequent byte will be close to F. When we hit the right key length, the width of the distribution will be much smaller than W and the frequency of the most frequent byte will be much larger than F.

As the most frequent byte in the plaintext is space (`0x20`), when the key length is found, the most frequent byte B in the filtered ciphertext must be the XOR sum of space and the first byte of the key. So the first byte of the key can be computed as B XOR `0x20`.

