
'''
If encryption is
X -> A -> B -> C -> D -> E -> Y
Then decryption is
Y -> E -> D -> C -> B -> A -> X
So, if we encrypt in three steps (bruteforcing K0, K1 and K2)
and decrypt in the three steps (bruteforcing K5, K4, K3)
and got the same C, we should have found the key (K0 to K5)

Note that decryption gives Cr Cl and encryption Cl Cr,
so we need to switch before we check

'''

from natasha import ENC, DEC, RF

plain = b'Meet_NataSHA_which_is_not_a_SHA_although'
cipher = bytes.fromhex('ae055b48d8fa60bc337ff846ee88fe33c7e026a5ea54dbb59814c68265540cef1c183ef746553686')
cipher_two = bytes.fromhex('8c4febe7e2f0a6d43110d37576535b8518eaa4b7ce3ac3722816062755aa8b5ed82eadf76e8af6f5')

K0, K1, K2, K3, K4, K5 = b'', b'', b'', b'', b'', b''
keys = []

# store all possible values of C from the encryption side
print('computing all possible values of C from the encryption side...')
encryption_cs = {}
for i in range(2**24):
    potential_key = i.to_bytes(3, byteorder='big')
    k0, k1, k2 = potential_key[0:1], potential_key[1:2], potential_key[2:3]

    L, R = plain[0:20], plain[20:40]
    R, L = RF(L, R, k0) # a
    R, L = RF(L, R, k1) # b
    R, L = RF(L, R, k2) # c

    encryption_cs[R + L] = potential_key
print('Done.')

# calculate all possible values of C from the decryption
# when we find a match with our encryption C's
# we have found the key
print('checking all possible values of C from the decryption side...')
decryption_cs = []
for i in range(2**24):
    potential_key = i.to_bytes(3, byteorder='big')
    k5, k4, k3 = potential_key[0:1], potential_key[1:2], potential_key[2:3]

    L, R = cipher[0:20], cipher[20:40]
    R, L = RF(L, R, k5) # e
    R, L = RF(L, R, k4) # d
    R, L = RF(L, R, k3) # c

    if (L + R) in encryption_cs.keys():
        print("match found")
        first_key_half = encryption_cs[L + R]
        keys.append(first_key_half + k3 + k4 + k5)


# Just in case, we found more than one key
# we decrypt the second cipher text, with all the keys
# and whichever produces a meaningful result is the right one
print("verifying key(s) with second ciphertext...")
for key in keys:
    print(key)
    print(DEC(cipher_two, key))