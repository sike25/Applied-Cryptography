from functools import reduce

def string_to_blocks(s, block_size=16):
    byte_data = s.encode()
    return [byte_data[i:i + block_size] for i in range(0, len(byte_data), block_size)]

def xor_blocks(blocks):
    result = blocks[0]
    for block in blocks[1:]:
        result = bytes(a ^ b for a, b in zip(result, block))
    return result

def test_xor_balance(original_record, modified_record):
    original_blocks = string_to_blocks(original_record)
    modified_blocks = string_to_blocks(modified_record)

    original_mac = xor_blocks(original_blocks)
    modified_mac = xor_blocks(modified_blocks)

    return original_mac == modified_mac

original_record = "2020:02:23|11:23:38|21450|A74635|B29846|00002500"
modified_record = "2020:02:23|11:27:38|21459|A74635|B29846|90002504"

if test_xor_balance(original_record, modified_record):
    print("XOR balance maintained.")
else:
    print("XOR balance disrupted.")
