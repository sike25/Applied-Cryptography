Hints for challenge MD5x3
=========================

A key observation is that the rounds of MD5x3 use independent subsets of the key: the first round uses the first 2 bytes of the key, the second round uses the next 2 bytes, and finally, the third round uses the last 2 bytes of the key. Also, by looking at the internal structure of the cipher, we can see that

    L0 + MD5(K0|R0|K1) = L3 + MD5(K4|R3|K5)

where L0, R0, L3, R3 are known (as L0|R0 is the test plaintex block and L3|R3 is the corresponding ciphertext block).

We can mount a meet-in-the-middle attack and determine K0, K1, K4, K5 in the following way: First, we compute and store L0 + MD5(K0|R0|K1) for all possible 2^16 values of (K0, K1). Then, we compute L3 + MD5(K4|R3|K5) for all possible values of (K4, K5), and for each computed value, we check if it is among the previously computed values of L0 + MD5(K0|R0|K1). When a match is found, we have both the right (K0, K1) and the right (K4, K5).

The remaining 2 bytes (K2, K3) can be found by brute force... 

