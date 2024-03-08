Applied Cryptography
Homework-4 solutions 

Name: Osasikemwen Ogieva    
E-mail: oogieva25@amherst.edu   

=======================================  
Challenge-1: Small blocks (2 points)  
---------------------------------------  
Recovered personal data:  

Name: T_omas Co_k   
Address: 1nt_o_st_tutio_ Avenue   
Postal code: 20_02   
  
The name is most likely: Thomas Cook   
The address is likely: '1st Constitution Avenue'   
A Google search rveals that Constitution Avenue is in the 
Washington DC zip code: 20002   

---------------------------------------   
Steps of your solution (brief description that is just enough to reproduce your solution):

Attack script is attached, small_blocks.py

For each encrypted byte of the missing information, 
check the rest of the cipher for a match.
If one is found, collect:
    a. its plain, X_i
    b. the cipher byte before the match, Y_(i-1)
    c. the cipher byte before the cipher byte we are trying to decrypt, Y_(j-1)
XOR all three. This gives us the plain X_j for our encrypted byte.
Convert to ASCII and print.




=======================================
Challenge-2: Padding Oracle (2 points)
---------------------------------------
Recovered plaintext block: Congrats4crackin

The right values for the placeholders:
__TODO_1__ =  b'\x00' * 16
__TODO_2__ =  R + Y
__TODO_3__ =  :i
__TODO_4__ =  i+1:
__TODO_5__ =  R[16-plen-1] ^ P[0]



================================================
Challenge-3: One, Two, Buckle my Shoe (4 points)
------------------------------------------------
The FLAG (the string after the "FLAG: " tag) in the plaintext:
AES-CTR_MUST_NEVER_RE-USE_CTRS

The name of the malware analyzed by the CrySyS Lab in May 2012 in an international collaboration:
sKyWIper

What is the 4 padding bytes at the end of the decoded plaintext? Provide your answer as a hex string (e.g., 1234abcd):
01000000
☺

Attach, in a separate file, your attack script that performs your attack and prints out the plaintext recovered.
one_two.py

