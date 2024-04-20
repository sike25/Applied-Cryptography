from Crypto.Cipher import AES
from Crypto.Hash import HMAC, MD5, SHA256
from Crypto.Util.strxor import strxor

# init variables we need to do the decryption
key = ''
iv = ''
encrypted = ''

# constants
header_length = 9
mac_length = 32

# read the message from the binary file
file_path = 'message.bin'
message = ''
with open(file_path, 'rb') as file:
    message = file.read()

# extract the iv from the message
header = message[0 : header_length]
iv = message [header_length : header_length + AES.block_size]  

# extract the ciphertext from the message
encrypted = message [header_length + AES.block_size : - mac_length]


'''
MAC key = MD5(Xi + Ti)
We know Xi from prngstate.txt. And we know Ti is earlier than 12:10 on March 19, 2022
So less than '2022031912100000'
If we decremented '2022031912100000' and computed the MAC key until we verified the MAC successfully,
we would have found Ti and the MAC key.

'''
# get the mac key...........
X_i = bytes.fromhex('b5562ff25e66e602eae4dbd61b2d5e8b')
T_i = '2022031912100000'.encode('utf-8')

message_mac = message [-mac_length:] 
right_mac_key = ''    

while True and int(T_i.decode()) > 0:
    # generate mac key with T_i
    H = MD5.new()
    H.update(strxor(X_i, T_i))
    mac_key = H.digest()

    # compute mac with mac_key
    MAC = HMAC.new(mac_key, digestmod=SHA256)
    MAC.update(header)
    MAC.update(iv)
    MAC.update(encrypted)
    computed_mac = MAC.digest()

    # verify our computed mac by checking it against the message mac
    if (computed_mac == message_mac):
        print("MAC key found.")
        right_mac_key = mac_key
        break

    # if we still have not found the right key, decrement T_i
    T_i = str(int(T_i.decode()) - 1).encode()


'''
ENC key = MD5(MAC_key + Xi + Tj)
We now know both Xi and the MAC key. We know Tj is after Ti.
So we increment Ti until we can achieve decryption
'''
# get the encryption key................
T_j = T_i
while True and int(T_j.decode()) < 2022031912100000:
    # generate enc key with T_j
    H = MD5.new()
    H.update(strxor(strxor(X_i, right_mac_key), T_j))
    enc_key = H.digest()

    # attempt decryption
    DEC = AES.new(enc_key, AES.MODE_CBC, iv)
    decrypted = DEC.decrypt(encrypted)

    # check padding to verify decryption worked
    i = -1
    while (decrypted[i] == 0): i -= 1
    padding = decrypted[i:]
    decrypted = decrypted[:i]
    if (padding[0] == 0x80):
        print("Encryption key found.")
        key = enc_key
        break

    # else, increment T_j
    T_j = str(int(T_j.decode()) + 1).encode()

# decrypt the ciphertext
DEC = AES.new(key = key, mode = AES.MODE_CBC, iv = iv)
decrypted = DEC.decrypt(encrypted)
print("Decrypting ciphertext....")
print(decrypted)