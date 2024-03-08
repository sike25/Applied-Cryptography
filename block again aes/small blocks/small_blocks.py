#######################################################################################
### HELPER FUNCTIONS

# Convert strings into lists
def stringToByteList(str):
    # Remove spaces and then slice into chunks of two characters
    return [str.replace(" ", "") [i:i+2] for i in range(0, len(str.replace(" ", "")), 2)]

def xorHexStrings(stra, strb):
    # Remove spaces and convert to integers
    inta = int(stra.replace(" ", ""), 16)
    intb = int(strb.replace(" ", ""), 16)

    # XOR the integers
    result_int = inta ^ intb

    # Convert the result back to hex, removing the '0x' prefix and making it uppercase
    return format(result_int, 'x').lower()

# Crypto.Util.strxor
# read in the cipher as a byte string
# just work with bytes

#######################################################################################

# Preceding Bytes
iv = "d0"
pre_name = "83"
pre_addr = "52"
pre_post = "76"


# Ciphertext for Missing Information
name = "2e 32 4e b1 5a b0 d1 26 13 85 e0"
address = "09 3c 9f 91 61 bb 68 9f 0f 4c 83 a6 2b ac eb 0b 24 8d 5f 3c 13 88"
postal_code = "ac f7 2a 87 a7"

name_list = stringToByteList(name)
address_list = stringToByteList(address)
postal_code_list = stringToByteList(postal_code)

# Total Information
total_cipher = ("96 0e f4 9d e0 ec 1d 52 73 87 48 af 20 a9 1c c4 "
                "98 61 66 fe 4d 67 78 2d 21 1b aa 54 b1 84 f1 fa " 
                "36 d6 bd 68 87 47 b1 5a 7f 58 88 f8 a7 77 9f 0e " 
                "7f 0d 51 b1 44 c7 11 5d 7b 56 74 87 45 a8 36 6e " 
                "92 45 3c 4e 40 12 15 e8 cb 07 c8 fb e1 1c f4 fc " 
                "9d ef ce 4a af 20 13 ba 08 70 c9 ab f3 18 70 fe " 
                "ce 95 35 57 b1 68 69 a5 bc 82 a6 0b 40 7f be 26 " 
                "d4 47 d9 ff b5 9d 64 42 53 b7 84 ca bf 28 06 f2 " 
                "cb bf 2b ac 1a 40 49 1f 67 ad a4 c1 f8 e7 e7 7c " 
                "19 83 4b 3a e2 6d 8e de 30 58 51 da ab 39 14 4c " 
                "83 ca d5 b9 84 f1 d1 ca 3e 50 8b 25 b6 2e 50 74 " 
                "76 22 e6 26 e6 bc f7 96 45 7d 58 83 6f 76 29 4e " 
                "40 c8 6a da 30 94 fd 31 a9 7c 03 f4 df 86 25 14 " 
                "51 0c 9a 86 65 9f 07 01 f2 d7 90 86 45 79 e2 c2 " 
                "04 49 e9 ce fd 8a 1a 9e 86 5f 73 c5 ab b8 72 8d " 
                "48 c8 ff 82 ee cb 11 09 b0 41 d8 ab 63 02 70 22 " 
                "e6 e1 ec ec dd ff 81 39 74 d3 27 24 21 19 83 2e " 
                "32 4e b1 5a b0 d1 26 13 85 e0 d5 6c 03 f2 96 45 " 
                "ea fa 1d 52 09 3c 9f 91 61 bb 68 9f 0f 4c 83 a6 " 
                "2b ac eb 0b 24 8d 5f 3c 13 88 dd 8c f5 cb 27 2d " 
                "a5 d0 b9 bc 44 c3 46 12 a0 2b db ee 5c c9 cf 28 " 
                "ad 1a 40 12 5d ba f3 f7 4d 7b 21 76 ac f7 2a 87 "  
                "a7 46")

total_plain = ("50 6c 65 61 73 65 2c 20 66 69 6c 6c 20 74 68 65 "
                "20 66 6f 72 6d 20 62 65 6c 6f 77 20 77 69 74 68 " 
                "20 79 6f 75 72 20 64 61 74 61 2e 20 4d 61 6b 65 " 
                "20 73 75 72 65 20 79 6f 75 20 65 6e 74 65 72 20 " 
                "64 61 74 61 20 61 73 20 69 74 20 69 73 20 77 72 " 
                "69 74 74 65 6e 20 69 6e 20 79 6f 75 72 20 69 64 " 
                "65 6e 74 69 74 79 20 64 6f 63 75 6d 65 6e 74 2c " 
                "20 73 75 63 68 20 61 73 20 79 6f 75 72 20 70 61 " 
                "73 73 70 6f 72 74 20 6f 72 20 64 72 69 76 69 6e " 
                "67 20 6c 69 63 65 6e 73 65 2e 20 49 66 20 79 6f " 
                "75 72 20 64 61 74 61 20 69 73 20 69 6e 61 63 63 " 
                "75 72 61 74 65 2c 20 77 65 20 63 61 6e 6e 6f 74 " 
                "20 67 75 72 61 6e 74 65 65 20 74 68 65 20 64 65 " 
                "6c 69 76 65 72 79 20 6f 66 20 79 6f 75 72 20 6f " 
                "72 64 65 72 2e 20 54 68 61 6e 6b 20 79 6f 75 20 " 
                "66 6f 72 20 79 6f 75 72 20 75 6e 64 65 72 73 74 " 
                "61 6e 64 69 6e 67 2e 0a 0a 4e 61 6d 65 3a 20 ?? " 
                "?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 0a 41 64 64 72 65 " 
                "73 73 3a 20 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? " 
                "?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 0a 43 69 74 79 3a " 
                "20 57 61 73 68 69 6e 67 74 6f 6e 20 44 43 0a 50 " 
                "6f 73 74 61 6c 20 63 6f 64 65 3a 20 ?? ?? ?? ?? " 
                "?? 0a")

cipher_list = stringToByteList(total_cipher)
plain_list = stringToByteList(total_plain)

# X_j = Y_(i-1) + Y_(j-1) + X_i 
decrypted_map = {}

# Decrypt Name
for i, enc_byte in enumerate(name_list):
    index = cipher_list.index(enc_byte)

    plain = plain_list[index] # X_i
    if plain == "??":
        decrypted_map[enc_byte] = plain
        continue

    Y_prev_av = "" # Y_(i-1)
    if index == 0:
        Y_prev_av = iv
    else:
        Y_prev_av = cipher_list[index - 1]

    Y_prev_ms = "" # Y_(j-1)
    if i == 0:
        Y_prev_ms = pre_name
    else:
        Y_prev_ms = name_list[i - 1]

    result = xorHexStrings(Y_prev_ms, Y_prev_av)
    result = xorHexStrings(result, plain)
    decrypted_map[enc_byte] = result

print("\nName is:")
decryption = ""
for byte in name_list:
    d = decrypted_map[byte]
    if d == "??":
        decryption += "_"
    else:
        decryption += bytes.fromhex(d).decode('ascii')
print(decryption)


# Decrypt Address
for i, enc_byte in enumerate(address_list):
    index = cipher_list.index(enc_byte)

    plain = plain_list[index] # X_i
    if plain == "??":
        decrypted_map[enc_byte] = plain
        continue

    Y_prev_av = "" # Y_(i-1)
    if index == 0:
        Y_prev_av = iv
    else:
        Y_prev_av = cipher_list[index - 1]

    Y_prev_ms = "" # Y_(j-1)
    if i == 0:
        Y_prev_ms = pre_addr
    else:
        Y_prev_ms = address_list[i - 1]

    result = xorHexStrings(Y_prev_ms, Y_prev_av)
    result = xorHexStrings(result, plain)
    decrypted_map[enc_byte] = result

print("\nAddress is:")
decryption = ""
for byte in address_list:
    d = decrypted_map[byte]
    if d == "??":
        decryption += "_"
    else:
        decryption += bytes.fromhex(d).decode('ascii')
print(decryption)


# Decrypt Postal Code
for i, enc_byte in enumerate(postal_code_list):
    index = cipher_list.index(enc_byte)

    plain = plain_list[index] # X_i
    if plain == "??":
        decrypted_map[enc_byte] = plain
        continue

    Y_prev_av = "" # Y_(i-1)
    if index == 0:
        Y_prev_av = iv
    else:
        Y_prev_av = cipher_list[index - 1]

    Y_prev_ms = "" # Y_(j-1)
    if i == 0:
        Y_prev_ms = pre_post
    else:
        Y_prev_ms = postal_code_list[i - 1]

    result = xorHexStrings(Y_prev_ms, Y_prev_av)
    result = xorHexStrings(result, plain)
    decrypted_map[enc_byte] = result


print("\nPostal Code is:")
decryption = ""
for byte in postal_code_list:
    d = decrypted_map[byte]
    if d == "??":
        decryption += "_"
    else:
        decryption += bytes.fromhex(d).decode('ascii')
print(decryption)

        






  # Available Information
# available_cipher = ("96 0e f4 9d e0 ec 1d 52 73 87 48 af 20 a9 1c c4 " 
#                    "98 61 66 fe 4d 67 78 2d 21 1b aa 54 b1 84 f1 fa " 
#                    "36 d6 bd 68 87 47 b1 5a 7f 58 88 f8 a7 77 9f 0e "
#                    "7f 0d 51 b1 44 c7 11 5d 7b 56 74 87 45 a8 36 6e "
#                    "92 45 3c 4e 40 12 15 e8 cb 07 c8 fb e1 1c f4 fc "
#                    "9d ef ce 4a af 20 13 ba 08 70 c9 ab f3 18 70 fe "
#                    "ce 95 35 57 b1 68 69 a5 bc 82 a6 0b 40 7f be 26 "
#                    "d4 47 d9 ff b5 9d 64 42 53 b7 84 ca bf 28 06 f2 "
#                    "cb bf 2b ac 1a 40 49 1f 67 ad a4 c1 f8 e7 e7 7c "
#                    "19 83 4b 3a e2 6d 8e de 30 58 51 da ab 39 14 4c "
#                    "83 ca d5 b9 84 f1 d1 ca 3e 50 8b 25 b6 2e 50 74 "
#                    "76 22 e6 26 e6 bc f7 96 45 7d 58 83 6f 76 29 4e "
#                    "40 c8 6a da 30 94 fd 31 a9 7c 03 f4 df 86 25 14 "
#                    "51 0c 9a 86 65 9f 07 01 f2 d7 90 86 45 79 e2 c2 "
#                    "04 49 e9 ce fd 8a 1a 9e 86 5f 73 c5 ab b8 72 8d "
#                    "48 c8 ff 82 ee cb 11 09 b0 41 d8 ab 63 02 70 22 "
#                    "e6 e1 ec ec dd ff 81 39 74 d3 27 24 21 19 83 "
#                    "d5 6c 03 f2 96 45 "
#                    "ea fa 1d 52 "
#                    "dd 8c f5 cb 27 2d "
#                    "a5 d0 b9 bc 44 c3 46 12 a0 2b db ee 5c c9 cf 28 "
#                    "ad 1a 40 12 5d ba f3 f7 4d 7b 21 76 " 
#                    "46")

# available_plain = ( "50 6c 65 61 73 65 2c 20 66 69 6c 6c 20 74 68 65 "
#                     "20 66 6f 72 6d 20 62 65 6c 6f 77 20 77 69 74 68 "
#                     "20 79 6f 75 72 20 64 61 74 61 2e 20 4d 61 6b 65 "
#                     "20 73 75 72 65 20 79 6f 75 20 65 6e 74 65 72 20 "
#                     "64 61 74 61 20 61 73 20 69 74 20 69 73 20 77 72 "
#                     "69 74 74 65 6e 20 69 6e 20 79 6f 75 72 20 69 64 "
#                     "65 6e 74 69 74 79 20 64 6f 63 75 6d 65 6e 74 2c "
#                     "20 73 75 63 68 20 61 73 20 79 6f 75 72 20 70 61 "
#                     "73 73 70 6f 72 74 20 6f 72 20 64 72 69 76 69 6e "
#                     "67 20 6c 69 63 65 6e 73 65 2e 20 49 66 20 79 6f "
#                     "75 72 20 64 61 74 61 20 69 73 20 69 6e 61 63 63 "
#                     "75 72 61 74 65 2c 20 77 65 20 63 61 6e 6e 6f 74 "
#                     "20 67 75 72 61 6e 74 65 65 20 74 68 65 20 64 65 "
#                     "6c 69 76 65 72 79 20 6f 66 20 79 6f 75 72 20 6f "
#                     "72 64 65 72 2e 20 54 68 61 6e 6b 20 79 6f 75 20 "
#                     "66 6f 72 20 79 6f 75 72 20 75 6e 64 65 72 73 74 "
#                     "61 6e 64 69 6e 67 2e 0a 0a 4e 61 6d 65 3a 20 "
#                     "0a 41 64 64 72 65 "
#                     "73 73 3a 20 "
#                     "0a 43 69 74 79 3a "
#                     "20 57 61 73 68 69 6e 67 74 6f 6e 20 44 43 0a 50 "
#                     "6f 73 74 61 6c 20 63 6f 64 65 3a 20 "
#                     "0a")

# av_cipher_list = stringToByteList(available_cipher)
# av_plain_list = stringToByteList(available_plain)
