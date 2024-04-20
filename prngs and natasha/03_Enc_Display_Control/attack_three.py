from Crypto.Util.strxor import strxor
from prng import PRNG

##############################################################
### HELPER FUNCTIONS #########################################

def display(ctrl_seq):
	D = []
	for i in range(10):
		d = []
		for j in range(160):
			d.append(' ')
		D.append(d)
	i, j = 0, 0
	for c in ctrl_seq:
		if c == 0: j += 1
		elif c == 1: j -= 1
		elif c == 2: i += 1
		elif c == 3: i -= 1
		else: D[i][j] = chr(c)
	for i in range(10):
		for j in range(160):
			print(D[i][j], end='')
		print('')
		
def parse_decrypted_message(decrypted_bytes):
    control_sequence = []
    i = 0
    while i < len(decrypted_bytes):
        control_byte = decrypted_bytes[i+2]
        control_sequence.append(control_byte)
        i += 3 
    return control_sequence

############################################################

# try different seeds to see the random bytes they produce
# prng = PRNG()
# seed = b'\x42'
# prng.seed(s = seed)
# print('seed:', seed)
# for i in range(3):
# 	print(prng.get_random_bytes(256))
# print()

# prng = PRNG()
# seed = b'\x10'
# prng.seed(s = seed)
# print('seed:', seed)
# for i in range(3):
#     print(prng.get_random_bytes(256))
# print()

############################################################

print("PRNG Weakness: The 'random' bytes repeat every 256 bytes.")
print()
chunk_size = 256

# load ciphertext from the .crypt file
file_path = 'proto_msgs.crypt'
message = ''
with open(file_path, 'rb') as file:
    message = file.read()

# xor the sequence numbers to the ciphertext to get the keystream
i = 0
keystream = [b'' for _ in range(chunk_size)]
seq_number = b'\x00\x00'
while i < len(message) and b'' in keystream:
	keystream[(i) % 256] = strxor(message[i:i+1], seq_number[0:1])
	keystream[(i + 1) % 256] = strxor(message[i+1:i+2], seq_number[1:2])
	seq_number = (int.from_bytes(seq_number, 'big') + 1).to_bytes(2, 'big')
	i += 3 

# decode the cipher text with the keystream
i = 0
plaintext = b''
while (i < len(message) - 1):
	for key_byte in keystream:
		if i >= len(message):
			break
		plaintext += strxor(key_byte, message[i:i+1])
		i += 1

# extract the contol sequence from the plain text
control_sequence = parse_decrypted_message(plaintext)

# display the control sequence on the screen
display(control_sequence)

  