
def findKey():
    most_frequent_bytes = [b'\x73', b'\x13', b'\x43', b'\x52', b'\x13', b'\x54']
    # XOR with space character
    for byte in most_frequent_bytes:
        print(xor_bytes(byte, b'\x20'))

def xor_bytes(byte_a, byte_b):
    result = bytes([byte_a[0] ^ byte_b[0]])    
    return result

findKey()


