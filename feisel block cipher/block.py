from Crypto.Hash import MD5
from Crypto.Util.strxor import strxor 
import md5x3

md5 = MD5.new()
plain = b'*THIS_IS_A_TEST_INPUT_FOR_MD5X3*'
cipher = 'f1eba0e1e77269c82f29b7a695dc7ae4899991ebcbeafe1c6a5fdb873621f750'
# convert cipher from hex to bytes
cipher = bytes.fromhex(cipher)

K0, K1, K2, K3, K4, K5, key = b'', b'', b'', b'', b'', b'', b''

# split plain and cipher text
L0 = plain [0:int((len(plain)/2))]
R0 = plain [int((len(plain)/2)):int(len(plain))]
L3 = cipher[0:int((len(cipher)/2))]
R3 = cipher[int(len(cipher)/2):int(len(cipher))]

# calculate all possible L0 + MD5(K0|R0|K1)
first_outputs = {}
for i in range(2**16):
    RK = i.to_bytes(2, byteorder='big')
    res = md5x3.RF(L0, R0, RK)[0]
    first_outputs[res] = (RK[0:1], RK[1:2])

# calculate all possible L3 + MD5(K4|R3|K5)
count = 0
print()
third_outputs = []
for i in range(2**16):
    RK = i.to_bytes(2, byteorder='big')
    res = md5x3.RF(L3, R3, RK)[0]

    if res in first_outputs.keys():
        print("FOUND A MATCH!!!!")
        K0, K1 = first_outputs[res]
        K4, K5 = RK[0:1], RK[1:2]
        break

print(f"K0: {K0}, K1: {K1}, K4: {K4}, K5: {K5}")
print("In hex:")
print(f"K0: {K0.hex()}, K1: {K1.hex()}, K4: {K4.hex()}, K5: {K5.hex()}")

print()
# brute force to find the middle two bytes of the key
for i in range(2**16):
    RK = i.to_bytes(2, byteorder='big')
    guess_key = b'' + K0 + K1 + RK + K4 + K5

    # if encoding the plain text with this potential key gives us the cipher, 
    # we know this potential key is the actual key
    if md5x3.ENC(plain, guess_key) == cipher:
        print("FOUND THE REST OF THE KEY!!!")
        K2 = RK[0:1]
        K3 = RK[1:2]
        key = guess_key
        break

print(f"Key is {key}")
print("In hex:")
print(f"Key is {key.hex()}")






