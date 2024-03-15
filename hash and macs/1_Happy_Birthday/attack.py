from Crypto.Hash import MD5
import itertools

def trhash(x):
	h = MD5.new()
	h.update(x)
	return h.digest()[0:4]



# positive message

place_one = ['Dear ', 'Hello ']
place_two = ['Mr. ', 'Mister ']
place_three = ['Jones, ', 'Jones,  ']
place_four = ["I'm ", 'I am ']
place_five = ['delighted to ', 'happy to ']
place_six = ['inform you that ', 'let you know that ']
place_seven = ['you have been ', ' you have been ']
place_eight = ['selected as ', 'chosen as ']
place_nine = ['one of the ', 'one of the  ']
place_ten = ['winners of our ', 'lucky winners of our ']
place_eleven = ['competition', 'contest']
place_twelve = ['. ', '! ']
place_thirteen = ['Your prize will ', 'Your reward will ']
place_fourteen = ['be ', 'be  ']
place_fifteen = ['1,000,000 ', 'one million ']
place_sixteen = ['USD, ', 'dollars, ']
place_seventeen = ['which we will transfer to your bank account within one week. ', 'which we will transfer to your bank account within seven days. ']
place_eighteen = ['Best regards, Andrew B. Clark', 'Best Regards, Andrew B. Clark']
places = [
     place_one, place_two, place_three, place_four, place_five,
     place_six, place_seven, place_eight, place_nine, place_ten, 
     place_eleven, place_twelve, place_thirteen, place_fourteen,
     place_fifteen, place_sixteen, place_seventeen, place_eighteen
]

def generate_variants(places):
    for combination in itertools.product(*places):
        yield ''.join(combination)

hash_to_positive_variant = {}
variant_generator = generate_variants(places)
for _ in range(2**18):
    variant = next(variant_generator)
    hash = trhash(variant.encode('ascii'))
    hash_to_positive_variant[hash] = variant




# negative message

place_one = ['Dear ', 'Hello ']
place_two = ['Mr. Jones, ', 'Mister Jones, ']
place_three = ['I regret ', 'We regret ']
place_four = ['to inform you that ', 'to let you know that ']
place_five = ['your complaint was ', 'your complaint  was ']
place_six = ['not approved by our management. ', 'rejected by our management. ']
place_seven = ['This, unfortunately means ', 'Unfortunately, this means ']
place_eight = ['that you cannot reclaim your ', "that you can't reclaim your "]
place_nine = ['cost of 1,234 ', 'cost of 1_234 ']
place_ten = ['USD ', 'dollars ']
place_eleven = ['and in addition ', 'and also ']
place_twelve = ['you have to ', 'you are required to ']
place_thirteen = ['cover ', 'pay ']
place_fourteen = ['our investigation cost of 345 ', 'our investigation costs of 345 ']
place_fifteen = ['USD as well. ', 'dollars as well. ']
place_sixteen = ['Yours sincerely, ', 'Yours Sincerely, ']
place_seventeen = ['Andrew B. ', 'Andrew B ']
place_eighteen = ['Clark', 'Clark.']
places_neg = [
     place_one, place_two, place_three, place_four, place_five,
     place_six, place_seven, place_eight, place_nine, place_ten, 
     place_eleven, place_twelve, place_thirteen, place_fourteen,
     place_fifteen, place_sixteen, place_seventeen, place_eighteen
]

variant_generator_neg = generate_variants(places_neg)
# collision variables
positive_variant = ''
negative_variant = ''

for _ in range(2**18):
    variant = next(variant_generator_neg)
    hash = trhash(variant.encode('ascii'))
    
    if hash in hash_to_positive_variant.keys():
        positive_variant = hash_to_positive_variant[hash]
        negative_variant = variant
        break

print(f"Positive variant is: \n{positive_variant}")
print(f"Negative variant is: \n{negative_variant}")

print("The hash values of the negative and postive variants are the same:")
print(trhash(positive_variant.encode('ascii')) == trhash(negative_variant.encode('ascii')))


         
