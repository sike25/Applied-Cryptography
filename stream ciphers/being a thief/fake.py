#########################################################################
### HELPER FUNCTIONS

def ascii_to_hex(ascii_string):
    return ''.join(format(ord(char), '02x') for char in ascii_string)

def xor_hex_strings(hex1, hex2):
    return hex(int(hex1, 16) ^ int(hex2, 16))[2:].lower()

###########################################################################



###########################################################################
### PART ONE
    # xor the five given accounts with each other

given_accounts_ascii = ["A74635", "B29846", "C12859", "D37465", "E12654"]

hex_xor_results = []
for i in range(len(given_accounts_ascii)):
    for j in range(i+1, len(given_accounts_ascii)):
        accountOne = ascii_to_hex(given_accounts_ascii[i])
        accountTwo = ascii_to_hex(given_accounts_ascii[j])
        xor_result = xor_hex_strings(accountOne, accountTwo)
        hex_xor_results.append((given_accounts_ascii[i], given_accounts_ascii[j], xor_result))

print("The results from XOR-ing all five accounts with each other")
for result in hex_xor_results:
    print(f"{result[0]} XOR {result[1]} = {result[2]}")


################################################################
### PART TWO
        # xor the encrypted destination accounts with each other

encrypted_destination_accounts = [b'ee48ac8f667e', b'e848ac816673', b'e94aa9836572']

xor_results = []
for i in range(len(encrypted_destination_accounts)):
    for j in range(i+1, len(encrypted_destination_accounts)):
        result = xor_hex_strings(encrypted_destination_accounts[i], encrypted_destination_accounts[j])
        xor_results.append((encrypted_destination_accounts[i], encrypted_destination_accounts[j], result))

print()
print("The results from XOR-ing all destination accounts with each other")
for result in xor_results:
    print(f"{result[0]} XOR {result[1]} = {result[2]}")


#####################################################
### PART THREE
    # Decode the destination accounts
    
'''
A74635 XOR B29846 = 03050d0e0703
A74635 XOR C12859 = 0206060e060c
A74635 XOR D37465 = 050403020500
A74635 XOR E12654 = 040606000601
B29846 XOR C12859 = 01030b00010f
B29846 XOR D37465 = 06010e0c0203
B29846 XOR E12654 = 07030b0e0102
C12859 XOR D37465 = 0702050c030c
C12859 XOR E12654 = 0600000e000d
D37465 XOR E12654 = 010205020301

and 

b'ee48ac8f667e' XOR b'e848ac816673' = 600000E000D
b'ee48ac8f667e' XOR b'e94aa9836572' = 702050C030C
b'e848ac816673' XOR b'e94aa9836572' = 10205020301

So we can conclude that:
ee48ac8f667e decodes to C12859
e94aa9836572 decodes to D37465
e848ac816673 decodes to E12654
'''
print()
print("destination accounts decoded...")


#####################################################
### PART FOUR
    # Use cracked destination accounts to find key
    # And encode my bank account with found key

print("using cracked destination accounts to find key...")

cHex = ascii_to_hex("C12859")
dHex = ascii_to_hex("D37465")
eHex = ascii_to_hex("E12654")

keyOne = xor_hex_strings("ee48ac8f667e", cHex)
keyTwo = xor_hex_strings("e94aa9836572", dHex)
keyThree = xor_hex_strings("e848ac816673", eHex)

if (keyOne != keyTwo) or (keyTwo != keyThree):
    print("key discovery failed!")
    print(f"We got {keyOne}, {keyTwo}, and {keyThree}")
else:
    print(f"The destination account key is {keyOne}") # ad799eb75347
    print("encoding my account number with key ....")

my_account = ascii_to_hex("X1337X")
my_account_encoded = xor_hex_strings(my_account, keyOne)
print(f"My encoded account is {my_account_encoded}") # f548ad84641f




#####################################################
### PART FIVE
    # Increment the amount being sent $$$
    # And the transaction numbers

print()
print("incrementing amounts + transaction numbers by replacing their prefixes")

amount_one = "75941d3b78f2bc"
amount_two =  "75941d3a7df7bc"
amount_three = "75941d3b79f4bc"

transaction_one = "dc75d21c"
transaction_two = "dc75d218"
transaction_three = "dc75d11e"

'''
We infer (and hope) that:
"dc 75" is 00 (in the transaction field)
"75 94 1d" is 000 (in the amount field)

if we xor them with zeroes, we retrieve the first key bytes
And can use the key bytes to encode larger digits
to lead both the transaction numbers and amounts of money
'''
transaction_key = xor_hex_strings("dc75", ascii_to_hex("00"))
amount_key = xor_hex_strings("75941d", ascii_to_hex("000"))

fake_amount_start = "999"
fake_transaction_start = "53"

encoded_fake_amount_start = xor_hex_strings(fake_amount_start, amount_key) # 45adb4
encoded_fake_transaction_start = xor_hex_strings(fake_transaction_start, transaction_key) # ec16

print("000 starting the amount number becomes 999, and 00 starting the transaction number becomes 53 ")
print(f"999 encoded is: {encoded_fake_amount_start} and 53 encoded is: {encoded_fake_transaction_start}")


#####################################################
### PART SIX 
    # Put it all together 

'''
Taking the second legitimate transaction:

*dc75* d218 ae 73a7fdb464e0 52 *e848ac816673* ea *75941d*3a7df7bc
    |                                |               |
increment                        replace with    increment
trans no                        my account no        $$$

To become:
ec16d218 ae 73a7fdb464e0 52 f548ad84641f ea 45adb43a7df7bc

'''

print()
print("putting it all together")
fraudulent_transaction = "ec16d218 ae 73a7fdb464e0 52 f548ad84641f ea 45adb43a7df7bc"
print(f"fraudulent transaction is {fraudulent_transaction}")
    


















# So, our matches are:
# C12859 XOR E12654 = 0600000e000d
# b'ee48ac8f667e' XOR b'e848ac816673' = 600000E000D

# C12859 XOR D37465 = 0702050c030c
# b'ee48ac8f667e' XOR b'e94aa9836572' = 702050C030C

# D37465 XOR E12654 = 010205020301
# b'e848ac816673' XOR b'e94aa9836572' = 10205020301